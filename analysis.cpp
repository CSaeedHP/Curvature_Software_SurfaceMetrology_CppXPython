#include "analysis.h"
#include "formula.h"
#include "dataContainer.h"
#include "userData.h" // Add this line to include the definition of UserData
#include <iostream>
#include <unordered_map>
#include <string>
#include <functional>
#include <stdexcept>
#include <algorithm>

void analysis::singleAnalysis(UserData* uData, DataContainer* data, double (*method)(point*,point*,point*), int numPoints){
    //inputs: data, pointer to desired analysis method

    std::cout << "Single Analysis" << std::endl;
        
    //populate cuvatureScaleArray
    double curvature;
    int minScale = uData->getMinScale();
    int maxScale = uData->getMaxScale();

    // Parallelize the outer loop for better performance
    #pragma omp parallel for private(curvature) schedule(dynamic)
    for(int scale = minScale; scale <= maxScale; scale++){ //iterate over scales
        for(int point = scale; point < numPoints - scale; point++){ //iterate over points
            // point is the center point 
            // Call the function on the points
            curvature = method( data->getPointAddress(point - scale), data->getPointAddress(point), data->getPointAddress(point + scale)); 
            // Store the result in the data container
            data->putCurvature(scale - minScale, point-scale, curvature); //add curvature to data

            if (curvature > 0){
                data->setAvgPos(((data->getAvgPos() * data->getPosAvgDenominator()) + curvature) / (data->getPosAvgDenominator() + 1));
                data->setPosAvgDenominator(data->getPosAvgDenominator() + 1);
            }

            else if (curvature < 0){
                data->setAvgPos(((data->getAvgNeg() * data->getNegAvgDenominator()) + curvature) / (data->getNegAvgDenominator() + 1));
                data->setNegAvgDenominator(data->getNegAvgDenominator() + 1);
            }

            data->updateFiveExtremes(curvature, data->getPointAddress(point)->x); //update five extremes

            if (data->getAbsMin() == 0 || curvature < data->getAbsMin()) {
                data->setAbsMin(curvature); //update absolute minimum
            }

            if (data->getAbsMax() == 0 || curvature > data->getAbsMax()) {
                data->setAbsMax(curvature); //update absolute maximum
            }

        }

        // scale curvature average

    }
}

void analysis::hybridAnalysis(UserData* uData, DataContainer* data, double (*method1)(point*,point*,point*), double (*method2)(point*,point*,point*), int numPoints){

    std::cout << "Hybrid Analysis" << std::endl;
        
    //populate cuvatureScaleArray
    double curvature;
    int minScale = uData->getMinScale();
    int maxScale = uData->getMaxScale();
    
    //determine if points are acute
    #pragma omp parallel for private(curvature) schedule(dynamic)
    for(int scale = minScale; scale <= maxScale; scale++){ //iterate over scales
        for(int point = scale; point < numPoints - scale; point++){ //iterate over points
            // point is the center point 
            bool acute = Formula::isAcute(data->getPointAddress(point-scale), data->getPointAddress(point), data->getPointAddress(point+scale));
            

            // Call the function on the points(point *point1, point *point2, point *point3);
            if(acute){
                curvature = method1( data->getPointAddress(point - scale), data->getPointAddress(point), data->getPointAddress(point + scale)); 
            }
            else{
                curvature = method2( data->getPointAddress(point - scale), data->getPointAddress(point), data->getPointAddress(point + scale)); 
            }

            data->putCurvature(scale-minScale, point-scale, curvature); //add curvature to data

            if (curvature > 0){
                data->setAvgPos(((data->getAvgPos() * data->getPosAvgDenominator()) + curvature) / (data->getPosAvgDenominator() + 1));
                data->setPosAvgDenominator(data->getPosAvgDenominator() + 1);
            }

            else if (curvature < 0){
                data->setAvgPos(((data->getAvgNeg() * data->getNegAvgDenominator()) + curvature) / (data->getNegAvgDenominator() + 1));
                data->setNegAvgDenominator(data->getNegAvgDenominator() + 1);
            }

            data->updateFiveExtremes(curvature, data->getPointAddress(point)->x); //update five extremes

            if (data->getAbsMin() == 0 || curvature < data->getAbsMin()) {
                data->setAbsMin(curvature); //update absolute minimum
            }

            if (data->getAbsMax() == 0 || curvature > data->getAbsMax()) {
                data->setAbsMax(curvature); //update absolute maximum
            }
            
        }
    }
}


void analysis::percentError(UserData* uData, DataContainer* data,int numPoints){

    std::cout << "Percent Error" << std::endl;
        
    //populate cuvatureScaleArray
    double percentError;
    int minScale = uData->getMinScale();
    int maxScale = uData->getMaxScale();
    
    #pragma omp parallel for 

    for(int scale = minScale; scale <= maxScale; scale++){ //iterate over scales
        for(int point = scale; point < numPoints - scale; point++){ //iterate over points
            //determine percent Error:
            float percentError = 0;//FLAG: Change to formula

            data->putPE(scale-minScale, point-scale, percentError); //add curvature to data
        }
    }

    int BroadArraySize = data->getCurvatureArrayLength();
    int ScaleSwitching = 0;
    while (ScaleSwitching < BroadArraySize) {
        int CurvatureArraySize = data->getIndex(ScaleSwitching)->getLength();
        // if (CurvatureArraySize <= 0) {
        //     std::cerr << "Error: Invalid CurvatureArraySize at index " << ScaleSwitching << "." << std::endl;
        // }

        int CurvatureSwitching = 0;
        while (CurvatureSwitching < CurvatureArraySize) {
            // X position : data->getPointAddress(CurvatureSwitching + ScaleSwitching + uData->getMinScale())->x << ","
            //      Scale : data->getIndex(ScaleSwitching)->getScale() * data->getMinLength() << ","
            // Curvature  : data->getIndex(ScaleSwitching)->getCurvature(CurvatureSwitching) << "\n";

            CurvatureSwitching++;
        }
        ScaleSwitching++;
    }

}

