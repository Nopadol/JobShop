import random
import array
from Tkinter import Tk
from tkFileDialog import askopenfilename
List =[]
Chromosome = []
Chromosome_map = []
ret = []
crossover_rate = 0.2 #define crossover rate
mutation = 0.05 #define mutation rate
iteration = 50
machine_table = []
operation_table = []

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

######################################
#Value of Mutation = 0.05
#Value of Crossover = 0.2
######################################

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


def mappingChromosomeRet(Chromosome,ret):
    for i in range(0,len(Chromosome)-1):
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        Chromosome_map.append([]);
        print "Case : ",
        for j in range(0,len(Chromosome[i])-1):
            bufferInt = Chromosome[i][j]
            if(bufferInt == 1):
                Chromosome_map[i].append(ret[a][bufferInt])
                print ret[a][bufferInt],
                a+=1
            if(bufferInt == 2):
                Chromosome_map[i].append(ret[b][bufferInt])
                print ret[b][bufferInt],
                b+=1
            if(bufferInt == 3):
                Chromosome_map[i].append(ret[c][bufferInt])
                print ret[c][bufferInt],
                c+=1
            if(bufferInt == 4):
                Chromosome_map[i].append(ret[d][bufferInt])
                print ret[d][bufferInt],
                d+=1
            if(bufferInt == 5):
                Chromosome_map[i].append(ret[e][bufferInt])
                print ret[e][bufferInt],
                e+=1
        print ""

mappingChromosomeRet(Chromosome,ret)
    

def createInputTable(List):
    for i in range(0,len(List)):
        bufferList = []
        print "Case" + str(i),
        for j in range(0,len(List[i])):
            bufferList.append(List[j][i])
            print List[j][i],
        if(i%2 == 0):
            machine_table.append(bufferList)
        else:
            operation_table.append(bufferList)
        print ""

createInputTable(List)


def calculateJobshop(Chromosome,Chromosome_map):
    
