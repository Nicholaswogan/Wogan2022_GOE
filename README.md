# Reproducing Wogan et al. (2022)

This repository contains the code for reproducing Wogan et al. (2022).


## Step 1: Install PhotochemPy v0.2.14

First, you will need to install PhotochemPy v0.2.14. You need a MacOS or Linux computer (Windows will not work). You will also need the `conda` package manager. You can install `conda` [here](https://www.anaconda.com/products/individual).

After installing `conda`, make a new environment with all dependencies

```sh
conda create -n photochempy -c conda-forge python=3.9 numpy=1.21 scipy=1.7 scikit-build=0.12 gfortran clang pathos=0.2.8 numba=0.55 jupyter matplotlib=3.5 matplotlib-label-lines=0.4.2
```

Note, `pathos`, `numba`, `jupyter`, `matplotlib` and `matplotlib-label-lines` are not PhotochemPy dependencies, but you will need them to reproduce plots later. Any recent versions of the above packages should work as of January 2022. I specify versions to make sure this code will still run many years into the future, as packages are updated.

Activate the environment, navigate to `PhotochemPy`, then install with setup.py

```sh
conda activate photochempy
cd PhotochemPy
python -m pip install --no-deps --no-build-isolation . -v
```

## Step 2: Run Great Oxidation Event simulations

Run the python script

```sh
python GOE_simulations.py
```

This will run simulations shown in Figure 2, 3, 4b, 4c, 4d, and Figure S3. Results of the simulation are stored in `<filename>.dat` binary files. All simulations are run in parallel using the number of available threads.

I omit scripts to run simulations shown in Figure 1 and Figure S1, because I did these model runs on a big computer with many cores. Reproducing with a normal computer would probably take about a week. However, Figure 1 and Figure SX simulations results are contained in the `ArcheanOutgassing_sweep` and `ModernValues_sweep` folders, respectfully. If you are really interested in these scripts, just contact me (wogan@uw.edu)

## Step 3: Plot the results

Run the python script `GOE_plots.py` to produce Figures 1, 2, 3, 4, S1, and S3. Figures are saved in `figures/` folder.

```sh
python GOE_plots.py
```

