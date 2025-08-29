#include "userInputCLI.h"

using namespace std;


string cliInput::getString(string message){
    cout << message << "\n";
    string userInput;
    getline(cin, userInput);
    return userInput;
}

int cliInput::getInt(string message){
    cout << message << "\n";
    string userInput;
    getline(cin, userInput);
    int retVal;
    try {
        retVal = stoi(userInput);
    }
    catch (std::exception& e){
        std::cerr << "Integer Input Error " << e.what() << endl;
    }
    return retVal;
}

double cliInput::getDouble(string message){
    cout << message << "\n";
    string userInput;
    getline(cin, userInput);
    double retVal;
    try {
        retVal = stod(userInput);
    }
    catch (std::exception& e){
        std::cerr << "Double Input Error " << e.what() << endl;
    }
    return retVal;
}

bool cliInput::getYesNo(string message){
    cout << message << " (Yes/No)\n";
    string userInput;
    getline(cin, userInput);
    if(userInput == "Yes"){
        return true;
    }
    else{
        return false;
    }
};




