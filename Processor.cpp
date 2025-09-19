#include "Processor.h"

void Processor::Processor(){
UserData uData;
DataContainer data;
uData.setDataContainer(&data);
};
void Processor::loadData(string inputfile, double minscale, double maxscale, bool hybrid, int acutemethod, int obtusemethod){
uData.setInputFilePath(inputfile);
uData.setScaleBounds(minscale, maxscale);
FileHandler::fileRead(uData.getInputFilePath(), &data);
data.setmaxhalfinterval();
uData.setScaleBounds(minscale, maxscale);
data.setNumOps(uData.getMinScale(), uData.getMaxScale());
uData.setIsHybrid(analysisType);
uData.setHybridSelection(obtuseMethod, acuteMethod);
};

void Processor::writeData();

py::array_t<double> fetchData();

