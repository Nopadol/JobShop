import random
import array
from Tkinter import Tk
from tkFileDialog import askopenfilename
List =[]

#Input Files to List !!

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

f=open(filename)
f.read()
for line in open(filename) :
    print line.rstrip('\n') # .rstrip('\n') removes the line break
    List.append([int(item) for item in line.rstrip('\n').split('\t')])
f.close()

Jobs = len(List)
Machines = len(List[1])/2

print "\n"+"Number of Jobs : "+str(Jobs)
print "Number of Machines : "+str(Machines)
print "Table : "+str(Jobs)+" X "+str(Machines)

######################################
#Value of Mutation = 0.05
#Value of Crossover = 0.2
######################################

    
