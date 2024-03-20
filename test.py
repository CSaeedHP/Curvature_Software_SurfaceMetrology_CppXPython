import filehandling
import userIO
import analysis
import time
#python file for testing methods

#asking user for info
input_array = filehandling.OpenCSV()
functionkey = userIO.askkey()
graphon = userIO.YesNo("Graph 3d plot?")
[user_min,user_max] = userIO.get_user_range(input_array)



#analysis
start_time = time.time()
print("analyzing data...")
XSC = analysis.parse_data(input_array,functionkey,user_min,user_max)
print("process finished in %s", time.time()-start_time)

#plotting
# userIO.plotly3d(XSC)
if graphon:
    userIO.plot3d(XSC)
# save = userIO.YesNo("Save file?")

# filehandling.WriteCSV(XSC)