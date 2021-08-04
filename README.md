# WaveFrost
A hybrid inverse and multi-phase poromechanical approach to quantitatively estimate the physical and mechanical properties of a permafrost site. 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5159712.svg)](https://doi.org/10.5281/zenodo.5159712)

## Install 
The hybrid inverse and multi-phase poromechanical approach solver is implemented in Fortran and Python. The attached wrapper for Fortran code can only run in Linux system. For the Windows user, the Fortran code nees to be complied through Numpy f2py function. The following dependencies are required: 

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
