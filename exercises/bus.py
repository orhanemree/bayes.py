"""
My implementation of Exercise 7.1 from Think Bayes.
"""

import os
import sys
from typing import cast
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bayes


class Problem(bayes.Suite):

    def likelihood(self, data: bayes.nameType, hypo: bayes.nameType) -> float:
        hypo = cast(float, hypo)
        return hypo # proportional to hypo, normalize after


if __name__ == "__main__":
    problem = Problem({ 10: .5, 20: .3, 40: .2 })
    data = 0 # any data
    problem.update(data)
    problem.normalize()

    wait_time = bayes.Suite()
    for i in range(41):
        prob = 0
        prob += problem.prob(40)*1/40
        if i <= 20:
            prob += problem.prob(20)*1/20
        if i <= 10:
            prob += problem.prob(10)*1/10
        wait_time.set(i, prob)
        
    wait_time.normalize()
    print("MODE", wait_time.mode())
    print("MEAN", wait_time.mean())
    print("MEDIAN", wait_time.median())
    print("CI", wait_time.confidence(.95))

    x = list(wait_time.hypos.keys())
    y = list(wait_time.hypos.values())
    plt.plot(x, y) # type: ignore
    plt.show() # type: ignore
