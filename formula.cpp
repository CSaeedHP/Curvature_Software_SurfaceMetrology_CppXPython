#include <iostream>
#include <cmath>
#include <unordered_map> // needed for the hashmap functionalityh
#include <functional> // needed for the function pointer functionality in hashmap implementation
#include "dataContainer.h"

// Define functionPointer as a type alias for a function pointer
typedef double (*functionPointer)(point*, point*, point*);
#include "formula.h"
//OLD: replaced in favor of not using #include <Eigen/Dense> // https://gitlab.com/libeigen/eigen/-/releases/3.4.0 // to download library
using namespace std;
const double PI = 3.14159265358979323846;

    //returns the function map. This is used to determine which function to use based on the user's input
    //store the function map into a variable, use hashmap methods to find correct method and check if exists
    std::unordered_map<int, functionPointer> Formula::funcMap() {
        std::unordered_map<int, functionPointer> functionMap;
    
        functionMap[1] = &Formula::herons;
        functionMap[2] = &Formula::parabola;
        functionMap[3] = &Formula::diffOfSlopes;
        functionMap[4] = &Formula::lagrangian;
        functionMap[5] = &Formula::finiteDiffAnalysis;
    
        return functionMap;
    }
// 1's correspond to first coordinate pair, 2's belong to second coordinate pair, 3's belong to third coordinate pair-----
// this fucntion follows Heron's formula for cuvature---------------------------------------------------------------------
    double Formula::herons (point *point1, point *point2, point *point3){
        double x1 = point1->x, z1 = point1->z, x2 = point2->x, z2 = point2->z, x3 = point3->x, z3 = point3->z, 
               curve, ABX, ABZ, BCX, BCZ, SlopeAB, SlopeBC, yfor, sideA, sideB, sideC, SP;

        ABX = x1-x2;
        ABZ = z1-z2;
        BCX = x2-x3;
        BCZ = z2-z3;
        SlopeAB = (ABZ/ABX);
        SlopeBC = (BCZ/BCX);

        //----------------------------------------------------------------------------------------------------------------
        // formula to determine sign of curvature

        yfor = (SlopeAB * x3) + (z1 - (SlopeAB*x1));

        //----------------------------------------------------------------------------------------------------------------
        // comparing slopes, if slopes are identical, no curvature to calculate in the first place

        if(SlopeAB == SlopeBC){ // straight line
            return 0;
        }
        else{
            sideA = pow((pow(ABX, 2) + pow((ABZ), 2)), 0.5);
            sideB = pow((pow((BCX), 2) + pow((BCZ), 2)), 0.5);
            sideC = pow((pow((x1-x3), 2) + pow((z1-z3), 2)), 0.5);
        }

        // required for herons formula
        SP = ((sideA + sideB + sideC)/2); // Semi Perimeter 
        
        curve = 4*(SP * pow((SP - sideA), 2) * (SP - sideB) * (SP - sideC))/(sideA * sideB * sideC);

        if(z3 < yfor){
            curve = (curve * -1);
        }
        return curve;
    }

// 1's correspond to first coordinate pair, 2's belong to second coordinate pair, 3's belong to third coordinate pair-----
// this function follows a calculus method for determining curvature------------------------------------------------------
    double Formula::parabola (point *point1, point *point2, point *point3){
        double Ax = point1->x, Az = point1->z, Bx = point2->x, Bz = point2->z, Cx = point3->x, Cz = point3->z, 
               a, b, c, Axpow2, Bxpow2, Cxpow2, detM, detMa, detMb, detMc, curve, first_deriv, second_deriv;
        
        // Creating variables representative of this matrix (Matrix M):

        // [Ax^2  Ax  1 ] [a]   [Az]
        // [Bx^2  Bx  1 ] [b] = [Bz]
        // [Cx^2  Cx  1 ] [c]   [Cz]

        // A^2
        Axpow2 = pow(Ax, 2);
        
        // B^2
        Bxpow2 = pow(Bx, 2);
        
        // C^2
        Cxpow2 = pow(Cx, 2);

        //----------------------------------------------------------------------------------------------------------------
        // first portion of the algorithm is solving for a, b, and c

        // det(M)
        detM = (Axpow2 * (Bx - Cx)) - (Ax * (Bxpow2 - Cxpow2)) + ((Bxpow2 * Cx) - (Bx * Cxpow2));
        
        // det(Ma)
        detMa = (Az * (Bx - Cx)) - (Ax * (Bz - Cz)) + ((Bz * Cx) - (Bx * Cz));
        
        // det(Mb)
        detMb = (Axpow2 * (Bz - Cz)) - (Az * (Bxpow2 - Cxpow2)) + ((Bxpow2 * Cz) - (Bz * Cxpow2));
        
        // det(Mc)
        detMc = (Axpow2 * ((Bx * Cz) - (Bx * Cx))) - (Ax * ((Bxpow2 * Cz) - (Bz * Cxpow2))) + (Az * ((Bxpow2 * Cx) - (Bx * Cxpow2)));

        // Solve for a, b and C
        a = detMa/detM;
        b = detMb/detM;
        c = detMc/detM;

        //----------------------------------------------------------------------------------------------------------------
        // finding first and second derivative equivalents to find curvature value

        first_deriv = 2 * a * Bx + b;
        second_deriv = 2 * a;
        curve = (4 * ((std::abs(second_deriv))/(pow((1 + pow(first_deriv, 2)), 1.5))));

        //----------------------------------------------------------------------------------------------------------------
        // sign of curvature determined by comparing the average of extreme heights with the central height

        if (((Cz + Az) / 2) < Bz){ // curve is negative
            return -1 * curve;
        }

        else if (((Cz + Az) / 2) == Bz){ // there is no curve 
            return 0;
        }

        return curve; // curve is positive
    }

