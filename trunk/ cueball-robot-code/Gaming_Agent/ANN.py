################################
#need to get a, b, c, d, x from vision code...
#x is input vectors with form: [[a], [b], ..., [n]]
#will define using dummy constants for now:
a, b, c, d = 3, 9, 4, 7
x = [[12, 41, True], [5, 29, True], [6, 52, False], [5, 9, False]]
#each vector has form [magnitude (unit TBD), direction (degrees), bool]
#True is my ball, false is opponent ball
#all vectors start at white ball and intersect with ball(s) and pockets
#note: need to establish common "0 degree" could use East?
#remember to change the above...
################################
import math
#import physics_solver

#a is possible likely success for me
#b is total number of vectors available to me
#c is possible likely successes for opponent
#d is total number of vectors available to opponent
#please note: error is a discrete value which remains constant for all nodes

def ERROR(a, b, c, d):
    a, b, c, d = float(a), float(b), float(c), float(d)
    E = 1 - ((a/b) + (c/d))
    #print E
    return E

inputs = [] #the tricky part of this algorithm is representing the inputs as state

def firstLayerNeuron(E, eta, inputs):
    j, first_layer_out = len(inputs), []
    for i in range(0, j):
        g = E*eta*inputs[i]
        first_layer_out.append(g)
    #print first_layer_out
    return first_layer_out

def sigmoid(q):
    r = 1.0/(1 + math.e**(-q))
    #print r
    return r

def step(r, thr):
    if r > thr:
        return 1
    elif r <= thr:
        return 0

#######
#inputs = physics_solver.solve(x)
E = ERROR(a, b, c, d)
eta, thr, inputs = 0.1, 0.5, [1, 3, 2, 5, 4, -5, -2]#"inputs" and "eta" are dummy values
#inputs represent utility of each vector
#might want to change learning rate and threshold with genetic algorithm

####
#l = neuron(E, eta, inputs)
#r = sigmoid(l)
#k = step(r)
####

lenInputs = len(inputs)
firstLayer = []
for i in range(0, lenInputs):
    l = firstLayerNeuron(E, eta, inputs)
    r = sigmoid(l[i])
    print r
    q = step(r, thr)
    #print q
    firstLayer.append(q)

print firstLayer
