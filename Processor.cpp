#include "Processor.h"
namespace py = pybind11;

Processor::Processor(){
UserData uData;
DataContainer data;
uData.setDataContainer(&data);
};
void Processor::loadData(string inputfile, double minscale, double maxscale, bool hybrid, int acuteMethod, int obtuseMethod){
uData.setInputFilePath(inputfile);
uData.setScaleBounds(minscale, maxscale);
FileHandler::fileRead(uData.getInputFilePath(), &data);
data.setmaxhalfinterval();
uData.setScaleBounds(minscale, maxscale);
data.setNumOps(uData.getMinScale(), uData.getMaxScale());
uData.setIsHybrid(hybrid);
uData.setHybridSelection(obtuseMethod, acuteMethod);
};

void Processor::processData(){
    auto functionMapping = Formula::funcMap();
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
};
void Processor::writeData(string filePath){
    FileHandler::fileWrite(&uData, filePath);
};
py::array_t<double> Processor::fetchData(){
    return FileHandler::exportData(&uData);
};


Processor::~Processor() {

}
