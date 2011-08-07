#!/usr/bin/env python
# solve the problem using genetic algorithm

import sys,random

def fitness(line):
    print len(line)-line.count(" "),line.count(" "),dcount(line)
    score = (len(line)-line.count(" "))*5
    score += line.count(" ")*1
    score -= (dcount(line)*3)
    # having trouble here where line.count("  ") counts a squence of 4 spaces as 3 double spaces
    return score
    #score = len(line)-line.count(" ")
    #score *= 1
    #score += line.count(" ")*2
    #score -= line.count("  ")*3
    #return score

def test1():
    f1 = fitness("this is a  line")
    f2 = fitness("this is a line")
    f3 = fitness("this is a  ine")
    f4 = fitness("thisis a  line")
    print f1,f2,f3,f4
    assert(f1 < f2)
    assert(f3 < f1)
    assert(f4 < f1)

    f1 = fitness("a   spacesss")
    f2 = fitness("a  spacesss")
    f3 = fitness("a   pacesss")
    print f1,f2,f3
    assert(f1 < f2 and f3 < f1)

def dcount(line):
    # count the double spaces in this line.
    i=0
    last = False
    count=0

    for c in line:
        if c==' ':
            if last==True:
                count+=1
                last=False
            else:
                last=True
        elif last==True:
            last=False
            
    return count

def dcountTest():
    assert(dcount("  ")==1)
    assert(dcount("   ")==1)
    assert(dcount("    ")==2)
    assert(dcount(" ")==0)
    assert(dcount("aoeu ")==0)
    assert(dcount("a oeu ")==0)
    assert(dcount("aoeu  ")==1)

dcountTest()

def mutate(line):
    x = random.randint(0,len(line)-2)
    return line[:x] + line[x+1:]

def evolve(line):
    best = (fitness(line),line)

    for m in range(1000):
        mm = mutate(line)
        if fitness(mm) > best[0]:
            best = (fitness(mm),mm)

    return best[1]

test1()

for line in map(str.rstrip, sys.stdin.readlines()):
    print "l %d '%s'" % (len(line),line)

    for i in range(1000):
        line = evolve(line)
        print "e %d '%s'" %(fitness(line),line)

    print 'best', line





