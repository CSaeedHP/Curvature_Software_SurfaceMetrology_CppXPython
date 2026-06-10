#include "userData.h"
#include "dataContainer.h"
#include "userInputCLI.h"
#include "fileHandler.h"
#include <string>
using namespace std;

    //setters

    bool UserData::setDataContainer(DataContainer* dataContainer){
        // Assuming dataContainer is a DataContainer object
        // You might need to implement a mapping from string to DataContainer
        this->dataContainer = dataContainer;
        return true;
    }
    int UserData::setScaleBounds(double min, double max){
        std::cout << "setScaleBounds" << std::endl;
        //returns 0 if valid, 1 if minscale is invalid, 2 if maxscale is invalid, 3 if both are invalid
        std::cout<< min << std::endl;
        std::cout<<ceil(min / this->dataContainer->getMinLength())<<std::endl;
        
        int minint = ceil(min / this->dataContainer->getMinLength());
        int maxint = floor(max / this->dataContainer->getMinLength());
        if (min < this->dataContainer->getMinLength()) {
            minint = 1;
        }
        if (max > this->dataContainer->getMaxLength()) {
            max = this->dataContainer->getmaxHalfIntervalPossible();
        }
        bool minValid = true;
        bool maxValid = true;

        
        std::cout << "minint: " << minint << std::endl;
        std::cout << "maxint: " << maxint << std::endl;

        std::cout <<"check minint" << std::endl;
        if(minint < 1){
            minValid = false;
        }
        std::cout <<"check maxint" << std::endl;
        if(maxint > this->dataContainer->getmaxHalfIntervalPossible()){
            maxValid = false;
        }
        std::cout <<"now return" << std::endl;
        if(minValid && maxValid){
            std::cout <<"success" << std::endl;
            this->userMinScale = minint;
            this->userMaxScale = maxint;

            return 0;
        }
        else if(!minValid && !maxValid){
            //cerr << "Both min and max scale are invalid" << endl;
            return 3;
        }
        else if(!minValid){
            //cerr << "Min scale is invalid" << endl;
            return 1;
        }
        else{
            //cerr << "Max scale is invalid" << endl;
            return 2;
        }
    }
    bool UserData::setAnalyisType(int method){
        // Assuming analysisType is an integer representation of the method
        // You might need to implement a mapping from string to int
        analysisType = method;
        return true;
    }
    int UserData::setIsHybrid(bool isItHybrid){
        hybrid= isItHybrid;
        return 0;
    }
    bool UserData::setHybridSelection(int method1, int method2){
        // Assuming hybridSelection is an integer representation of the methods
        // You might need to implement a mapping from string to int
        hybridSelection[0] = method1;
        hybridSelection[1] = method2;
        return true;
    }
    bool UserData::setInputFilePath(string path){
        //returns true if file is valid        
        inputFilepath = path;
        return true;
    }

    //getters
    string UserData::getInputFilePath(){
        return inputFilepath;
    }
    DataContainer* UserData::getDataContainer(){
        return dataContainer;
    }
    int UserData::getMinScale(){
        return userMinScale;
    }
    int UserData::getMaxScale(){
        return userMaxScale;
    }
    int UserData::getAnalysisType(){
        return analysisType;
    }
    bool UserData::getHybrid(){
        return hybrid;
    }
    int UserData::getHybridSelection(int index){
        return hybridSelection[index];
    }
    bool UserData::getLogScale(){
        return logScale;
    }
    void UserData::setLogScale(bool logScale){
        UserData::logScale = logScale;
    }