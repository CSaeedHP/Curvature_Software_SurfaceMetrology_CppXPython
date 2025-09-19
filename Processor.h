#ifndef PROCESSOR_H
#define PROCESSOR_H
#endif
#include<stdio.h> 
#include<stdlib.h>
#include<iostream>

#include "dataContainer.h"
#include"userInputCLI.h"
#include<string>
#include<chrono>
using namespace std;

//testing single execution method
#include "fileHandler.h"
#include "userData.h"
#include "analysis.h"
#include "formula.h"
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
namespace py = pybind11;

class Processor{
    public:
    //Constructor
    Processor();
    UserData uData;
    DataContainer data;
    //Destructor
    ~Processor();


    //process data
    void loadData(string inputfile, double minscale, double maxscale, bool hybrid, int acutemethod, int obtusemethod);
    void processData();
    //write data
    void writeData(string filePath);

    //return data
    py::array_t<double> fetchData();


};
