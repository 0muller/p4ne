from matplotlib import pyplot
from openpyxl import load_workbook
wb=load_workbook('data_analysis_lab.xlsx') #load table
sheet = wb['Data'] #Load list Data

def getvalue(x): return x.value


yars=list(map(getvalue, sheet['A'][1:])) #List columm A
temp=list(map(getvalue, sheet['C'][1:])) #List C
active=list(map(getvalue, sheet['D'][1:])) # Lsit D

pyplot.plot(yars, active, label="activity Sun")
pyplot.plot(yars, temp, label="Temp Sun")

pyplot.show()
