# ncrystal-notebooks

Python notebooks with examples, documentation, and tutorials for usage of NCrystal.

## How to use them

The notebooks below include output cells, so apart from a few interactive widgets you can view them directly at GitHub by clicking the links to each notebook below. However, it might be more beneficial to clone the repository and run the notebooks interactively: clearing all outputs and executing line by line to see the effect.

To take full advantage of all the notebooks, you should not only have NCrystal available, but also the following Python packages:

```
numpy matplotlib spglib ase gemmi jupyterlab ipympl
```

### Install dependencies via conda

Everything (including NCrystal) can be installed using conda (or mamba) using the [conda.yml](conda.yml) environment file.


### Other options for installing dependencies

Alternatively, if you are not using conda, you can install NCrystal in [some other fashion](https://github.com/mctools/ncrystal/wiki/Get-NCrystal) and get the other dependencies via `python3 -mpip install ncrystal matplotlib ipympl numpy spglib ase gemmi jupyterlab` (it is planned to eventually support "pip install ncrystal" as well, but for the time being it is not available).

## The notebooks

### Notebooks providing a basic introduction to NCrystal

* [Basic1: Introduction to NCrystal and the Python API](notebooks/ncrystal1_basic_01_Introduction_and_Python_API.ipynb)
  * This is where you should start, to get a good solid foundation.
* [Basic2: Continued introduction to NCrystal](notebooks/ncrystal1_basic_02_Continued_introduction.ipynb)
  * Here we provide a helicopter view of various other subjects and features.

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
