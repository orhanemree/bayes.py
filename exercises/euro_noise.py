"""
My implementation of Exercise 4.1 from Think Bayes.
"""

import os
import sys
import random
from typing import cast

import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bayes


class Problem(bayes.Suite):

    def likelihood(self, data: bayes.nameType, hypo: bayes.nameType):
        hypo = cast(float, hypo)
        if data == "H":
            return hypo/100
        elif data == "T":
            return 1-hypo/100
        else:
            return 0
        
    def calculate(self, data: bayes.nameType):
        data = cast(str, data)
        for i in data:
            self.update(i)
        self.normalize()

        print("MODE", self.mode())
        print("MEAN", self.mean())
        print("MEDIAN", self.median())
        print("CI", self.confidence(.95))
        print("UNBIASED", self.prob(50))
        
    def set_noise(self, noise: float):
        self.noise = noise


def add_noise(data: str, noise: float):
    data_noised = ""
    for c in data:
        if noise >= random.random():
            if c == "H":
                data_noised += "T"
            elif c == "T":
                data_noised += "H"
            else: assert 0, "Unreachable"
        else:
            data_noised += c
    return data_noised


if __name__ == "__main__":
    random.seed(1)
    data = 80*"H"+30*"T"

    for i in range(5):
        # y = random.random()
        y = .10*i
        data_noised = add_noise(data, y)
        problem = Problem(list(range(101)))
        problem.normalize()
        problem.calculate(data_noised)

        x = list(problem.hypos.keys())
        y = list(problem.hypos.values())

        plt.plot(x, y) # type: ignore

    plt.show() # type: ignore
