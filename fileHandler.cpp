#include "dataContainer.h"
#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <filesystem>
#include <vector>
#include "fileHandler.h"
#include "userData.h"

using namespace std;

FileHandler::FileHandler() {}

// Function is meant to read a CSV file and return an array of points
char FileHandler::fileRead(string input, DataContainer* data) {
    std::cout<<"reading file"<<std::endl;
    string filePath = remove_quotes(input); // Remove quotes from the input string

    // Check if the file exists
    if (!validPath(filePath)) {
        std::cerr << "Error: File does not exist!" << std::endl;
        return 0;
    }

    // Check if the file extension is ".csv"
    // PathExtension function is used to make the file type case insensitive
    if (pathExtension(filePath) != ".csv" && pathExtension(filePath) != ".txt" && pathExtension(filePath) != ".x3p") {
        std::cerr << "Error: Invalid file type! Expected a .csv file." << std::endl;
        std::cerr << pathExtension(filePath) << std::endl;
        return 0;
    }

    std::ifstream file(filePath); // Open file
    if (!file.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 0;
    }
    else{
        // First loop: Count the number of lines
        std::string line;
        int ArraySize = 0;
        while (std::getline(file, line)) {
            ArraySize++;
        }

        // Reset file pointer
        file.clear();               
        file.seekg(0, ios::beg);    

        // Allocate point array
        std::cout<<"set point array"<<std::endl;
        data->setPointArray(ArraySize);
        std::cout<<"set successful"<<std::endl;
        // Second loop: Read data into array
        int ite = 0;
        
        // Read each line from the file until EOF (end of file) is reached
        while (std::getline(file, line)) {  
            // Create a stringstream object from the line to parse values separately
            std::stringstream ss(line);  
            std::string x_str, z_str;  // Strings to store the extracted x and z values

            // Extract values separated by a comma
            // - Reads the first value (x) into x_str
            // - Reads the second value (z) into z_str
            if (std::getline(ss, x_str, ',') && std::getline(ss, z_str, ',')) {  
                // Convert extracted string values to double and store in pointArray
                data->setPoint(ite, {std::stod(x_str), std::stod(z_str)});
                
                // Increment index to store the next point in the array
                ite++;  
            }
        }

        file.close(); 


        // //Print the points read from the file and file type, use for TESTING
        // std::cout << "File Type: " << pathExtension(filePath) << std::endl;
        // ite = 0;
        // while(ite < ArraySize){
        //     std::cout << "Point " << ite << ": " << pointArray[ite].x << ", " << pointArray[ite].z << std::endl;
        //     ite++;
        // }

        std::cout << "Data was read successfully.\n";
        return 1;
    }
}

// Function is meant to write data to a CSV file
int FileHandler::fileWrite(UserData* uData, string fileName) {
    DataContainer* XSC = uData->getDataContainer();
    if (XSC == nullptr) {
        std::cerr << "Error: DataContainer is null." << std::endl;
        return 1;
    }

    int BroadArraySize = XSC->getCurvatureArrayLength();
    if (BroadArraySize <= 0) {
        std::cerr << "Error: Invalid BroadArraySize." << std::endl;
        return 1;
    }

    fileName += ".csv";

    std::ofstream myFile(fileName, std::ios::out | std::ios::trunc);
    if (!myFile.is_open()) {
        std::cerr << "Unable to open file." << std::endl;
        return 1;
    }

    // Use a stringstream as a buffer
    std::ostringstream buffer;
    buffer << "X-Position,Scale,Curvature\n";

    int ScaleSwitching = 0;
    while (ScaleSwitching < BroadArraySize) {
        int CurvatureArraySize = XSC->getIndex(ScaleSwitching)->getLength();
        if (CurvatureArraySize <= 0) {
            std::cerr << "Error: Invalid CurvatureArraySize at index " << ScaleSwitching << "." << std::endl;
            return 1;
        }

        int CurvatureSwitching = 0;
        while (CurvatureSwitching < CurvatureArraySize) {
            buffer << XSC->getPointAddress(CurvatureSwitching + ScaleSwitching + uData->getMinScale())->x << ","
                   << XSC->getIndex(ScaleSwitching)->getScale() * XSC->getMinLength() << ","
                   << XSC->getIndex(ScaleSwitching)->getCurvature(CurvatureSwitching) << "\n";

            CurvatureSwitching++;
        }
        ScaleSwitching++;
    }

    // Write the entire buffer to the file at once
    myFile << buffer.str();
    myFile.close();

    std::cout << "Data written to file successfully." << std::endl;
    return 0;
}

//File checking:
// Function to check if a file exists
bool FileHandler::validPath(const std::string& path) {
    return std::filesystem::exists(path);
}

// Function to get file extension
std::string FileHandler::pathExtension(const std::string& path) { 
    if (path.size() < 3) { 
        return std::filesystem::path(path).extension().string();; 
    }

    //std::cout << path << std::endl; // for testing

    string result = path.substr(0, path.size() - 3); 

    result += tolower(path[path.size() - 3]); 
    result += tolower(path[path.size() - 2]); 
    result += tolower(path[path.size() - 1]); 

    //std::cout << result << std::endl; // for testing

    return std::filesystem::path(result).extension().string(); 
}

// Function to read a CSV file and return a vector of doubles
// std::vector<double> readCSV(std::string path){
//     std::ifstream file(path);
//     std::string line;
//     std::vector<double> data;

//     while(std::getline(file, line) ){
//         std::stringstream ss(line);
//         std::string value;
//         while( std::getline(ss, value, ',') ){
//             data.push_back(std::stod(value));
//         }
//     }
// }

// Function to remove quotes from a string
string FileHandler::remove_quotes(const string& input) {
    string result = input;
  
    if (result.size() >= 2 && result[0] == '"' && result[result.size() - 1] == '"') {
        result = result.substr(1, result.size() - 2); 
    }
  
    return result;
}      

//for testing purposes
// int main() {
//     FileHandler fh;
//     fh.fileRead();
//     return 0;
// }