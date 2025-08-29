#include<stdio.h> 
#include<stdlib.h>
#include<iostream>
// #include"gui.h"
#include "dataContainer.h"

int main() {
  point *pointArray = new point[5];
  pointArray[0] = {0,0};
  pointArray[1] = {1,1};
  pointArray[2] = {2,0};
  pointArray[3] = {4,5};
  pointArray[4] = {3,6};
  DataContainer *data = new DataContainer(pointArray, 5);
  // data->setPointArray(pointArray, 5);
  CurvatureScale *curv = data->getIndex(0);
  curv->setScale(0.5);
  curv->setCurvature(0.3, 0);
  
  printf("curve array size: %d\n", data->getCurvatureArrayLength());
  printf("curve 0: %lf\n", curv->getCurvature(0));
  printf("point 3: x:%lf z:%lf", data->getPoint(3).x, data->getPoint(3).z);
}
