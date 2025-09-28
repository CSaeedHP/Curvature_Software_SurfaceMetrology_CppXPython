#include "Processor.h"
namespace py = pybind11;
using namespace std;
Processor::Processor(){
uData.setDataContainer(&data);
};
void Processor::loadData(string inputfile, double minscale, double maxscale, bool hybrid, int acuteMethod, int obtuseMethod){
    std::cout << "setting inputfilepath"<< std::endl;
    uData.setInputFilePath(inputfile);
    // std::cout << "setting minscale, maxscale" << std::endl;
    // uData.setScaleBounds(minscale, maxscale);
    std::cout << "Reading file" << std ::endl;
    FileHandler::fileRead(uData.getInputFilePath(), &data);
    std::cout << "setting bounds" <<std ::endl;
    data.setmaxhalfinterval();
    std::cout << "setting min and max scale" << std::endl;
    uData.setScaleBounds(minscale, maxscale);
    std::cout << "preparing number of operations" << std::endl;
    data.setNumOps(uData.getMinScale(), uData.getMaxScale());
    std::cout << "setting hybrid status" <<std::endl;
    uData.setIsHybrid(hybrid);
    std::cout << "setting methods" <<std::endl;
    uData.setAnalyisType(obtuseMethod);
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
    std::cout << "Processing Finsihed" << std ::endl;
};
void Processor::writeData(string filePath){
    FileHandler::fileWrite(&uData, filePath);
};
py::array_t<double> Processor::fetchData(){
    return FileHandler::exportData(&uData);
};


Processor::~Processor() {

}
