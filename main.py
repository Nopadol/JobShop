import random
import array
from Tkinter import Tk
from tkFileDialog import askopenfilename
List =[]
Chromosome = []
crossover_rate = 0.2 #define crossover rate
mutation = 0.05 #define mutation rate

#####################################################################
#Input Files to List !!

Tk().withdraw() 
filename = askopenfilename() 
print(filename)

file =open(filename)
file.read()
for line in open(filename) :
    print line.rstrip('\n') # .rstrip('\n') removes the line break
    List.append([int(item) for item in line.rstrip('\n').split('\t')])
file.close()

Jobs = len(List)
Machines = len(List[1])/2

print "\n"+"Number of Jobs : "+str(Jobs)
print "Number of Machines : "+str(Machines)
print "Table : "+str(Jobs)+" X "+str(Machines)+"\n"

######## End of Input file ##########################################

#####################################################################
#Number of Chromosome = 20  #########################################
#Crossover_rate = 0.2       #########################################
#Mutation_rate = 0.05       #########################################
#####################################################################

def generateChromosome(Chromosome,List,Machines,Jobs):
    #####Chromosome Machines
    NumC = input('Enter Number of Chromosome : ')
    for c in range (0,NumC,1):
        tmp = []
        for j in range (0,Jobs,1):
            s=list(range(1,Machines+1))
            random.shuffle(s)
            for k in range (0,Machines):
                tmp.append(s[k])
            #print(s)
        random.shuffle(tmp)       
        Chromosome.append(tmp)
        #print Chromosome
 
generateChromosome(Chromosome,List,Machines,Jobs)

def defineMinFitness(Chromosome,List,Machines,Jobs):
    print Chromosome
    print Chromosome[0][0:len(Chromosome[0])]
    ret = []
    for line in List :
        tmp = {}
        for j in range (0,len(line),2):
            tmp[line[j]]= line[j+1]
        ret.append(tmp)
    print "\n\n\n",ret
    print "\n\n\n"
    for i in ret:
        print i[1]
    print [i[1] for i in ret]

defineMinFitness(Chromosome,List,Machines,Jobs)
    
