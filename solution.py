import pandas as pd
import numpy as np

import warnings

from hyppo.ksample import Energy, MMD, DISCO
from scipy.stats import laplace, norm, ks_2samp, anderson_ksamp, cramervonmises_2samp
from statsmodels.stats.weightstats import ztest
from statsmodels.distributions.empirical_distribution import ECDF

chat_id = 996494546 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = anderson_ksamp([x, y])
    
    return pval < 0.03 # Ваш ответ, True или False
