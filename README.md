# ncrystal-notebooks

Python notebooks with examples, documentation, and tutorials for usage of NCrystal. You can either run the notebooks directly on your laptop (see below for instructions), or you can open them in google Colab by clicking the links (note: you must then click "save to Drive" before you can actually run any cells). Finally, you can also simply click the notebook links to browse them as static files directly on GitHub.

## The notebooks

### Notebooks providing a basic introduction to NCrystal

* [Introduction to NCrystal and the Python API](notebooks/ncrystal1_basic_01_Introduction_and_Python_API.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal1_basic_01_Introduction_and_Python_API.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * This is where you should start, to get a good solid foundation and learn about the basic NCrystal objects and what they provide.
* [NCrystal data infrastructure and standard data library](notebooks/ncrystal1_basic_02_Data_Infrastructure_and_StdDataLib.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal1_basic_02_Data_Infrastructure_and_StdDataLib.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this notebook we will discuss the NCrystal data library of predefined materials, as well as the general infrastructure for how such data is handled.
* [Using the builtin "MiniMC" framework for generating scatter patterns](notebooks/ncrystal1_basic_03_Scatter_patterns_with_the_builtin_MiniMC_framework.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal1_basic_03_Scatter_patterns_with_the_builtin_MiniMC_framework.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * Here we discuss how to generate simple scattering patterns using the builtin "MiniMC" framework, including effects of geometry and multiple scattering.
* [Using NCrystal as a backend for full-fledged Monte Carlo simulations](notebooks/ncrystal1_basic_04_NCrystal_as_backend_for_third_party_apps.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal1_basic_04_NCrystal_as_backend_for_third_party_apps.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * Here we discuss how NCrystal can be used as a physics engine in fully fledged frameworks like McStas, OpenMC, or Geant4.

### Notebooks related to creation of new material definitions

* [Creating materials and the NCMATComposer](notebooks/ncrystal2_advanced_01_Creating_materials_and_the_NCMATComposer.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal2_advanced_01_Creating_materials_and_the_NCMATComposer.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * This is for people wishing to put together new materials, introducing the `NCMATComposer` helper class and discussing the basic ingredients needed to define a material in NCrystal.
* [Importing crystal structures from CIF files or online databases](notebooks/ncrystal2_advanced_02_Import_crystal_structure_from_CIF_or_databases.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal2_advanced_02_Import_crystal_structure_from_CIF_or_databases.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * If your material has a crystal structure, you most likely will need to import that crystal structure from either a CIF file or an online database. We learn how to build upon the previous `NCMATComposer` work by loading such structures from external sources.
* [Adding phonon information](notebooks/ncrystal2_advanced_03_Add_phonon_info_with_PhononDOSAnalyser_with_QuantumEspresso_example.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal2_advanced_03_Add_phonon_info_with_PhononDOSAnalyser_with_QuantumEspresso_example.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * If your material is a solid (crystalline or amorphous), you need a phonon density of state (DOS) curve to get high-quality modelling of both inelastic and (perhaps surprisingly) elastic scattering. In this example, we go through all the steps of loading DOS curves produced by [Quantum Espresso](https://www.quantum-espresso.org/), and goes through the steps needed to clean them up a bit by removing unwanted artifacts that would otherwise prevent their usage, Finally, we use the `NCMATComposer` to combine both phonon DOS curves and crystal structures into a high quality NCMAT description of the material.

### Miscellaneous notebooks

* [Connecting phonon DOS curves to inelastic scattering ](notebooks/ncrystal2_advanced_04_VDOS2KNL_Connecting_phonons_to_inelastic_scattering.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/ncrystal2_advanced_04_VDOS2KNL_Connecting_phonons_to_inelastic_scattering.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this short notebook, we briefly mention the theoretical procedure used by NCrystal to expand a 1D phonon DOS curve to a 2D scattering kernel, and proceed to provide a few interactive widgets which can be used to understand this connection in practice.
* [Investigate sapphire filter](notebooks/misc/ncrystal_sapphire_filter.ipynb)
  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/misc/ncrystal_sapphire_filter.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * Notebook investigating transmission probability of a sapphire filter, and the effect of different ways of modelling.

### Contributed notebooks

Examples from the NEUWAVE-12 tutorial

* [NEUWAVE-12 Examples: Neutron filters](notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Neutron_filters_exercise.ipynb)  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Neutron_filters_exercise.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this example we will calculate cross-sections and neutron transmission through various polycrystalline and single-crystal filters and make comparisons to experimental data.
* [NEUWAVE-12 Examples: Sample container transmission exercise](notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Sample_container_transmission_exercise.ipynb)  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Sample_container_transmission_exercise.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this example we will calculate cross-sections and neutron transmission through various metals used for sample holders.
* [NEUWAVE-12 Examples: water / ice](notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Water_Ice.ipynb)  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Water_Ice.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this example we use NCrystal to see the wavelength dependence of the total cross section of light water and ice at different temperatures.
* [NEUWAVE-12 Examples: in-scattering](notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_In_scattering.ipynb)  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_In_scattering.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this example we will compute the in-scattering probability using different techiques, and see the effect it has in the wavelength dependent transmission.
* [NEUWAVE-12 Examples: extiction correction](notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Extinction_correction_exercise.ipynb)  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Extinction_correction_exercise.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * In this example it is shown how to calculate the coherent elastic cross-section by accessing hkl information in NCrystal. The cross-section is then modified with the extinction parameter from the Sabine model.
* [NEUWAVE-12 Examples: texture plugin](notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Installing_Plugins_Texture_exercise.ipynb)  <a target="_blank" href="https://colab.research.google.com/github/mctools/ncrystal-notebooks/blob/main/notebooks/contributed/NEUWAVE-12/NEUWAVE_12_Examples_Installing_Plugins_Texture_exercise.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
  * This exercise shows how to use the texture plugin, CrysText, together with NCrystal. In this example, the modifications to the coherent elastic cross-section are included in the NCrystal plugin.


## Instructions for running these notebooks.

### Browse on GitHub

Just click the names of the notebooks above to get a static view of the notebooks. This is can be convenient, but offers a non-interactive view. GUI widgets are not working, and cells containing a huge amount of output are shown expanded.

### Open in google Colab

Clicking the google Colab links above will open the notebooks in google Colab. To actually be able to execute cells, you will need a google account and then you must click "Copy to Drive" to get your own copy in the cloud that you can edit and run. One downside is that although GUI widgets work, matplotlib plots are only shown as static images and can therefore not be resized or zoomed interactively. Apart from that, this is a convenient way to run the notebooks without the need for any local installations.

### Run locally

Running locally is easy since everything can be installed via `pip` or `conda`. So either create a conda environment using the [conda.yml](conda.yml) environment file, or `pip install` all the required dependencies into a dedicated Python environment by (you can of course also `pip install` into your default Python environment if you are not the careful type):

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

In any case, you can then download the above notebooks (individually, or just clone or download the whole ncrystal-notebooks repo) and open the notebooks via the command `jupyter-lab nameofnotebook.ipynb`.

Note: although support for Windows is planned for EOY2024, it is by August 2024 still not possible to install NCrystal on Windows. So Windows users should either use the WSL, or simply run via google Colab as noted above.
