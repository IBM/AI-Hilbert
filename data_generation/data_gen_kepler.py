# -*- coding: utf-8 -*-

import numpy as np
import regex as re
from scipy.optimize import minimize

def generate_data_kepler(num, noise_all = False, noise_target = True):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []
    for i in range(num):
        m1 = np.random.uniform(low=0.5, high=3.0)
        m2 = np.random.uniform(low=0.5, high=3.0)
        d = np.random.uniform(low=30.0, high=150.0)

        # std from binary stars dataset
        # p       m1      m2      d
        # 1089    0.54    0.5     107.27
        # 143.1   1.33    1.41    38.235
        # 930     0.88    0.82    113.769
        # 675.5   3.06    1.97    131.352

        if noise_all:
            m_std = 0.8048592656483493
            d_std = 35.42009818238792
            noise_m1 = np.random.normal(0, m_std, 1)[0] * noise_amount  # μ = 0, σ = 2, size = 1
            noise_m2 = np.random.normal(0, m_std, 1)[0] * noise_amount    # μ = 0, σ = 2, size = 1
            noise_d = np.random.normal(0, d_std, 1)[0] * noise_amount    # μ = 0, σ = 2, size = 1
            m1 = m1 + noise_m1
            m2 = m2 + noise_m2
            d = d + noise_d

        p = np.sqrt(d**3 / (m1 + m2))
        
        if noise_target:
            p_std = 358.68001756440236
            noise_p = np.random.normal(0, p_std, 1)[0] * noise_amount     # μ = 0, σ = 2, size = 1
            p = p + noise_p
            
        data.append([p, m1, m2, d])



    with open('data_kepler.dat', 'w') as f:
        for d in data:
            d_list = d[:-1]
            for d_i in d_list:
                # f.write(f'{d_i:.2f} ')
                f.write(f'{d_i} ')
            f.write('0.0 0.0') # for d1 and d2
            f.write('\n')

    with open('data_kepler_d.dat', 'w') as f:
        for d in data:
            #f.write(f'{d[-1]:.2f} ')
            f.write(f'{d[-1]} ')

    with open('data_kepler_n_points.dat', 'w') as f:
        f.write(f'{num}\n')


#------------------------------------------------------------------------------------------------------------------------

# DATA GENERATION

seed_p = np.random.randint(0, 2**32)
print('------> SEED: ', seed_p)
#seed_p = 1432406613 
np.random.seed(seed_p)

generate_data_kepler(20000, noise_all = False, noise_target = True)






