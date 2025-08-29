#include "dataContainer.h"


#include <iostream> // for testing purposes only

// CurvatureScale functions ---------------------------------------------------------------------------------------------------

CurvatureScale::CurvatureScale(double *curvatureArray, int dataLength, double scale, point *pointArray) {
    CurvatureScale::curvatureArray = new double[dataLength];
    memcpy(CurvatureScale::curvatureArray, curvatureArray, dataLength * sizeof(double));
    CurvatureScale::scale = scale;
    CurvatureScale::pointArray = pointArray;
    CurvatureScale::dataLength = dataLength;
}

// Getters

double CurvatureScale::getCurvature(int index) {
    return curvatureArray[index];    
}

double CurvatureScale::getScale() {
    return scale;
}

int CurvatureScale::getLength() {
    return dataLength;
}

point CurvatureScale::getPoint(int index) {
    return pointArray[index];
}

//These silly functions just initiate the arrays to be overwritten later
CurvatureScale::CurvatureScale() {
    curvatureArray = new double[10];
}

//void CurvatureScale::setPercentErrorArray(double* PercentErrorArray, int dataLength) {
//    curvatureArray = new double[dataLength];
//}

//void CurvatureScale::setPercentErrorArray(int dataLength) {
    //curvatureArray = new double[dataLength];
//}

// Setters

//void CurvatureScale::setCurvatureArray(double* curvatureArray, int dataLength) {
//    delete[] CurvatureScale::curvatureArray;
//    CurvatureScale::curvatureArray = new double[dataLength];
//    memcpy(CurvatureScale::curvatureArray, curvatureArray, dataLength * sizeof(double));
//} //FLAG: Commented bcs we think its unneccessary

void CurvatureScale::setCurvatureArray(int dataLength) {
    delete[] CurvatureScale::curvatureArray;
    CurvatureScale::curvatureArray = new double[dataLength];
    CurvatureScale::dataLength = dataLength;
}

void CurvatureScale::setCurvature(double curvature, int index) {
    // std::cout<<"setting curvature" << std::endl; for debugging
    // std::cout<<"array length: " << dataLength << std::endl;
    // std::cout<<"index: " << index << std::endl;
    this->curvatureArray[index] = curvature;
}

//void  CurvatureScale::setPercentErrorArray(double* PercentErrorArray, int dataLength){
//    delete[] CurvatureScale::percentErrorArray;
//    CurvatureScale::percentErrorArray = new double[dataLength];
//    memcpy(CurvatureScale::percentErrorArray, percentErrorArray, dataLength * sizeof(double));
//
//} //FLAG: Commented bcs we think its unneccessary

void  CurvatureScale::setPercentErrorArray(int dataLength){
    delete[] CurvatureScale::percentErrorArray;
    CurvatureScale::percentErrorArray = new double[dataLength];
    CurvatureScale::dataLength = dataLength;
}

void  CurvatureScale::setPercentError(double curvature, int index){
    this->percentErrorArray[index] = curvature;

}


void CurvatureScale::setScale(int scale) {
    CurvatureScale::scale = scale;
}

// DataContainer functions ---------------------------------------------------------------------------------------------------


DataContainer::DataContainer(point* pointArray, int dataLength) : pointArray(nullptr) {
    setPointArray(pointArray, dataLength);
}

// Destructor deletes the arrays and pointers so memory is not leaked
DataContainer::~DataContainer() {
    delete[] curvatureScaleArray;
}

// getters
CurvatureScale* DataContainer::getIndex(int index) {
    return &(this->curvatureScaleArray[index]);
}

// CurvatureScale* DataContainer::getScale(double scale){

// }

point DataContainer::getPoint(int index) {
    return pointArray[index];
}

point* DataContainer::getPointAddress(int index) {
    return &pointArray[index];
}

int DataContainer::getPointArrayLength() {
    return pointArrayLength;
}

int DataContainer::getCurvatureArrayLength() {
    return curvatureArrayLength;
}
int64_t DataContainer::getNumOps() {
    return numOps;
}

double DataContainer::getMinLength() {
    return DataContainer::minLength;
}

double DataContainer::getMaxLength() {
    return (DataContainer::minLength * DataContainer::maxHalfIntervalPossible);
}

