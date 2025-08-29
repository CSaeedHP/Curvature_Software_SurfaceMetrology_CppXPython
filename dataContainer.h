#ifndef DATACONTAINER_H
#define DATACONTAINER_H
#include <cstring>
#include <cmath>
#include <cstdint>
/**
* 
*/

// Point data type to store x value and z value
typedef struct{
    double x;
    double z;
}point;

// This struct stores an array of curvatures and the scale at whitch they were calculated
class CurvatureScale {

    public:

        // constructors
        CurvatureScale();
        CurvatureScale(double *curvatureArray, int dataLength, double scale, point *pointArray);

        // destructor
        ~CurvatureScale(){};
        
        // getters
        double getCurvature(int index);
        double getScale();
        int getLength();
        point getPoint(int index);

        
        //----------------------------------------------------------------------------------------------------------------
        // setters
        
        // sets the curvature array from an external array
        void setCurvatureArray(double* curvatureArray, int dataLength);
        void setCurvatureArray(int dataLength);
        
        // sets curvature at index
        void setCurvature(double curvature, int index);
        
        
        // sets the percentErrorArray from an external array
        void setPercentErrorArray(double* PercentErrorArray, int dataLength);
        void setPercentErrorArray(int dataLength);

        // sets percentError at index
        void setPercentError(double curvature, int index);


        /**
        * Function: setScale()
        * Sets the value of the scale parameter
        * @param scale: The scale at which this data was calculated
        */
        void setScale(int scale);

    private:
        int scale;
        double* curvatureArray;
        double* percentErrorArray;
        point* pointArray;
        int dataLength;

};

class DataContainer {

    public:

        // Constructors 
        DataContainer() : pointArray(nullptr), curvatureScaleArray(nullptr), pointArrayLength(0), 
                          curvatureArrayLength(0), minLength(0), maxHalfIntervalPossible(0), odd(false), 
                          min(0), max(0), avgPos(0), posAvgDenominator(0), avgNeg(0), negAvgDenominator(0), 
                          fiveExtremes{0, 0} {}

        DataContainer(point* pointArray, int dataLength);
        
        // Destructor deletes the arrays and pointers so memory is not leaked
        ~DataContainer ();
        
        // getters
        CurvatureScale* getIndex(int index);
        CurvatureScale* getScale(double scale);
        int getCurvatureArrayLength();

        point getPoint(int index);
        int getPointArrayLength();
        int64_t getNumOps();
        point* getPointAddress(int index);
        double getMinLength();
        double getMaxLength();
        double getmaxHalfIntervalPossible();

        // setters
        void setIndex(int index, CurvatureScale* data);
        void putCurvature(int scale, int index, double curvature);
        void putPE(int scale, int index, double percentError);
        void setPointArray(point *pointArray, int dataLength);
        void setPointArray(int dataLength);
        void setCurvatureScaleArray(int dataLength);
        void setPoint(int index, point point);
        void setmaxhalfinterval();
        void setNumOps(const int& minScale, const int& maxScale);        
        
        // Statistics functions ----------------------------------------------------------------------------------------------

        // Setters
        void setAbsMin(double value);
        void setAbsMax(double value);
        void setAvgPos(double value);
        void setPosAvgDenominator (int value);
        void setAvgNeg(double value);
        void setNegAvgDenominator (int value);
        void updateFiveExtremes(double curvature, double pos);

        // Getters
        double getAbsMin() const ;
        double getAbsMax() const;
        double getAvgPos() const;
        double getPosAvgDenominator() const;
        double getAvgNeg() const;
        double getNegAvgDenominator() const;
        point** getFiveExtremes();

        friend class UserData;
        
    private:
        // This array stores the height data from input file
        point* pointArray;
        int pointArrayLength;
        
        // This array stores a list of curvature scale objects. Each object stores the curvature array at a scale
        CurvatureScale* curvatureScaleArray;
        int64_t curvatureArrayLength;

        //Properties of data
        double minLength;
        double maxLength;
        int maxHalfIntervalPossible;
        bool odd;

        //Property of analysis
        int64_t numOps;

        double min;
        double max;
        double avgPos;
        double posAvgDenominator;    
        double avgNeg;
        double negAvgDenominator;
        point* fiveExtremes[5];

        
};

#endif
