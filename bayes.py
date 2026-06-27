from typing import cast

type nameType = int|float|str|Suite

class Suite:

    def __init__(self, hypos: dict[nameType, float] | list[nameType] | None = None, numeric_labels: bool = True):
        self.numeric_labels = numeric_labels
        if isinstance(hypos, dict):
            self.hypos = hypos.copy()
            if isinstance(list(self.hypos)[0], str):
                self.numeric_labels = 0
        elif isinstance(hypos, list):
            self.hypos = dict.fromkeys(hypos, 1.0)
        else:
            self.hypos = {}

    def set(self, hypo: nameType, prob: float):
        self.hypos[hypo] = prob

    def prob(self, hypo: nameType):
        return self.hypos.get(hypo)
    
    def likelihood(self, data: nameType, hypo: nameType) -> float:
        raise NotImplementedError()
    
    def update(self, data: nameType):
        for hypo, prob in self.hypos.items():
            self.hypos[hypo] = prob * self.likelihood(data, hypo)

    def normalize(self):
        x = sum(self.hypos.values())
        for hypo, prob in self.hypos.items():
            self.hypos.update({hypo: prob/x})
        return x
    
    def mode(self):
        return max(self.hypos.items(), key=lambda h: h[1])

    def percentile(self, percentage: float):
        total = 0
        for hypo, prob in self.hypos.items():
            total += prob
            if total >= percentage:
                return hypo
            
    def median(self):
        return self.percentile(.5)
    
    def mean(self):
        if self.numeric_labels:
            total = 0
            for hypo, prob in self.hypos.items():
                hypo = cast(float, hypo)
                total += hypo * prob
            return total/len(self.hypos)
        else:
            assert 0, "Not Implemented"
    
    def confidence(self, percentage: float):
        min_ = self.percentile(.5-percentage/2)
        max_ = self.percentile(.5+percentage/2)
        return (min_, max_)