// 1's correspond to first coordinate pair, 2's belong to second coordinate pair, 3's belong to third coordinate pair-----
// this function follows difference of slopes method for determining curvature--------------------------------------------
    double Formula::diffOfSlopes (point *point1, point *point2, point *point3){
        double x1 = point1->x, z1 = point1->z, x2 = point2->x, z2 = point2->z, x3 = point3->x, z3 = point3->z, ABX, ABZ, BCX, BCZ, SlopeAB, SlopeBC;
        
        ABX = x1-x2;
        ABZ = z1-z2;
        BCX = x2-x3;
        BCZ = z2-z3;

        //----------------------------------------------------------------------------------------------------------------
        // checking if there is a calculatable slope between points 1 and 2

        if(ABX == 0){ // if x position is the same, slope is undefined
            std::cout << "Slope = undifiend" << std::endl;
        }
        else{ // otherwise compute slope
            SlopeAB = (ABZ/ABX);
        }

        //----------------------------------------------------------------------------------------------------------------
        // checking if there is a calculatable slope between points 2 and 3
        
        if(BCX == 0){ // if x position is the same, slope is undefined
            std::cout << "Slope = undifiend" << std::endl;
        }
        else{
            SlopeBC = (BCZ/BCX);
        }

        //----------------------------------------------------------------------------------------------------------------
        // comparing slopes, if slopes are identical, no curvature to calculate in the first place

        if(SlopeAB == SlopeBC){ // straight line
            return 0;
        }
        return (SlopeAB - SlopeBC)/(x3-x1);
    }

// 1's correspond to first coordinate pair, 2's belong to second coordinate pair, 3's belong to third coordinate pair-----
// this function follows the 3-ordinate Lagrangian method in order to determine curvature---------------------------------
    double Formula::lagrangian (point *point1, point *point2, point *point3){
        double x1 = point1->x, z1 = point1->z, x2 = point2->x, z2 = point2->z, x3 = point3->x, z3 = point3->z; 
        // Proper data hould never divide by 0
        return  ((2 * (z1))-(z2)-(z3))/pow((((x3) - (x1))/2), 2);
    }

// 1's correspond to first coordinate pair, 2's belong to second coordinate pair, 3's belong to third coordinate pair-----
// this function follows the Finite Difference Analysis method in order to determine curvature----------------------------
    double Formula::finiteDiffAnalysis (point *point1, point *point2, point *point3){
        double x1 = point1->x, z1 = point1->z, x2 = point2->x, z2 = point2->z, x3 = point3->x, z3 = point3->z, 
               zPrime, zDoublePrime;
        // Proper data hould never divide by 0

        //----------------------------------------------------------------------------------------------------------------

        zPrime = (z3-z1)/(x3-x1);

        //----------------------------------------------------------------------------------------------------------------

        zDoublePrime = (((z3-z2)/(x3-x2))-((z2-z1)/(x2-x1)))/((x3-x2)*(x2-x1));
    
        return  zDoublePrime/(pow((1 + pow(zPrime, 2)), 1.5));
    }

// 1's correspond to first coordinate pair, 2's belong to second coordinate pair, 3's belong to third coordinate pair-----
// this function follows will run a formula to determine if the overall angle between points is acute or not -------------
    bool Formula::isAcute (point *point1, point *point2, point *point3){
        double x1 = point1->x, z1 = point1->z, x2 = point2->x, z2 = point2->z, x3 = point3->x, z3 = point3->z,
               slope1, slope2, angle;

        //----------------------------------------------------------------------------------------------------------------
        // calculating both slopes through this formula: (y2 - y1) / (x2 - x1)

        slope1 = (z2 - z1)/(x2 - x1);
        slope2 = (z3 - z2)/(x3 - x2);
        
        //----------------------------------------------------------------------------------------------------------------
        // Calculate the angle, multiplied by 180/PI to translate to degrees

        angle = (std::atan(std::abs((slope2 - slope1) / (1 + (slope1 * slope2))))) * (180/PI);;

        return (angle < 90.00);
    }


    


// for testing functions, software not dependent on this function
// int main() {
//     double curve;
//     string output;
//     Formula method;
//     curve = method.diffOfSlopes(point1, point2, point3);
//     cout << curve << endl;
//     return 0;
// }