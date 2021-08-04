# WaveFrost
WaveFrost is a hybrid inverse and multi-phase poromechanical approach to quantitatively estimate the physical and mechanical properties of a permafrost site. 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5159712.svg)](https://doi.org/10.5281/zenodo.5159712)
 
## Dependencies 
The hybrid inverse and multi-phase poromechanical solver (WaveFrost) is implemented in Fortran and Python. The attached wrapper (ice_elastic.so) for Fortran code can only run in Linux system. The following dependencies are required in order to run WaveFrost : 

gfortran compiler:
```
$ sudo apt install gfortran-9
```

blas and lapack library: 

```
$ sudo apt-get install libblas-dev checkinstall 
$ sudo apt-get install libblas-doc checkinstall 
$ sudo apt-get install liblapacke-dev checkinstall 
$ sudo apt-get install liblapack-doc checkinstall
```

## Instruction
An example code (inversion.py) is given to show the estimation of mechanical properties of a permafrost site using R1 wave. The dispersion data for various sites can be found in the 'data' folder. The 'dispersion_R1.py' is used to calculate the theoretical dispersion relation of R1 wave. Similarly,  the 'dispersion_R2.py' is used to calculate the theoretical dispersion relation of R2 wave. The inversion analysis is perfomed based on the Neighborhood algorithm and detailed information can be found in https://github.com/keithfma/neighborhood. Users should run the 'inversion.py' multiple times with various random initial values to increase the robustness of the inversion results. 
