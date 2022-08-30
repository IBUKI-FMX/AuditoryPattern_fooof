#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
from scipy.io import loadmat, savemat

# Import the FOOOFGroup object
from fooof import FOOOFGroup

# Import utilities to manage frequency band definitions
from fooof.bands import Bands
from fooof.analysis import get_band_peak_fg

# Import simulation utilities for making example data
from fooof.sim.gen import gen_group_power_spectra
from fooof.sim.params import param_jitter

# Import plotting function for model parameters and components
from fooof.plts.periodic import plot_peak_fits, plot_peak_params
from fooof.plts.aperiodic import plot_aperiodic_params, plot_aperiodic_fits


# In[2]:


# Set up labels and colors for plotting
colors = ['#2400a8', '#00700b']
labels = ['REG', 'RAND']
# Set the number of 'subjects' per group
n_subjs = 19
# Define the frequency range for our simulations
freq_range = [1, 30]


# In[3]:


# Load the mat file 
data = loadmat('C:/Users/18146/Desktop/study/data/groupREG.mat')
# Unpack data from dictionary, and squeeze numpy arrays
freqs = np.squeeze(data['freq']).astype('float')
psds = np.squeeze(data['power']).astype('float')

# Transpose power spectra, to have the expected orientation for FOOOF
psds = psds.T 
# Initialize FOOOFGroup object
fgREG = FOOOFGroup(verbose=False,peak_width_limits=[1.0, 7.0])
# Parameterize neural power spectra
fgREG.report(freqs, psds, [1, 30])


# In[4]:


# Load the mat file 
data = loadmat('C:/Users/18146/Desktop/study/data/groupRAND.mat')

# Unpack data from dictionary, and squeeze numpy arrays
freqs = np.squeeze(data['freq']).astype('float')
psds = np.squeeze(data['power']).astype('float')

# Transpose power spectra, to have the expected orientation for FOOOF
psds = psds.T 
# Initialize FOOOFGroup object
fgRAND = FOOOFGroup()
# Fit the FOOOF model on all PSDs, and report
fgRAND.report(freqs, psds, [1, 30])


# In[5]:


# Define frequency bands of interest
bands = Bands({'theta' : [4, 8],
               'alpha' : [8, 15],})
# Extract alpha peaks from each group
gREG_alphas = get_band_peak_fg(fgREG, bands.alpha)
gRAND_alphas = get_band_peak_fg(fgRAND, bands.alpha)


# In[6]:


# Compare the peak parameters of alpha peaks between groups
plot_peak_params([gREG_alphas, gRAND_alphas], freq_range=bands.alpha,
                 labels=labels, colors=colors)


# In[7]:


# Compare the peak fits of alpha peaks between groups
plot_peak_fits([gREG_alphas, gRAND_alphas],
               labels=labels, colors=colors)


# In[8]:


# Extract the aperiodic parameters for each group
apsREG = fgREG.get_params('aperiodic_params')
apsRAND = fgRAND.get_params('aperiodic_params')
# Compare the aperiodic parameters between groups
plot_aperiodic_params([apsREG, apsRAND], labels=labels, colors=colors)


# In[9]:


# Plot the aperiodic fits for both groups
plot_aperiodic_fits([apsREG, apsRAND], freq_range,
                    control_offset=True, log_freqs=True,
                    labels=labels, colors=colors)


# In[10]:


# Plot the aperiodic fits for Group 1
plot_aperiodic_fits(apsREG, freq_range, control_offset=True)


# In[18]:





# In[ ]:




