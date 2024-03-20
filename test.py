import filehandling
import userIO
import analysis
import time
#python file for testing methods
input_array = filehandling.OpenCSV()


functionkey = userIO.askkey()
graphon = userIO.YesNo("Graph 3d plot?")


[user_min,user_max] = userIO.get_user_range(input_array)

start_time = time.time()
XSC = analysis.parse_data(input_array,functionkey,user_min,user_max)
print("process finished in %s", time.time()-start_time)
userIO.plotly3d(XSC)
if graphon:
    userIO.plot3d(XSC)
save = userIO.YesNo("Save file?")

filehandling.WriteCSV(XSC)