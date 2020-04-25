# ML Workshop
Resources for Joey Hejna's ML Workshop.

### Links to the presentation:
Hack:Now Version: https://docs.google.com/presentation/d/196mQECjAryaqI1vNII3c4LrNM1H_Nl2sEt5w7Mhzp0s/edit?usp=sharing

Slightly Reduced: https://docs.google.com/presentation/d/1aDlGjjBSpZU91YW6_it-tSgQYDBZbD_R8_XGWcmSuoE/edit?usp=sharing

Original Full: https://docs.google.com/presentation/d/1cpxkLCDK6ikYC1ja6Txg4YWEo-P6sS7fNUQT6mA6y44/edit?usp=sharing

### Colab Notebook
I have made colab versions of the original workshop! Now you don't need to install anything locally, and can just use the "open in colab" links at the top of the workshop files marked "colab". AFterwards, you can make a copy to your drive.

**To Run the workshop notebook, click on `workshop.ipynb`, then open in Colab, then make a copy**.


### Local Setup

If you want to run everything locally, use these directions. To start, clone this repository. We'll be working out of it for the workshop.

To follow good practice, we'll be working out of virtual environment for the following reasons:
1. Leaving your global python installation the same
2. Ensuring that we are all working with the same exact packages
3. Prevent versioning conflicts. Specifically, we're using tensorflow 2.

#### Python Installation
1. Make sure you have python 3.6 or python 3.7 on your computer.
2. Make sure you have `pip` for `python3` installed on your computer. As I have both `python` and `python3` on my computer, for me this is `pip3`
3. Then, install the virtualenv package with `pip3 install virtualenv`. Ideally, this is the _only_ package you have on your system level python installation. You can figure out what pip packages you currently have installed by running `pip freeze`. Ideally, the output list should only contain `virtualenv`, though that's probably not the case.


#### Creating a Virtual Environment
1. Create a virtual environment called `venv` in the github repository by running `python3 -m virtualenv venv`. 
2. Activate the virtual environment by running `source venv/bin/activate`. You can always deactivate the virtual environment with `deactivate`.
3. Install all the packages for this workshop by running `pip install -r requirements.txt`. This will install all packages needed for the workshop!


#### Load Datasets
Finally, we're going to be using some datasets during the workshop and its best if you have them downloaded before hand.

To make sure the data sets are on your system, with your virtual environment active run `python load_datasets.py`.

You should see some datasets being downloaded through the Keras package. That's all you need to do!

#### Starting the Workshop
We will work out of jupyter notebooks. Run `jupyter notebook` in the virtual environment from the `mlworkshop` directory.
