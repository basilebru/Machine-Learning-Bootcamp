import numpy as np 
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, '../ex03')
from mylinearregression import MyLinearRegression
from csvreader import CsvReader

# 1: import data

with CsvReader("spacecraft_data.csv", header = True, skip_top = 0, skip_bottom = 0) as csv_file:
    data = np.array(csv_file.getdata(), float)
    #Xage = data[:, 0:1]
    Xage = data[:, 0:3]
    Yprice = data[:, 3:4]

# 2: perform fit

#tr = MyLinearRegression([516, -1])
tr = MyLinearRegression([8., -10., 7., -2.])
print(tr.mse_(Xage, Yprice))
print(tr.fit_(Xage, Yprice, 1e-4, 1000))
#print(tr.cost_(Xage, Yprice))
print(tr.mse_(Xage, Yprice))

# 3: print plot

plt.plot(Xage[:, 0:1], Yprice, 'bo', label = "Strue")
#plt.plot(Xage, tr.predict_(Xage), 'g')
plt.plot(Xage[:, 0:1], tr.predict_(Xage), 'go', label ="Spredict")
plt.ylabel('sell price')
plt.xlabel('age')
plt.grid()
plt.legend()
plt.show()