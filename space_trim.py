#!/usr/bin/env python
# remove the extra spaces from a line using a genetic algorithm
# done by counting the 'deleted' characters. A organinsim is a set of 'deletions' from the source string.

import sys,random,Levenshtein

POP_SIZE = 100
GENERATIONS = 100

def wordCount(line):
    # count 'words' with spaces following them.
    last = False # last c was a character
    count=0
    for c in line:
        if last== True:
            if c == ' ':
                count+=1
                last=False
        else:
            if c != ' ':
                last = True
    return count

def wcTest():
    assert(wordCount("e ")==1)
    assert(wordCount("e  ")==1)
    assert(wordCount("e")==0)
    assert(wordCount("e e ")==2)
    assert(wordCount("e e")==1)

wcTest()

def fitness(line):
    score = wordCount(line)*30 #TODO these should be scaled up by the length of the input line that doesnt change.
    score += (len(line)-line.count(" "))*20
    score -= line.count(" ")
    return score

def fitnessTest():
    f1 = fitness("this is a  line")
    f2 = fitness("this is a line")
    f3 = fitness("this is a  ine")
    f4 = fitness("thisis a  line")
    assert(f1 < f2)
    assert(f3 < f1)
    assert(f4 < f1)

    f1 = fitness("a   spacesss")
    f2 = fitness("a  spacesss")
    f3 = fitness("a   pacesss")
    assert(f1 < f2 and f3 < f1)

fitnessTest()

def mutate(organism,line):
    choices = range(len(line)) # only return a deletion not in organism
    for c in organism:
        choices.remove(c)
    if len(choices)==0: return organism
    organism.append(random.choice(choices))
    return organism

def mate(f,m):
    return list(set(f+m)) # union of the two.

def lineFrom(deletions,line):
    s = range(0,len(line))
    for d in deletions:
        s.remove(d)
    l = []
    for c in s:
        l.append(line[c])
    return ''.join(l)

def lineFromTest():
    assert(lineFrom([0],"01234")=="1234")
    assert(lineFrom([0,1],"01234")=="234")
    assert(lineFrom([1,4],"01234")=="023")

lineFromTest()

def evolve(line):
    #build initual population
    p = []
    for i in range(POP_SIZE):
        o = []
        if random.randint(0,100) < 70:
            mutate(o,line)
        p.append((fitness(lineFrom(o,line)),o))
    p.sort()
    p.reverse()

    for g in range(GENERATIONS):
        p2 = p[:(len(p)/100)*10] # keep the top 10%

        # mating tornament for rest of population
        for i in range(len(p)-len(p2)):
            f = max(random.choice(p),random.choice(p))
            m = max(random.choice(p),random.choice(p))
            c = mate(m[1],f[1])
            if random.randint(0,100) < 30:
                c = mutate(c,line)
            p2.append((fitness(lineFrom(c,line)),c))
        p = p2
        p.sort()
        p.reverse()

    return lineFrom(p[0][1],line)

def correct(line):
    return ' '.join(line.split())

for line in map(str.rstrip, sys.stdin.readlines()):
    e = evolve(line)
    print "%s: '%s' => '%s'" % ('correct' if e==correct(line) else 'wrong', line,e)
