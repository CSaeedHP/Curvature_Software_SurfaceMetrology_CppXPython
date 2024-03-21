from tkinter import filedialog
import tkinter
import math

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from analysis import *
import time
#pip install plotly
import plotly.graph_objects as go

tkinter.Tk().withdraw()
def fileselect():
    '''opens computer file dialogue window'''
    fileToOpen =filedialog.askopenfile()
    return fileToOpen

function_keys = {
    "herons" : "herons_curvature",
    "diffslope" : "diff_slope",
    "calculus" : "quad_curvature",
    "3lag" : "oriented_lagrangian",
    "fda" : "fin_diff_slope"
}

def YesNo(message):
    '''returns boolean of user's response'''
    question = str(input(message + "\n"))
    if question == "y" or question == "Y":
        answer = True
    else:
        answer = False
    return answer
def askkey():
    '''gets functionkey from user, checks to make sure functionkey is valid'''
    listofkey = function_keys.keys()
    functionkey = input('Please select function analysis, or type "help" for help \n')
    while not functionkey in listofkey:
        if functionkey == "help":
            print("To select function analysis, choose one of the following functions:")
            print(listofkey)
            functionkey = input('Please select function analysis, or type "help" for help \n')
        else:
            functionkey = input('Your function key is invalid. Please enter a valid function key, or type "help" for more info \n')
    return functionkey



#get_range and user_range are helper functions of get_user_range
def get_range(input_array):
    '''determines minimum and maximum interval, handles odd and even data'''
    min_length_interval = (input_array[1][0] - input_array[0][0])
    if len(input_array) % 2 == 1: #odd even data handler
        max_length_interval = ((len(input_array) -1)/2)* min_length_interval
        odd = True
    else:
        max_length_interval = (len(input_array) / 2 - 1) * min_length_interval
        odd = False
    return min_length_interval, max_length_interval,odd





def user_range(min_interval,max_interval):
    '''using minimum and maximum interval, prompts user to check if narrower scope is wanted'''
    choice = input(f"The sampling interval currently ranges from {min_interval} to {max_interval}.\nWould you like to input your "
                   f"own range? Y/N \n").lower()
    scale_user_lower = 1
    scale_user_upper = 0
    if choice == 'y':
        while scale_user_lower > scale_user_upper:
            user_lower = float(input(f"Please choose a lower bound. The smallest possible lower bound is {min_interval} \n"))
            if user_lower < min_interval:
                print(f"Your input value was too small. Your lower bound was automatically set to {min_interval}")
                user_lower = min_interval
            user_upper = float(input(f"Please choose an upper bound. The largest possible upper bound is {max_interval} \n"))
            if user_upper > max_interval:
                print(f"Your input value was too large. Your upper bound was automatically set to {max_interval}")
                user_upper = max_interval
            scale_user_lower = math.floor(user_lower/min_interval)
            scale_user_upper = math.ceil(user_upper/min_interval)
            if scale_user_lower > scale_user_upper:
                print("Error: Minimum value cannot exceed Maximum value, please reenter your bounds.")
    else:
        user_lower = min_interval
        user_upper = max_interval
        print(f"Bounds have been automatically set to ({user_lower},{user_upper})")
        scale_user_lower = math.floor(user_lower/min_interval)
        scale_user_upper = math.ceil(user_upper/min_interval)  
    print(f"Your selected bounds are ({user_lower},{user_upper})")
    return scale_user_lower,scale_user_upper,max_interval/min_interval




def evendata(scales,min,max):
    minops = scales - min + 1
    maxops = scales - max
    totalops = minops**2 + minops - maxops ** 2 - maxops
    return totalops

def odddata(scales,min,max):
    minops = scales - min + 1
    maxops = scales - max
    totalops = minops**2 - maxops ** 2
    return totalops

def get_user_range(input_array):
    '''gets user range from input array after prompting user'''
    [min_length_interval,max_length_interval,odd] = get_range(input_array)
    [usermin,usermax,maxscale] =  user_range(min_length_interval,max_length_interval)
    if (odd):
        print("odd number of datapoints")
        print(f"{odddata(maxscale,usermin,usermax)} total operations in progress")
    else:
        print("even number of datapoints")
        print(f"{evendata(maxscale,usermin,usermax)} total operations in progress")
    return usermin,usermax








# def ops(datanumber):
#     totaloperations = datanumber^2
#     print(datanumber)
#     if datanumber%2 == 1:
#         totaloperations = datanumber * datanumber
#     else:
#         totaloperations = datanumber * (datanumber + 1)
#     print(totaloperations)
#     return totaloperations
def totalCurvaturesScales(data,min,max):
    datamax = len(data)
    totalops = ((ops(datamax - 2*min) - ops(datamax - 2*max)))/4
    print("analyzing data...")
    print(f"{totalops} curvatures calculating...\n{max-min+1} scales calculating...")
    return totalops
# totalops = ((ops(10001 - 2) - ops(10001-10000)))
# print(totalops)