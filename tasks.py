import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import norm, pearsonr

from for_MS.data_collector import NumberAnalyzer

number_analyser = NumberAnalyzer()


def task_1(data):
    values, base = np.histogram(data, bins=40)
    cumulative = np.cumsum(values)
    relative_frequency = cumulative / cumulative[-1]

    plt.figure(figsize=(10, 6))

    plt.plot(base[:-1], relative_frequency, c='red', label='Накопичені відносні частоти')

    plt.title('Гістограма накопичених відносних частот')
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.legend(loc='upper left')

    plt.show()


def task_2(data):
    mu = number_analyser.mean(data)
    sigma = number_analyser.sample_root_mean_square_deviation(data=data)

    values, base = np.histogram(data, bins=40)
    cumulative = np.cumsum(values)
    relative_frequency = cumulative / cumulative[-1]

    x = np.linspace(min(data), max(data), 100)
    y = norm.cdf(x, mu, sigma)

    plt.plot(x, y, '-o', color='orange', label='Normal Distribution')
    plt.plot(base[:-1], relative_frequency, c='red', label='Накопичені відносні частоти')
    plt.legend()
    plt.show()


def task_4(data):
    mu, std = np.mean(data), np.std(data)

    confidence_level = 0.95
    degrees_freedom = len(data) - 1
    confidence_interval = stats.t.interval(confidence_level, degrees_freedom, mu, stats.sem(data))
    print(f'Довірчий інтервал для середнього: {confidence_interval}')
    variance_interval = stats.chi2.interval(confidence_level, degrees_freedom, loc=np.var(data),
                                            scale=std ** 2 / len(data))
    print(f'Довірчий інтервал для дисперсії: {variance_interval}')


def task_5(data):
    mu = np.mean(data)
    sigma = np.std(data)
    num_bins = 'auto'  # використовуйте 'auto' для автоматичного вибору кількості бінів

    # Підрахуйте спостережувані частоти (без нормалізації)
    observed_frequencies, bins = np.histogram(data, bins=num_bins, density=False)

    # Обчисліть очікувані частоти
    expected_density, _ = np.histogram(data, bins=bins, density=True)
    bin_widths = np.diff(bins)
    expected_frequencies = expected_density * bin_widths * len(data)

    # Уникнення нульових значень в очікуваних частотах
    expected_frequencies[
        expected_frequencies == 0] = 0.1  # мінімальне значення для очікуваних частот, щоб уникнути ділення на нуль

    # Проведіть хі-квадрат тест
    chi_square_stat, p_value = stats.chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)

    print("Chi-square Statistic:", chi_square_stat)
    print("P-value:", p_value)

    # Висновок
    if p_value > 0.05:
        print('Не відхиляємо нульову гіпотезу, дані відповідають нормальному розподілу')
    else:
        print('Відхиляємо нульову гіпотезу, дані не відповідають нормальному розподілу')
