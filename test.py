import filehandling
import userIO
import analysis
import time
import random
#python file for testing methods

#asking user for info
input_array = filehandling.OpenCSV()
functionkey = userIO.askkey()

[user_min,user_max] = userIO.get_user_range(input_array)



#analysis
start_time = time.time()

# totalops = userIO.totalCurvaturesScales(input_array,user_min,user_max)
XSC = analysis.parse_data(input_array,functionkey,user_min,user_max)
print("process finished in %s", time.time()-start_time)
print(len(XSC)) #debug purposes check len xsc
#plotting
# if totalops > 1000000:
#     print("Note: graphing not recommended with large amounts of data.") totalops unfinished
graphon = userIO.YesNo("Graph 3d plot?")
if graphon:
    if totalops > 1000000:
        print("Note: graphing not recommended with large amounts of data.")
        if userIO.YesNo("Continue with graphing?"):
            print("graphing...")
            userIO.plot3d(XSC)
        # elif userIO.YesNo("Graph with a random sample of 1 million points?"):
        #     print("graphing...")
        #     samplepoints = random.sample(1000000,XSC)
        #     userIO.plotly3d(samplepoints)
# save = userIO.YesNo("Save file?")

# filehandling.WriteCSV(XSC)