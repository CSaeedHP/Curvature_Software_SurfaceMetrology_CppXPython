#ifndef FORMULA_H
#define FORMULA_H
#include <unordered_map>
#include <functional>

typedef double (*functionPointer)(point*, point*, point*);
class Formula{
    /* Formulas used to calculate the curvature across three different points */

    // double herons (double x1, double z1, double x2, double z2, double x3, double z3);
    // double parabola (double x1, double z1, double x2, double z2, double x3, double z3);
    // double diffOfSlopes (double x1, double z1, double x2, double z2, double x3, double z3);
    // double lagrangian (double x1, double z1, double x2, double z2, double x3, double z3);
    // double finiteDiffAnalysis (double x1, double z1, double x2, double z2, double x3, double z3);
    // bool isAcute (double x1, double z1, double x2, double z2, double x3, double z3);
    public:
        static double herons (point *point1, point *point2, point *point3);
        static double parabola (point *point1, point *point2, point *point3);
        static double diffOfSlopes (point *point1, point *point2, point *point3);
        static double lagrangian (point *point1, point *point2, point *point3);
        static double finiteDiffAnalysis (point *point1, point *point2, point *point3);
        static bool isAcute (point *point1, point *point2, point *point3);
        static std::unordered_map<int, functionPointer> funcMap();

};

#endif

