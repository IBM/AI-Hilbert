# -*- coding: utf-8 -*-

import numpy as np
import regex as re
from scipy.optimize import minimize

np.random.seed(42)


# Inelastic Relativistic Collision # inelastic relativistic collision law
def generate_data_inelastic(num, noise_all = False, noise_target = False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []
    for i in range(num):
        m = np.random.uniform(low=0.5, high=2.0)
        v_c = np.random.uniform(low=0.5, high=1.0)
        c = 1
        m_c = ( (4 * m) / (np.sqrt(3)) )
        p_c =  (4 * m_c * v_c * c) / (np.sqrt(3 * (c**2 - v_c**2)))

        std = 0.833
        p_c_std = 22.098849327020748

        noise_m = np.random.normal(0, std, 1)[0] * noise_amount
        noise_v_c = np.random.normal(0, std, 1)[0] * noise_amount
        noise_p_c = np.random.normal(0, p_c_std, 1)[0] * noise_amount

        if noise_all:
            m = m + noise_m
            v_c = v_c + noise_v_c
            p_c = p_c + noise_p_c
        if noise_target:
            p_c = p_c + noise_p_c

        data.append([p_c, m, v_c, c])
    with open('data_inelastic.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')


# Decay of Pion into Muon and Neutrino # kinetic energy, and momentum when a pion at rest decays into a muon and a neutrino,
def generate_data_decay(num, noise_all = False, noise_target = False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []

    for i in range(num):
        m_pi = np.random.uniform(low=0.5, high=2.0)
        m_u = np.random.uniform(low=0.5, high=2.0)
        p_v = (m_pi**2 - m_u**2) / (2 * m_pi)

        std = 0.833
        p_v_std = 0.7711755220155624

        noise_m_pi = np.random.normal(0, std, 1)[0] * noise_amount
        noise_m_u = np.random.normal(0, std, 1)[0] * noise_amount
        noise_m_p = np.random.normal(0, std, 1)[0] * noise_amount
        noise_p_v = np.random.normal(0, p_v_std, 1)[0] * noise_amount

        if noise_all:
            m_pi = m_pi + noise_m_pi
            m_u = m_u + noise_m_u
            p_v = p_v + noise_p_v
        if noise_target:
            p_v = p_v + noise_p_v

        data.append([p_v, m_pi, m_u])

    with open('data_decay.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')


# Radiation Damping and Light Scattering # the light scattering law,
def generate_data_light(num, noise_all = False, noise_target = False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []

    for i in range(num):
        q_c = np.random.uniform(low=0.5, high=2.0)
        x_0 = np.random.uniform(low=0.5, high=2.0)
        w = np.random.uniform(low=0.5, high=2.0)
        pi = np.pi
        p = 4/3 * pi * q_c**2 * x_0**2 * w**4

        std = 0.833
        p_std = 94.05754932859698

        noise_q_c = np.random.normal(0, std, 1)[0] * noise_amount
        noise_x_0 = np.random.normal(0, std, 1)[0] * noise_amount
        noise_w = np.random.normal(0, std, 1)[0] * noise_amount
        noise_p = np.random.normal(0, p_std, 1)[0] * noise_amount

        if noise_all:
            q_c = q_c + noise_q_c
            x_0 = x_0 + noise_x_0
            w = w + noise_w
            p = p + noise_p
        if noise_target:
            p = p + noise_p

        data.append([p, q_c, x_0, w])

    with open('data_light.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')


# Escape Velocity # the minimal velocity that enables an object to overcome the gravitational pull of a plane,
def generate_data_escape(num, noise_all = False, noise_target = False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []
    for i in range(num):
        G = 1
        m = np.random.uniform(low=0.5, high=2.0)
        r = np.random.uniform(low=0.5, high=2.0)
        v_e = np.sqrt((2*G*m)/r)

        std = 0.833
        v_e_std = 0.4030474579043394

        noise_m = np.random.normal(0, std, 1)[0] * noise_amount
        noise_r = np.random.normal(0, std, 1)[0] * noise_amount
        noise_v_e = np.random.normal(0, v_e_std, 1)[0] * noise_amount

        if noise_all:
            m = m + noise_m
            r = r + noise_r
            v_e = v_e + noise_v_e
        if noise_target:
            v_e = v_e + noise_v_e

        data.append([v_e, G, m, r])

    with open('data_escape.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')



# Hall Effect #the Hall potential of an electrical conductor.
def generate_data_hall(num, noise_all = False, noise_target = False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []

    for i in range(num):
        h = np.random.uniform(low=0.5, high=2.0)
        l = np.random.uniform(low=0.5, high=2.0)
        I = np.random.uniform(low=0.5, high=2.0)
        b = np.random.uniform(low=0.5, high=2.0)
        N = np.random.uniform(low=0.5, high=2.0)
        q_e = np.random.uniform(low=0.5, high=2.0)
        u_h = (h * l * I * b) / (N * q_e)

        std = 0.833
        u_h_std = 2.2342097847869353

        noise_h = np.random.normal(0, std, 1)[0] * noise_amount
        noise_l = np.random.normal(0, std, 1)[0] * noise_amount
        noise_I = np.random.normal(0, std, 1)[0] * noise_amount
        noise_b = np.random.normal(0, std, 1)[0] * noise_amount
        noise_N = np.random.normal(0, std, 1)[0] * noise_amount
        noise_q_e = np.random.normal(0, std, 1)[0] * noise_amount
        noise_u_h = np.random.normal(0, u_h_std, 1)[0] * noise_amount

        if noise_all:
            h = h + noise_h
            l = l + noise_l
            I = I + noise_I
            b = b + noise_b
            N = N + noise_N
            q_e = q_e + noise_q_e
            u_h = u_h + noise_u_h
        if noise_target:
            u_h = u_h + noise_u_h

        data.append([u_h, h, l, I, b, N, q_e])

    with open('data_hall.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')



# Compton Scattering
def generate_data_compton(num, noise_all=False, noise_target=False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []
    for i in range(num):
        h = 1
        c = 1
        l_1 = np.random.uniform(low=0.5, high=2.0)
        m_e = 1
        cos_t = np.random.uniform(low=0.05, high=1.0)
        l_2  = l_1 + ((h * (1 - cos_t)) / (m_e * c ))

        std = 0.833
        l_2_std = 0.6148374283827321

        noise_l_1 = np.random.normal(0, std, 1)[0] * noise_amount
        noise_cos_t = np.random.normal(0, std, 1)[0] * noise_amount
        noise_l_2 = np.random.normal(0, l_2_std, 1)[0] * noise_amount

        if noise_all:
            l_1 = l_1 + noise_l_1
            cos_t = cos_t + noise_cos_t
            l_2 = l_2 + noise_l_2
        if noise_target:
            l_2 = l_2 + noise_l_2

        data.append([l_2, l_1, cos_t, h, c, m_e])

    with open('data_compton.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')


# Radiation Gravitational Wave Power
def generate_data_radiationGravitationalWavePower(num, noise_all=False, noise_target=False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []
    for i in range(num):
        m1 = np.random.uniform(low=0.5, high=2.0)
        m2 = np.random.uniform(low=0.5, high=2.0)
        r = np.random.uniform(low=0.5, high=2.0)
        G = 1
        c = 1
        p = - (32 * G**4 * m1**2 * m2**2 * (m1 + m2))/(5 * c**5 * r**5)

        std = 0.833
        p_std = 533.2198022034981

        noise_m1 = np.random.normal(0, std, 1)[0] * noise_amount
        noise_m2 = np.random.normal(0, std, 1)[0] * noise_amount
        noise_r = np.random.normal(0, std, 1)[0] * noise_amount
        noise_p = np.random.normal(0, p_std, 1)[0] * noise_amount

        if noise_all:
            m1 = m1 + noise_m1
            m2 = m2 + noise_m2
            r = r + noise_r
            p = p + noise_p
        if noise_target:
            p = p + noise_p
        data.append([p, m1, m2, r])
    with open('data_WavePower.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')


# Hagen Poiseuille equation
def generate_data_HagenPoiseuille(num, noise_all=False, noise_target=False):
    # amount of noise in the data = 1%
    noise_amount = 0.01
    data = []
    for i in range(num):
        p = np.random.uniform(low=0.5, high=2.0)
        l = np.random.uniform(low=0.5, high=2.0)
        mu = np.random.uniform(low=0.5, high=2.0)
        rad = np.random.uniform(low=0.5, high=5.0)
        r = np.random.uniform(low=0, high=rad)
        u = - (p * (r**2 - rad**2)) / ( 4 * l * mu)

        std = 0.833
        u_std = 2.300493890164562

        noise_p = np.random.normal(0, std, 1)[0] * noise_amount
        noise_l = np.random.normal(0, std, 1)[0] * noise_amount
        noise_mu = np.random.normal(0, std, 1)[0] * noise_amount
        noise_r = np.random.normal(0, std, 1)[0] * noise_amount
        noise_rad = np.random.normal(0, std, 1)[0] * noise_amount
        noise_u = np.random.normal(0, u_std, 1)[0] * noise_amount

        if noise_all:
            p = p + noise_p
            l = l + noise_l
            r = r + noise_r
            mu = mu + noise_mu
            rad = rad + noise_rad
            # while not (rad > r):
            #     rad = np.random.uniform(low=r, high=5.0)
            #     rad = rad + noise_rad
            u = u + noise_u
        if noise_target:
            u = u + noise_u

        data.append([u, p, l, mu, r, rad])

    with open('data_HagenPoiseuille.dat', 'w') as f:
        for d in data:
            for d_i in d:
                f.write(f'{d_i} ')
            f.write('\n')



generate_data_inelastic(10, noise_all = False, noise_target = True)
generate_data_decay(10, noise_all = False, noise_target = True)
generate_data_light(10, noise_all = False, noise_target = True)
generate_data_escape(10, noise_all = False, noise_target = True)
generate_data_hall(10, noise_all = False, noise_target = True)
generate_data_compton(10, noise_all = False, noise_target = True)
generate_data_radiationGravitationalWavePower(10, noise_all = False, noise_target = True)
generate_data_HagenPoiseuille(10, noise_all = False, noise_target = True)




