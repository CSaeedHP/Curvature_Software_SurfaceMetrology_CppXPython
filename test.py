import filehandling
import userIO

#python file for testing methods

input_array = filehandling.OpenCSV()

[user_min,user_max] = userIO.get_user_range(input_array)
