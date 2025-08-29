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


int main() {
  if (sizeof(void*) == 8) {
    std::cout << "Running as a 64-bit application." << std::endl;
  } else if (sizeof(void*) == 4) {
      std::cout << "Running as a 32-bit application." << std::endl;
  } else {
      std::cout << "Unknown architecture." << std::endl;
  }
  
  std::cout << "This program was developed by Worcester Polytechnic Institute's Surface Metrology Lab.\nFor more information, please visit https://www.surfacemetrology.org/ and https://wp.wpi.edu/surfacemetrology/.\nThis software is distributed under the GPL-3.0 License.\n";

  //prog flow starts here. create uData and data objects
  UserData uData;
  DataContainer data;

  //THIS SHOULD BE CHANGED LATER BECAUSE THERE IS NO CHECK TO MAKE SURE DATA IS VALID
  std::cout<< "ref data container" << std::endl;
  uData.setDataContainer(&data);

  //get file path, store it into the uData.
  uData.setInputFilePath(cliInput::getString("Please enter the file path"));
  

  //read the file, store the data into the data object.
  FileHandler::fileRead(uData.getInputFilePath(), &data);

  //find the max half interval.
  data.setmaxhalfinterval();


  //print the minimum length and maximum length possible.
  std::cout << "The minimum length is: " << data.getMinLength() << std::endl;
  std::cout << "The maximum length possible is: " << data.getMaxLength() << std::endl;

  //get the minimum and maximum scales from the user.
  double minscale = cliInput::getDouble("Please enter the minimum scale");
  double maxscale = cliInput::getDouble("Please enter the maximum scale");

  //set the scales into the uData object.
  uData.setScaleBounds(minscale, maxscale);

  std::cout<< "bounds set successfully" << std::endl;

  //create the curvature array according to the minscale and maxscale.
  data.setNumOps(uData.getMinScale(), uData.getMaxScale());

  //print the number of operations to be performed.
  std::cout << "The number of operations to be performed is: " << data.getNumOps() << std::endl;

  //standard or hybrid analysis?
  bool analysisType = cliInput::getYesNo("Would you like to perform a hybrid analysis?");
  uData.setIsHybrid(analysisType);

  //if hybrid, which methods?
  if(analysisType){
    int obtuseMethod = cliInput::getInt("Please enter the method for obtuse angles");
    int acuteMethod = cliInput::getInt("Please enter the method for acute angles");
    uData.setHybridSelection(obtuseMethod, acuteMethod);
  }
  else{
    int method = cliInput::getInt("Please enter the method for standard analysis");
    uData.setAnalyisType(method);
  }

  //set variables for function pointers
  //create the map variable (use auto to make life easy)
  auto functionMapping = Formula::funcMap();

 
  //confirm user input to start analysis.
  bool confirm = cliInput::getYesNo("Would you like to start the analysis?");
  // record start time
  std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
  if (confirm){
    
  
    //start the analysis
    if(uData.getHybrid()){
      //if hybrid, declare *method2
      int methodKey1 = uData.getHybridSelection(0);
      int methodKey2 = uData.getHybridSelection(1);
      if (functionMapping.find(methodKey1) == functionMapping.end()) {
        std::cerr << "Error: Method " << methodKey1 << " not found in function mapping." << std::endl;  
      }
      if (functionMapping.find(methodKey2) == functionMapping.end()) {
        std::cerr << "Error: Method " << methodKey2 << " not found in function mapping." << std::endl;  
      }
      double (*method1)(point*,point*,point*) = functionMapping[methodKey1];
      double (*method2)(point*,point*,point*) = functionMapping[methodKey2];
      analysis::hybridAnalysis(&uData, &data, method1, method2, data.getPointArrayLength());
      
      
    }
    //case for standard analysis
    else{
      int methodKey1 = uData.getAnalysisType();
      if (functionMapping.find(methodKey1) == functionMapping.end()) {
        std::cerr << "Error: Method " << methodKey1 << " not found in function mapping." << std::endl;  
      }
      double (*method1)(point*,point*,point*) = functionMapping[methodKey1];
      analysis::singleAnalysis(&uData, &data, method1, data.getPointArrayLength());
    }
  }
  else{
    std::cout << "Analysis aborted" << std::endl;
  }
  // record end time, calculate difference
  std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
  std::cout << "Time taken to perform analysis: " << std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() << " seconds" << std::endl;

  //once analysis is finished, write the data to a file.
  string writePath = cliInput::getString("Please enter the file name to write the data to");
  std::cout<<"writing to file"<< writePath<< std::endl;

  //write to the file



  FileHandler::fileWrite(&uData, writePath);
  //analysis is complete. send a completion message.
  std::cout << "Analysis complete. Data written to file." << std::endl;

  
  

  // UserInput cli;
  // // point pointArray[] = {{0,0},{1,1},{2,0}};
  // // DataContainer data = DataContainer();
  // // data.setPointArray(pointArray, 3);
  // // CurvatureScale *curv = data.getIndex(0);
  // // curv->setScale(0.5);
  
}
 
