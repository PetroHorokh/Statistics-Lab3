import random
from math import sqrt


class SampleGenerator:
    def __init__(self, v, n, sum_limit, *args, **kwargs):
        self.v = v
        self.n = n
        self.a = self.v - 10
        self.sigma = 3 + self.v / 10
        self.sum_limit = sum_limit

    def generation_x(self):
        r = sum(random.uniform(0, 1) for _ in range(self.sum_limit))
        return (r - 6) * self.sigma + self.a

    def data_collector(self):
        X = [self.generation_x() for _ in range(self.n)]
        return X


class NumberAnalyzer:
    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    def sample_variance(self, data):
        mean_value = self.mean(data)
        total = 0
        for number in data:
            total += pow((number - mean_value), 2)
        return total / len(data)

    def sample_root_mean_square_deviation(self, data):
        return sqrt(self.sample_variance(data))
