#!/usr/bin/env python
# solve the problem using genetic algorithm

import sys,random

def fitness(line):
    score = len(line)-line.count(" ")
    score += line.count(" ")
    score -= line.count("  ")*3

    return score

def mutate(line):
    if random.randint(0,100) < 1000:
        x = random.randint(0,len(line)-2)
        line = line[:x] + line[x+1:]
    return line

def evolve(line):
    mutations = []
    mutations.append((fitness(line),line))
    for m in range(100):
        mm = mutate(line)
        mutations.append((fitness(mm),mm))
    mutations = sorted(mutations)
    for f,m in mutations:
        #break
        print 'm',f,m
    print ''
    return mutations[len(mutations)-1][1]


for line in map(str.rstrip, sys.stdin.readlines()):
    print "l %d '%s'" % (len(line),line)

    for i in range(100):
        line = evolve(line)
        print "e %d '%s'" %(fitness(line),line)

    print 'best', line
