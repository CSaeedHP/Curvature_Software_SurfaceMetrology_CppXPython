import filehandling
import userIO
import analysis
import time

#python file for testing methods

functionkey = userIO.askkey()

input_array = filehandling.OpenCSV()

[user_min,user_max] = userIO.get_user_range(input_array)

start_time = time.time()
XSC = analysis.parse_data(input_array,functionkey,user_min,user_max)
print("process finished in %s", time.time()-start_time)

userIO.plot3d(XSC)