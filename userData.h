#ifndef USERDATA_H
#define USERDATA_H
#include <cmath>
#include <string>
#include "dataContainer.h"
using namespace std;
class UserData{
    public:
        //setters
        bool setDataContainer(DataContainer* dataContainer);
        int setScaleBounds(double min, double max);
        bool setAnalyisType(int method);
        bool setHybridSelection(int obtusemethod, int acutemethod);
        bool setInputFilePath(string path);
        int setIsHybrid(bool isItHybrid);


        //getters
        DataContainer* getDataContainer();
        int getMinScale();
        int getMaxScale();
        int getAnalysisType();
        bool getHybrid();
        int getHybridSelection(int index);
        bool getLogScale();
        void setLogScale(bool logScale);
        string getInputFilePath();
        
    private:
        //filepath
        string inputFilepath;

        //scale data
        int userMinScale;
        int userMaxScale;
    
        DataContainer* dataContainer;

        int analysisType;
        bool hybrid;
        int hybridSelection[2];
        bool logScale;
};
#endif


