# Binary Classifier
Binary Classifier is a program and library for generating and classifying transient data.

```bash
$ python -m binaryclassifier 100
Transients:     50 / 50
Non-Transients: 50 / 50
```

## Tutorials
* [Emulator Main Tutorial](tutorial/EmulatorMain.ipynb)
* [Simple Classifier Tutorial](tutorial/SimpleClassifier.ipynb)

## Installation
### From Source
To build and install the package from the source code using Conda, run the following commands. You can skip some of the steps if you have already downloaded the source or have already setup a Conda environment.

```bash
git clone https://github.com/CSC380Team8/binary-classifier.git
cd binary-classifier

conda create -q --name binaryclassifier-environment python=2.7
source activate binaryclassifier-environment

conda build .
conda install binaryclassifier --use-local
```

Also be sure that you have `conda-build` installed, as it is needed to build the Conda package. You can install it by running `conda install conda-build` in your root environment.

## License
The source code of Binary Classifier is available under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.
