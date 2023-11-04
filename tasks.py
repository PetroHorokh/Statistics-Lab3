import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import norm

from data_collector import NumberAnalyzer

number_analyser = NumberAnalyzer()


def task1(data):
    values, base = np.histogram(data)
    cumulative = np.cumsum(values)
    relative_cumulative_frequency = cumulative / cumulative[-1]

    plt.figure(figsize=(10, 8))

    plt.plot(base[:-1], relative_cumulative_frequency, c='green', linewidth=3, label='Accumulated relative frequencies')

    plt.title('Accumulated frequency histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(loc='lower right')

    plt.show()


def task2(data):
    mu = number_analyser.mean(data)
    sigma = number_analyser.sample_root_mean_square_deviation(data=data)

    values, base = np.histogram(data, bins=40)
    cumulative = np.cumsum(values)
    relative_frequency = cumulative / cumulative[-1]

    x = np.linspace(min(data), max(data), 150)
    y = norm.cdf(x, mu, sigma)

    plt.figure(figsize=(10, 8))

    plt.plot(x, y, '-o', color='red', label='Normal Distribution')
    plt.plot(base[:-1], relative_frequency, c='green', label='Accumulated relative frequencies')
    plt.title('Accumulated frequency histogram approximation')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(loc='lower right')
    plt.show()


def task4(data):
    mu, std = np.mean(data), np.std(data)

    confidence_level = 0.95
    degrees_freedom = len(data) - 1
    confidence_interval = stats.t.interval(confidence_level, degrees_freedom, mu, stats.sem(data))
    print(f'Довірчий інтервал для середнього: {confidence_interval}')
    variance_interval = stats.chi2.interval(confidence_level, degrees_freedom, loc=np.var(data),
                                            scale=std ** 2 / len(data))
    print(f'Довірчий інтервал для дисперсії: {variance_interval}')


def task5(data):
    observed_frequencies, bins = np.histogram(data, bins='auto', density=False)

    expected_density, _ = np.histogram(data, bins=bins, density=True)
    bin_widths = np.diff(bins)
    expected_frequencies = expected_density * bin_widths * len(data)

    expected_frequencies[expected_frequencies == 0] = 0.1

    chi_square_stat, p_value = stats.chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)

    print("Значення хі-кватрадрат:", chi_square_stat)
    print("Теоретична ймовірность попадання випадкової величини на інтервал(p):", p_value)

    if p_value > 0.05:
        print('Не відхиляємо нульову гіпотезу, дані відповідають нормальному розподілу')
    else:
        print('Відхиляємо нульову гіпотезу, дані не відповідають нормальному розподілу')
