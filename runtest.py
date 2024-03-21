# import test
# bar = getattr(test,"foo")
# result = bar(3)
# print(result)
from tkinter import filedialog
import csv
s = [[1,2,3],
 [2,3,4],
 [3,4,5]]


new_file = filedialog.asksaveasfile()
writer = csv.writer(new_file)
writer.writerows(s)


