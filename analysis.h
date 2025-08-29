#ifndef ANALYSIS_H
#define ANALYSIS_H

#include "dataContainer.h"
#include "userInputCLI.h"
#include "userData.h"
#include <omp.h>


//extension of dataContainer class to include analysis functions
//make methods static.
class analysis{
    public:
        static void singleAnalysis(UserData* uData, DataContainer* data, double (*method)(point*,point*,point*), int numpoints);
        static void hybridAnalysis(UserData* uData, DataContainer* data, double (*method1)(point*,point*,point*), double (*method2)(point*,point*,point*), int numPoints);
        static void percentError(UserData* uData, DataContainer* data,int numPoints);
};

#endif