double DataContainer::getmaxHalfIntervalPossible() {
    return maxHalfIntervalPossible;
} 

// setters
void DataContainer::setIndex(int index, CurvatureScale* data) {
    curvatureScaleArray[index] = *data;
}
void DataContainer::setPoint(int index, point point) {
    pointArray[index] = point;
}
void DataContainer::putCurvature(int scale, int index, double curvature) {
    this->curvatureScaleArray[scale].setCurvature(curvature, index); // puts the data into the array for a particular scale
    // std::cout<<this->curvatureScaleArray[scale].getCurvature(index)<<std::endl; //check if data is actually being put correctly
    // std::cout<<this->curvatureScaleArray[scale].getLength()<<std::endl;
}

void DataContainer::putPE(int scale, int index, double percentError) {
    this->curvatureScaleArray[scale].setCurvature(percentError, index); // puts the data into the array for a particular scale
    // std::cout<<this->curvatureScaleArray[scale].getCurvature(index)<<std::endl; //check if data is actually being put correctly
    // std::cout<<this->curvatureScaleArray[scale].getLength()<<std::endl;
}

void DataContainer::setCurvatureScaleArray(int dataLength) {
    delete[] DataContainer::curvatureScaleArray;
    DataContainer::curvatureScaleArray = new CurvatureScale[dataLength];
    DataContainer::curvatureArrayLength = dataLength;
}

void DataContainer::setPointArray(point *pointArray, int dataLength) {
    delete[] DataContainer::pointArray;
    DataContainer::pointArray= new point[dataLength];
    memcpy(DataContainer::pointArray, pointArray,   dataLength * sizeof(point));
    DataContainer::pointArrayLength = dataLength;
}

void DataContainer::setPointArray(int dataLength) {
    std::cout<<"setting point array with length " << dataLength << std::endl;
    if(this->pointArray){
        std::cout<<"array already exists, clearing"<<std::endl;
        if (this->pointArray) {
            delete[] this->pointArray;
            this->pointArray = nullptr;
        }
    }
    std::cout<<"make new array"<<std::endl;
    this->pointArray= new point[dataLength];
    this->pointArrayLength = dataLength;
}

void DataContainer::setmaxhalfinterval(){
    //we find the minimum length by averaging the length across the entire data, thatis, the smallest distance between two points
   this->minLength = fabs(((DataContainer::pointArray[pointArrayLength-1].x)-(DataContainer::pointArray[0].x)) / (DataContainer::pointArrayLength - 1));
    
    //FOR DEBUGGING
    // std::cout<< DataContainer::pointArray[pointArrayLength-1].x << std::endl;
    // std::cout<< DataContainer::pointArray[0].x << std::endl;

    // std::cout << ((DataContainer::pointArray[pointArrayLength-1].x)-(DataContainer::pointArray[0].x)) << std::endl;
    // std::cout <<9.9 / 99 << std::endl;
    // std::cout <<9.9/99.<< std::endl;
    // std::cout<< DataContainer::pointArrayLength - 1 << std::endl;
    // std::cout<< minLength << std::endl;


    //we calculate the maximum length possible. First, we check to see if the data has an even or odd number of points
    //an even number of points results in an odd number of intervals. the number of intervals is always one less than the number of points
    //an odd number of points results in an even number of intervals.
    //we want to find the maximum interval possible that fits in twice within the data.
    //the following formulas calculate the maximum interval possible given the data.
    if(DataContainer::pointArrayLength % 2 == 0){
        //data is even length
        //odd number of intervals
        //example: 4 points. this means there are 3 intervals, and the maximum half interval possible is 1.
        DataContainer::maxHalfIntervalPossible = (DataContainer::pointArrayLength / 2) - 1;
        this->odd = false;
        std::cout<<"even"<<std::endl;
    }
    else{
        //data is odd length
        //even number of intervals
        //example: 5 points. this means there are 4 intervals, and the maximum half interval possible is 2.
        DataContainer::maxHalfIntervalPossible = (DataContainer::pointArrayLength - 1) / 2;
        this->odd = true;
        
    }
    //finally, for the user, we multiply the minimum length by the maximum half interval possible to get the maximum length possible.
    //this value is shown later to the user as they select their bounds, as it represents the upper limit of what is possible to enter into the bounds.
    DataContainer::maxLength = DataContainer::minLength * DataContainer::maxHalfIntervalPossible;
}

