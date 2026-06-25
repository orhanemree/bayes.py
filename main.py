import bayes
from typing import cast
import matplotlib.pyplot as plt

class Problem(bayes.Suite):

    def likelihood(self, data: bayes.nameType, hypo: bayes.nameType):
        hypo = cast(float, hypo)
        if data == "H":
            return hypo/100
        elif data == "T":
            return 1-hypo/100
        else:
            return 0
    
problem = Problem() 
for i in range(51):
    problem.set(i, i) # probability of H
for i in range(50):
    problem.set(i+51, 49-i)

# problem = Problem(list(range(101)))
problem.normalize()
data = 140*"H" + 110*"T"
for i in data:
    problem.update(i)
problem.normalize()

print(problem.mode())
print(problem.mean())
print(problem.median())
print(problem.confidence(.95))


x = list(problem.hypos.keys())
y = list(problem.hypos.values())


plt.plot(x, y) # type: ignore
plt.show() # type: ignore