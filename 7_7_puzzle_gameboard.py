
from gurobipy import *

P = [
    [5,4,6,7,1,5,6],
    [9,8,5,1,1,2,3],
    [1,7,4,6,2,3,5],
    [1,1,2,4,2,6,2],
    [15,12,1,3,10,8,2],
    [16,17,1,1,6,6,2],
    [3,5,8,1,2,1,1]
]

m = Model() #Gurobi Model is created

#Variables for the model
C = []
for i in range(len(P)):
    row = []
    for j in range(len(P[0])):
        v = m.addVar(lb=0, ub=1, vtype=GRB.BINARY, name=str(i)+","+str(j))
        row.append(v)
    C.append(row)

#Objectives
obj = 0
for i in range(len(P)):
    for j in range(len(P[0])):
        obj += C[i][j]*P[i][j]
m.setObjective(obj, GRB.MAXIMIZE) #Objective is to maximize the sum

#Constraints
for i in range(len(P)):
    const = 0
    for j in range(len(P[0])):
        const += C[i][j]
    m.addConstr(const == 1)

for j in range(len(P[0])):
    const = 0
    for i in range(len(P)):
        const += C[i][j]
    m.addConstr(const == 1)

m.optimize()

#Print result
for i in range(len(C)):
    for j in range(len(C[0])):
        if int(C[i][j].x) == 1:
            print("Row: ",i+1, ", Col: ",j+1)
print("Score: ",m.objVal)

