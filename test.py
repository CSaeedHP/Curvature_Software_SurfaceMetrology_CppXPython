import filehandling
import userIO
import analysis
import time
import random
import display
import matplotlib.pyplot as plt
import matplotlib as mpl
#python file for testing methods

#asking user for info
input_array = filehandling.OpenCSV()

plt.figure(1)
display2d = display.plot2d(input_array)
[functionkey,obtusekey,acutekey] = userIO.askkey()

[user_min,user_max] = userIO.get_user_range(input_array)


#analysis
start_time = time.time()

# totalops = userIO.totalCurvaturesScales(input_array,user_min,user_max)
if functionkey == "hybrid":
    XSC = analysis.parse_hybrid_data(input_array,obtusekey,acutekey,user_min,user_max)
else:
    XSC = analysis.parse_data(input_array,functionkey,user_min,user_max)
print(f"process finished in {time.time()-start_time}s")
print(len(XSC)) #debug purposes check len xsc
#plotting
# if totalops > 1000000:
#     print("Note: graphing not recommended with large amounts of data.") totalops unfinished
graphon = userIO.YesNo("Graph 3d plot?")
plt.figure(2)
if graphon:
    if len(XSC) > 1000000:
        print("Note: graphing not recommended with large amounts of data.")
        if userIO.YesNo("Continue with graphing?"):
            print("graphing...")
            display.plot3d(XSC)
        elif userIO.YesNo("Graph with a random sample of 1 million points?"):
            print("graphing...")
            samplepoints = random.sample(XSC,1000000)
            display.plotly3d(samplepoints)
    else:
        print("graphing...")
        # samplepoints = random.sample(XSC,10000)
        # display.plotly3d(samplepoints)
        display3d = display.plot3d(XSC)

plt.show(block = False)
if userIO.YesNo("Save File?"):
    print("saving file...")
    filehandling.WriteCSV(XSC)
print("Task finalized!")