#include <iostream>
#include <thread>
#include <vector>
#include <mutex>



const int pointArrayLength = 100;

double* generateArray(int length) {
    double* array = new double[length];
    for (int i = 0; i < length; ++i) {
        array[i] = i + 1;
    }
    return array;
}




// typedef struct{
//     double x;
//     double z;
// }point;

// point* pointArray = new point[pointArrayLength];

// double minLength;
// int maxHalfIntervalPossible;
// bool odd;
// double maxLength;
// void setmaxhalfinterval(){
//     //we find the minimum length by averaging the length across the entire data, thatis, the smallest distance between two points
//     minLength = abs((pointArray[pointArrayLength].x)-(pointArray[0].x) / (pointArrayLength - 1));
//     //we calculate the maximum length possible. First, we check to see if the data has an even or odd number of points
//     //an even number of points results in an odd number of intervals. the number of intervals is always one less than the number of points
//     //an odd number of points results in an even number of intervals.
//     //we want to find the maximum interval possible that fits in twice within the data.
//     //the following formulas calculate the maximum interval possible given the data.
//     if(pointArrayLength % 2 == 0){
//         //data is even length
//         //odd number of intervals
//         //example: 4 points. this means there are 3 intervals, and the maximum half interval possible is 1.
//         maxHalfIntervalPossible = (pointArrayLength / 2) - 1;
//         odd = false;
//     }
//     else{
//         //data is odd length
//         //even number of intervals
//         //example: 5 points. this means there are 4 intervals, and the maximum half interval possible is 2.
//         maxHalfIntervalPossible = (pointArrayLength - 1) / 2;
//         odd = true;
//     }
//     //finally, for the user, we multiply the minimum length by the maximum half interval possible to get the maximum length possible.
//     //this value is shown later to the user as they select their bounds, as it represents the upper limit of what is possible to enter into the bounds.
//     maxLength = minLength * maxHalfIntervalPossible;
// }

// void numOps(const minScale, const maxScale){
//     int64_t retval;
//     //formula is different for calculating the number of operations if the data is odd or even.
//     int minops = (maxHalfIntervalPossible) - minScale + 1;
//     int maxops = (maxHalfIntervalPossible) - maxScale;
//     retval = minops * minops - maxops * maxops;
//     if (odd){
//         //the only part that is different depending on if the data is odd or even.
//         retval += minops - maxops;
//     }
//     //the total number of operations to be performed = indexes in the array.
    
// }


int getMaxHalfInt(int arraylen){
    if(arraylen % 2 == 0){
        return (arraylen / 2) - 1;
    }
    else{
        return (arraylen - 1) / 2;
    }
}

int numOps(int minScale, int maxScale, int maxHalfIntervalPossible){
    int64_t retval;
    int minops = (maxHalfIntervalPossible) - minScale + 1;
    int maxops = (maxHalfIntervalPossible) - maxScale;
    retval = minops * minops - maxops * maxops;
    if (maxHalfIntervalPossible % 2 == 0){
        retval += minops - maxops;
    }
    return retval;
}

double* newEmptyArray(int length) {
    double* array = new double[length];
    return array;
}

int getNumThreads() {
    return std::thread::hardware_concurrency();
}





int main() {
    double* array = generateArray(pointArrayLength);
    for (int i = 0; i < pointArrayLength; ++i) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
    delete[] array;
    return 0;
}
