import matplotlib.pyplot as plt
import pandas as pd

def crunch():
    print("Running")
    lDistances, wDistances = [], []
    names = []

    #process long club data
    longData = pd.read_csv('data/Long Club Data.csv')
    for name, value in longData.iloc[:, 1:].iteritems():
        #print(f'Name: {name}, Value: {sum(value.values)}')
        lDistances.append((sum(value.values), name))
        names.append(name)

    #process wedge data
    wedgeData = pd.read_csv('data/Wedge Data.csv')
    for name, value in wedgeData.iloc[:, 1:].iteritems():
        #print(f'Name: {name}, Value: {sum(value.values)}')
        wDistances.append((sum(value.values), name))
        names.append(name)

    wDistances.sort()
    lDistances.sort()
    maxName = len(max(names, key = len))

    #format output
    file = open('output/distances.txt', 'w')
    file.write('-'*50+'\n')
    word = ''
    for x in range(max([len(wDistances), len(lDistances)])):
        if(x >= len(lDistances)):
            word = wDistances[x][1].ljust(maxName+1)+ ' | ' + str(wDistances[x][0]).rjust(5)
            file.write(word+'\n')
            file.write('-'*20+'\n')
        else:
            word = wDistances[x][1].ljust(maxName+1)+' | '+str(wDistances[x][0]).rjust(5)+'     <|>     '+lDistances[x][1].ljust(maxName+1)+' | '+str(lDistances[x][0]).rjust(5)
            file.write(word+'\n')
            file.write('-'*50+'\n')

    file.close()
    print("File Updated, look in distances.txt")