// this function takes in the maximum measurement parameters from the function defined above, as well as the user's preferred measurement parameters in order
// to determine how many curvatures will be calculated (Number of Operations: numops)
void DataContainer::setNumOps(const int& minScale, const int& maxScale){
    int64_t retval;
    //formula is different for calculating the number of operations if the data is odd or even.
    int minops = (DataContainer::pointArrayLength - 2*minScale);
    std::cout<<"minops"<<minops<<std::endl;
    int maxops = (DataContainer::pointArrayLength - 2*maxScale);
    std::cout<<"maxops"<<maxops<<std::endl;
    retval = (((minops - maxops)/2+1)*(minops + maxops))/2;
    std::cout<<"minscale"<<minScale<<std::endl;
    std::cout<<"maxscale"<<maxScale<<std::endl;


    //retval is the total number of curvatures to be made. 
    //the total number of operations to be performed = indexes in the array.
    
    //check if too many curvatures for 32-bit mode
    if(retval > std::numeric_limits<int>::max()){
        std::cerr << "Error: Too many curvatures to calculate.\nPlease reduce number of curvatures, or relaunch in 64-bit mode." << std::endl;
        return;
    }

    try {
        std::cout << "Allocating memory for " << retval << " CurvatureScales" << std::endl;
        // Check if retval exceeds std::numeric_limits<int>::max()
        if (retval > std::numeric_limits<int>::max()) {
            throw std::bad_alloc();
        }

        // Allocate memory for the array of CurvatureScales
        DataContainer::curvatureScaleArray = new CurvatureScale[maxScale - minScale + 1];

        // Dynamically allocate memory for each CurvatureScale's curvatureArray
        for (int i = minScale; i <= maxScale; ++i) {
            int length = DataContainer::pointArrayLength - 2 * i;
            if (length <= 0) {
                throw std::invalid_argument("Invalid length for curvatureArray");
            }
            std::cout << "Setting length of array " << i << " to " << length << std::endl;
            DataContainer::curvatureScaleArray[i - minScale].setCurvatureArray(length);
            DataContainer::curvatureScaleArray[i - minScale].setScale(i);
        }

        DataContainer::curvatureArrayLength = maxScale - minScale + 1;
        DataContainer::numOps = retval;
    } catch (const std::bad_alloc& e) {
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    }
}

//  Statistics functions --------------------------------------------------------------------------------------------------------------

void DataContainer::setAbsMin(double value) { min = value; }
void DataContainer::setAbsMax(double value) { max = value; }
void DataContainer::setAvgPos(double value) { avgPos = value; }
void DataContainer::setPosAvgDenominator (int value) { posAvgDenominator = value; }
void DataContainer::setAvgNeg(double value) { avgNeg = value; }
void DataContainer::setNegAvgDenominator (int value) { negAvgDenominator = value; }
void DataContainer::updateFiveExtremes(double curvature, double pos) {
    // This function updates the five extremes based on the curvature and position
    // For simplicity, we assume fiveExtremes is an array of pointers to points
    // This is a placeholder implementation; actual logic will depend on requirements
    if (fiveExtremes[0] == nullptr || abs(curvature) < abs(fiveExtremes[0]->z)) {
        fiveExtremes[0] = new point{curvature, pos};
    }
    // Additional logic to update other extremes would go here

    for (int i = 0; i < 4; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < 5; ++j) {
            if (abs(fiveExtremes[j]->z) < abs(fiveExtremes[i]->z))
                minIndex = j;
        }
        std::swap(fiveExtremes[i], fiveExtremes[minIndex]);
    }

}

void sortArrayAscending(double arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < size; ++j) {
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }
        std::swap(arr[i], arr[minIndex]);
    }
}

double DataContainer::getAbsMin() const  {return min; }
double DataContainer::getAbsMax() const  { return max; }
double DataContainer::getAvgPos() const { return avgPos; }
double DataContainer::getPosAvgDenominator() const { return posAvgDenominator; }
double DataContainer::getAvgNeg() const { return avgNeg; }
double DataContainer::getNegAvgDenominator() const { return negAvgDenominator; }
point** DataContainer::getFiveExtremes() { return fiveExtremes; }
