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
An example code (inversion.py) is given to show the estimation of mechanical properties of a permafrost site using R1 wave. Users can simply run following command to load the field measurement, define loss function and run inversion analysis for the estimation of the permafrost properties. 
```
$ python inversion.py
```

The dispersion data for various sites can be found in the 'data' folder. The file in the 'data' folder is named based on R1 and R2 wave in various sites (for example, the dispersion data for R1 wave in site 1 is name as site1_R1.csv). To use a different dataset, users can change the file name accordingly in line 10 and 11 of inversion.py. 

```
disp1 = np.loadtxt('data/site1_R2.csv')  
disp2 = np.loadtxt('data/site1_R1.csv')  
```

The aim function is defined based R2 wave in the case of the estimation of physical properties of permafrost. On the other hand, the aim function is defined based R1 wave in the case of the estimation of mechanical properties of permafrost. For instance, to define aim function based on R2 wave, users need to change line 37 of Python script 'inversion.py' into: 

```
loss11 = np.abs(yt1- y_data1)
```

Then the loss function can be defined in line 43 of Python script 'inversion.py' as: 

```
loss = np.sqrt(np.sum(loss11**2))
```

Similarly, to define aim function based on R1 wave, uses can write following code in the line line 37 and 47 of Python script 'inversion.py': 

```
loss22 = np.abs(yt2- y_data2)
```

```
loss = np.sqrt(np.sum(loss22**2))
```


The 'dispersion_R1.py' is used to calculate the theoretical dispersion relation of R1 wave. Similarly,  the 'dispersion_R2.py' is used to calculate the theoretical dispersion relation of R2 wave. Users need to place these file Python scripts in the same directory as the Python script 'inversion.py'. The inversion analysis is perfomed based on the Neighborhood algorithm and detailed information can be found in https://github.com/keithfma/neighborhood. Users should run the 'inversion.py' multiple times with various random initial values to increase the robustness of the inversion results. 
