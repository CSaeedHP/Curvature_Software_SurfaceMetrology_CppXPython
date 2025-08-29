#ifndef USERINPUTCLI_H
#define USERINPUTCLI_H
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

using namespace std;
class cliInput{
    public:
        //functions to get data from command line
        static string getString(string message);
        static int getInt(string message);
        static double getDouble(string message);
        static bool getYesNo(string message);

        //functions to get data from file
};





#endif