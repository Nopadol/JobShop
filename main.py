import random
import array

from Tkinter import Tk
from tkFileDialog import askopenfilename
List =[]
crossover_rate = 0.2 #define crossover rate
mutation_rate = 0.05 #define
chromosome = []
maxtime = []
roulette = []
parent = []
child = []
listMinTime = []
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

numJobs = len(List)
numProcess = len(List[0])/2 #number of Process
nj = max([len(i) for i in List]) #Number of Jobs
print "\n"+"Number of Processs : "+str(numProcess)
print "Number of Jobs : "+str(numJobs)
print "Table : "+str(numProcess)+" X "+str(numJobs)+"\n"

process = [] #List of Process
numMachines = 0
for item in List:
    job = []
    for j in range( 0,len(item),2):
        job.append([item[j],item[j+1],List.index(item)])
        numMachines = max(numMachines,item[j])
    process.append(job)

process=zip(*process)

#####################################################################

def findmaxtime(child,numJobs,numMachines):
        maxJ = [0]*numJobs
        maxM = [0]*numMachines
        for p in child:
            for j in range(len(p)):
                machine = p[j][0]-1
                time = p[j][1]
                maxM[machine] = time + max(maxJ[j],maxM[machine])
                maxJ[j] = maxM[machine]
        maxTime = max(maxM)
        return maxTime

def generateChromosome(process,numJobs,numMachines):
    numC =input('Enter your Number of Chromosome : ')
    for i in range (0,numC):
        
        new_process = []
        for i in range(0,len(process)):
            new_process.append(list(process[i]))

        for i in range(0,len(new_process)):
            random.shuffle(new_process[i])

        chromosome.append(new_process)
        
        
        maxTime = findmaxtime(new_process,numJobs,numMachines)
        maxtime.append(maxTime)
    
#generateChromosome(process,nj,numMachines)



def roulettewheel():
    fitness = []
    allfit = 0
    alltime = 0
    alld = 0
    minfitness = [0.0]
    sr = 0
##    print "maxtex : "
##    print maxtime

    for i in range(0,len(maxtime)):
        alltime = maxtime[i]+alltime
    for j in range(0,len(maxtime)):
        fitness.append(float(alltime*1.0/maxtime[j]))
        allfit = (allfit*1.0)+float(alltime*1.0/maxtime[j])
    for k in range(0,len(fitness)):
        minfitness.append(float(fitness[k]*1.0/allfit))
        alld = (alld*1.0)+float(fitness[k]*1.0/allfit)
##    print "\n"
##    print minfitness
##    print "\n"
    minfitness.append(0.0)
    for p in range (1,len(minfitness)):
        sr = sr+minfitness[p-1]
        roulette.append(sr)
           
    roulette[len(roulette)-1] = 1.0
##    print "roulettewheel"
##    print roulette
##    print "\n"
#roulettewheel(chromosome,maxtime)

def randomroulette():
    while(len(parent)<=len(chromosome)/2):
        bufferlist = []
        for k in range(0,2):
            v = random.random()
            for j in range(0, len(roulette)):
                if ( v > roulette[j] and v <= roulette[j+1]):
                    bufferlist.append(j)
##        print bufferlist
        if(parent == [] and bufferlist[0]!=bufferlist[1]):
            parent.append(bufferlist)
        else:
            check = False
            for i in range(0,len(parent)):
                swapBufferlist = [bufferlist[1],bufferlist[0]]
                if (parent[i]==bufferlist and parent[i]==swapBufferlist):
                    print "fail"
                elif(bufferlist[0]==bufferlist[1]):
                    print "fail"
                else:
                    check = True
            if(check):
                parent.append(bufferlist)
    parent.pop();
##    print parent

        
#randomroulette(roulette)


def setRealChromosome():
 
    for k in range(0,len(chromosome)):
        bufferChromosome = chromosome[k]
        chromosome[k] = []
        for c in bufferChromosome:
            for i in c:
                    chromosome[k].append(i)

    
##setRealChromosome()

    

def cross(father,mother):
    child = list()
    for g in mother:
        if g[2] == j:
            mother.remove(g)
    for g in range(len(father)):                    
        if father[g][2] == j:   # check is job random
            child.append(father[g])
        else:
            child.append(mother.pop(0))
    return child


def mutation(child):
    for i in child:
        v = random.random()
        if(v < mutation_rate):
            r = random.randint(0,len(child)-1)
            a,b = child.index(i),r
            child[b],child[a] = child[a],child[b]

    return child
            
            



def crossover():
        
##        print "Crossover Chromosome :"+str(chromosome) 
        for c in parent:
            child1 = [[0]*3]*numJobs*numProcess
            child2 = [[0]*3]*numJobs*numProcess

            r = random.random() #random.random()   #randomcrossoverrate
            if( r < crossover_rate):
                j = random.randint(0,numJobs-1)
              
                
                child1 = cross(list(chromosome[c[0]]),list(chromosome[c[1]]))
                child2 = cross(list(chromosome[c[1]]),list(chromosome[c[0]]))

                child1 = [child1[i:i+numJobs] for i in range(0,numProcess*numJobs,numJobs)]
                child2 = [child2[i:i+numJobs] for i in range(0,numProcess*numJobs,numJobs)]
                        
##                print "child crossover"
                child.append(mutation(list(child1)))
                child.append(mutation(list(child2)))
                             
            else:
                child1 =  list(chromosome[c[0]])
                child2 =  list(chromosome[c[1]])
                child1 = [child1[i:i+numJobs] for i in range(0,numProcess*numJobs,numJobs)]
                child2 = [child2[i:i+numJobs] for i in range(0,numProcess*numJobs,numJobs)]
##                print "child"
                child.append(mutation(list(child1)))
                child.append(mutation(list(child2)))

                
        return child
                
#chromosome = crossover(chromosome,parent)


def main():
    chromosome = []
    generateChromosome(process,numJobs,numMachines)
    setRealChromosome()
    numR =input('Enter your Number of Round : ')
    for i in range(0,numR):
        print "Loop Round : " + str(i)
        roulette = []
        parent = []
        child = []
        roulettewheel()
        randomroulette()   
        chromosome = crossover()
        maxtime = []
        for j in chromosome:
            maxTime = findmaxtime(j,numJobs,numMachines)
            maxtime.append(maxTime)
        listMinTime.append(min(maxtime))
        print min(listMinTime)
main()



