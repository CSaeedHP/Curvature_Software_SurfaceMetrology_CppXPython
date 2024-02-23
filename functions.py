import math
import csv
import numpy as np
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing


def get_folder():
    folder_path = filedialog.askopenfile()
    inputarray = np.genfromtxt(folder_path, delimiter=",")
    return inputarray

def get_range(array_range):
    min_length_interval = (array_range[1,0] - array_range[0,0])
    if len(array_range) % 2 == 1:
        max_length_interval = (round(len(array_range) / 2) - 1) * min_length_interval
    else:
        max_length_interval = (len(array_range) / 2 - 1) * min_length_interval
    return min_length_interval, max_length_interval

def user_range(min_interval,max_interval):
    choice = input(f"The sampling interval currently ranges from {min_interval} to {max_interval}. \n Would you like to input your "
                   f"own range? Y/N \n").lower()
    if choice == 'y':
        user_lower = float(input(f"Please choose a lower bound. The smallest possible lower bound is {min_interval} \n"))
        if user_lower < min_interval:
            print(f"Your input value was too small. Your lower bound is now {min_interval}")
        user_upper = float(input(f"Please choose an upper bound. The largest possible upper bound is {max_interval} \n"))
        if user_upper > max_interval:
            print(f"Your input value was too large. Your upper bound is now {max_interval}")
    else:
        user_lower = min_interval
        user_upper = max_interval
    user_lower = math.floor(user_lower/min_interval)
    user_upper = math.ceil(user_upper/min_interval)
    return user_lower,user_upper


input_array = get_folder()
print(input_array)
minimum_possible, maximum_possible = get_range(input_array)

user_min,user_max = user_range(minimum_possible,maximum_possible)
print(user_min)
print(user_max)

function_key = input("Please indicate what kind of analysis you would like to perform. \n")

def array_repackager(input_array,user_lower,user_upper):
    repackaged = np.empty((0,2),float)
    for sampling_interval in range(user_lower,user_upper+1):
        for array_index in range (0, len(input_array)-2*sampling_interval):
            group = np.array([[input_array[array_index,0],input_array[array_index,1]]], 
                             [[input_array[array_index + sampling_interval, 0], input_array[array_index + sampling_interval, 1]]],
                             [[input_array[array_index + 2 * sampling_interval, 0], input_array[array_index + 2 * sampling_interval, 1]]])
            repackaged = np.append(repackaged, group)
            # repackaged = np.append(repackaged, [[input_array[array_index,0],input_array[array_index,1]]], axis = 0)
            # repackaged = np.append(repackaged, [[input_array[array_index + sampling_interval, 0], input_array[array_index + sampling_interval, 1]]], axis = 0)
            # repackaged = np.append(repackaged, [[input_array[array_index + 2 * sampling_interval, 0], input_array[array_index + 2 * sampling_interval, 1]]], axis = 0)
    return repackaged
new_array = array_repackager(input_array,user_min,user_max)
print(new_array)
