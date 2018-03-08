"""
Data link: http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/
"""

import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

x_axisdata = []
y_axisdata = []

with open("forestfires.csv") as ff:
    csvreader = csv.reader(ff, delimiter=',')

    next(csvreader)
    for line in csvreader:
        temporary = float(line[8])
        humidity = float(line[9])
        wind = float(line[10])
        rain = float(line[11])
        area = 1 if float(line[12]) > 0 else 0
        x_axisdata.append([temporary, humidity, wind, rain])
        y_axisdata.append(area)

np_x_axisdata = np.array(x_axisdata)
np_y_axisdata = np.array(y_axisdata)

model = LinearDiscriminantAnalysis()
model.fit(np_x_axisdata, np_y_axisdata)

temporary = 30
humidity = 90
wind = 8
rain = 0.1
print(" Temperature [%f] , relative humidity [%f] , wind speed [%f] and rain [%f]" % (temporary, humidity, wind, rain))
if model.predict([[temporary, humidity, wind, rain]])[0]:
    print("Having more chance to have a forest fire")
else:
    print("Forest fire may not happen")

temporary = 5
humidity = 20
wind = 0.5
rain = 5.8
print("With temperature [%f], relative humidity [%f] wind speed [%f] rain [%f]" % (temporary, humidity, wind, rain))
if model.predict([[temporary, humidity, wind, rain]])[0]:
    print("Having more chance to have a forest fire")
else:
    print("Forest fire may not happen")

