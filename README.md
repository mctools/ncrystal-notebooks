# ncrystal-notebooks

Python notebooks with examples, documentation, and tutorials for usage of NCrystal.

## How to use them

The notebooks below include output cells, so apart from a few interactive widgets you can view them directly at GitHub by clicking the links to each notebook below. However, it might be more beneficial to clone the repository and run the notebooks interactively: clearing all outputs and executing line by line to see the effect.

To take full advantage of all the notebooks, you should not only have NCrystal available, but also other Python packages. The full list is here:

```
ncrystal numpy matplotlib spglib ase gemmi jupyterlab ipympl
```

### Install dependencies via conda

Everything (including NCrystal) can be installed using conda (or mamba) using the [conda.yml](conda.yml) environment file.

### Install dependencies via pip

Everything (including NCrystal) can be installed using pip. Here is a full example which also creates a virtual environment to keep everything nice and clean (you can of course simply run the final of the shown commands if you prefer a less sandboxed installation):

```
#create the directory and step into it:
mkdir ./my_venv_for_ncrystal_notebooks/
cd ./my_venv_for_ncrystal_notebooks/
#create and activate the virtual environment:
python3 -mvenv ./venv
. ./venv/bin/activate
#install the packages:
python3 -mpip install ncrystal numpy matplotlib spglib ase gemmi jupyterlab ipympl
```

### Other options for installing dependencies

A final option is to build NCrystal manually. Refer to [the documentation](https://github.com/mctools/ncrystal/wiki/Get-NCrystal) for details. You will most likely have to add the other dependencies in another fashion (e.g. with pip or conda, or your systems package manager.

## The notebooks

### Notebooks providing a basic introduction to NCrystal


* [Basic1: Introduction to NCrystal and the Python API](notebooks/ncrystal1_basic_01_Introduction_and_Python_API.ipynb)
  * This is where you should start, to get a good solid foundation and learn about the basic NCrystal objects and what they provide.
* [Basic2: Using NCrystal as a backend for full-fledged Monte Carlo simulations](notebooks/ncrystal1_basic_02_NCrystal_in_other_apps_and_builtin_MiniMC.ipynb)
  * Here we discuss how NCrystal can be used as a physics engine in fully fledged frameworks like McStas, OpenMC, or Geant4.
  * We also try out NCrystal's own builtin "MiniMC" framework, which can be used to model neutron scattering patterns with effects of multiple scattering and geometry.
* [Basic3: NCrystal data infrastructure and standard data library](notebooks/ncrystal1_basic_03_Data_Infrastructure_and_StdDataLib.ipynb)
  * In this notebook we will discuss the NCrystal data library of predefined materials, as well as the general infrastructure for how such data is handled.

### Notebooks providing more advanced information

* [Advanced1: Creating materials and the NCMATComposer](notebooks/ncrystal2_advanced_01_Creating_materials_and_the_NCMATComposer.ipynb)
  * This is for people wishing to put together new materials, introducing the `NCMATComposer` helper class and discussing the basic ingredients needed to define a material in NCrystal.
* [Advanced2: Importing crystal structures from CIF files or online databases](notebooks/ncrystal2_advanced_02_Import_crystal_structure_from_CIF_or_databases.ipynb)
  * If your material has a crystal structure, you most likely will need to import that crystal structure from either a CIF file or an online database. We learn how to build upon the previous `NCMATComposer` work by loading such structures from external sources.
* [Advanced3: Adding phonon information](notebooks/ncrystal2_advanced_03_Add_phonon_info_with_PhononDOSAnalyser_with_QuantumEspresso_example.ipynb)
  * If your material is a solid (crystalline or amorphous), you need a phonon density of state (DOS) curve to get high-quality modelling of both inelastic and (perhaps surprisingly) elastic scattering. In this example, we go through all the steps of loading DOS curves produced by [Quantum Espresso](https://www.quantum-espresso.org/), and goes through the steps needed to clean them up a bit by removing unwanted artifacts that would otherwise prevent their usage, Finally, we use the `NCMATComposer` to combine both phonon DOS curves and crystal structures into a high quality NCMAT description of the material.
* [Advanced4: Connecting phonon DOS curves to inelastic scattering ](notebooks/ncrystal2_advanced_04_VDOS2KNL_Connecting_phonons_to_inelastic_scattering.ipynb)
  * In this short notebook, we briefly mention the theoretical procedure used by NCrystal to expand a 1D phonon DOS curve to a 2D scattering kernel, and proceed to provide a few interactive widgets which can be used to understand this connection in practice.

### Other notebooks

In the [notebooks/misc/](notebooks/misc/) subdirectory we aim to provide miscellaneous notebooks with a variety of recipes, examples, and tools.
