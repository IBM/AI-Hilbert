[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# AI-Hilbert
This repository contains the code and the data used for the experiments in the paper [Evolving Scientific Discovery by Unifying Data and
Background Knowledge with AI Hilbert](https://arxiv.org/abs/2308.09474).


AI Hilbert is an algebraic geometric based discovery system (based on Hilbert's NullStellensatz result), that enables the discovery of fundamental laws of nature (or non-physical systems) based on knowledge (articulated in formal logic terms) and experimental data.

**Visit our website** for a general overview, references, and some introductory videos: &rarr; [AI-Hilbert website](https://ai-hilbert.github.io) &larr;

<p align="center"> <img align="center" src="figures/system_high_level.png" alt="system overview"/> </p> 


## Code

The code is organized in 2 folders. One containing the problems studied in the main paper and one containing the problems studied in the paper appendix.

The folder `main_problems` contains:
* A notebook for the **Hagen-Poissuille Equation**, **Einstein’s Relativistic Time Dilation Law** and **Kepler’s Third Law of Planetary Motion**: [hagen_einstein_kepler[3.3][3.5][3.6].ipynb](main_problems/hagen_einstein_kepler[3.3][3.5][3.6].ipynb)
* A folder for the **revisited** problem of deriving **Kepler’s third law of planetary motion** from an incomplete background theory [kepler_with_missing_axioms[3.7]](main_problems/kepler_with_missing_axioms[3.7]) containing:
  * the corresponding notebook [kepler_with_missing_axioms[3.7].ipynb](main_problems/kepler_with_missing_axioms[3.7]/kepler_with_missing_axioms[3.7].ipynb)
  * the data used [data_kepler.dat](main_problems/kepler_with_missing_axioms[3.7]/data_kepler.dat), [data_kepler_d.dat](main_problems/kepler_with_missing_axioms[3.7]/data_kepler_d.dat), and [data_kepler_n_points.dat](main_problems/kepler_with_missing_axioms[3.7]/data_kepler_n_points.dat).
* A notebook for the **Radiated Gravitational Wave Power Equation**: [grav_waves[3.4].ipynb](main_problems/grav_waves[3.4].ipynb)
* A notebook for the **Bell Inequalities**: [bell_inequalities[3.8].ipynb](main_problems/bell_inequalities[3.8].ipynb)

The folder `suppl_material_problems` contains a notebook for each of the following problems:
* 6 problems from [FSRD]():
  * **I.15.10 FSRD**: [I_15_10.ipynb](suppl_material_problems/I_15_10.ipynb)
  * **I.27.6 FSRD**: [I_27_6.ipynb](suppl_material_problems/I_15_10.ipynb)
  * **I.34.8 FSRD**: [I_34_8.ipynb](suppl_material_problems/I_15_10.ipynb)
  * **I.43.16 FSRD**: [I_43_16.ipynb](suppl_material_problems/I_15_10.ipynb)
  * **II.10.9 FSRD**: [II_10_9.ipynb](suppl_material_problems/I_15_10.ipynb)
  * **II.34.2 FSRD**: [II_34_2.ipynb](suppl_material_problems/I_15_10.ipynb)
* 6 additional problems:
  * **Inelastic Relativistic Collision**: [inelastic.ipynb](suppl_material_problems/inelastic.ipynb)
  * **Decay of Pion into Muon and Neutrino**: [decay.ipynb](suppl_material_problems/decay.ipynb)
  * **Radiation Damping and Light Scattering**: [light.ipynb](suppl_material_problems/light.ipynb)
  * **Escape Velocity**: [escape.ipynb](suppl_material_problems/escape.ipynb)
  * **Hall Effect**: [hall.ipynb](suppl_material_problems/hall.ipynb)
  * **Compton Scattering**: [compton.ipynb](suppl_material_problems/compton.ipynb)


## How to cite

```
@misc{AI_Hilbert_2024,
      title={Evolving Scientific Discovery by Unifying Data and Background Knowledge with AI Hilbert}, 
      author={Ryan Cory-Wright and Cristina Cornelio and Sanjeeb Dash and Bachir El Khadir and Lior Horesh},
      year={2024},
      eprint={2308.09474},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
