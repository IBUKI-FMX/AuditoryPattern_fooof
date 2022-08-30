#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
from scipy.io import loadmat, savemat


from fooof import FOOOF
import fooof
import numpy as np

from fooof.core.io import fname, fpath
from fooof.core.utils import nearest_ind
from fooof.core.modutils import safe_import, check_dependency
from fooof.sim.gen import gen_periodic
from fooof.utils.data import trim_spectrum
from fooof.utils.params import compute_fwhm
from fooof.plts.spectra import plot_spectrum
from fooof.plts.settings import PLT_FIGSIZES, PLT_COLORS
from fooof.plts.utils import check_ax, check_plot_kwargs
from fooof.plts.style import check_n_style, style_spectrum_plot
import matplotlib.pyplot as plt
# Import math Library
import numpy

plt = safe_import('.pyplot', 'matplotlib')


# In[27]:



data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum61.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freq'])
psd = np.squeeze(data['allP'])
# Initialize FOOOF object
fm1 = FOOOF()
# Fit the FOOOF model, and report
fm1.fit(freqs, psd, [1,80 ])



data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum62.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freq'])
psd = np.squeeze(data['allP'])
# Initialize FOOOF object
fm2 = FOOOF()
# Fit the FOOOF model, and report
fm2.fit(freqs, psd, [1, 80])

data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum63.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freq'])
psd = np.squeeze(data['allP'])
# Initialize FOOOF object
fm3 = FOOOF()
# Fit the FOOOF model, and report
fm3.fit(freqs, psd, [1, 80])



data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum64.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freq'])
psd = np.squeeze(data['allP'])
# Initialize FOOOF object
fm4 = FOOOF()
# Fit the FOOOF model, and report
fm4.fit(freqs, psd, [1, 80])

data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum65.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freq'])
psd = np.squeeze(data['allP'])
# Initialize FOOOF object
fm5 = FOOOF()
# Fit the FOOOF model, and report
fm5.fit(freqs, psd, [1, 80])



data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick/power_spectrum66.mat')

# Unpack data from dictioanry, and squeeze numpy arrays
freqs = np.squeeze(data['freq'])
psd = np.squeeze(data['allP'])
# Initialize FOOOF object
fm6 = FOOOF()
# Fit the FOOOF model, and report
fm6.fit(freqs, psd, [1, 80])


# In[ ]:


"""Plots for the FOOOF object.

Notes
-----
This file contains plotting functions that take as input a FOOOF object.
"""

import numpy as np

from fooof.core.io import fname, fpath
from fooof.core.utils import nearest_ind
from fooof.core.modutils import safe_import, check_dependency
from fooof.sim.gen import gen_periodic
from fooof.utils.data import trim_spectrum
from fooof.utils.params import compute_fwhm
from fooof.plts.spectra import plot_spectrum
from fooof.plts.settings import PLT_FIGSIZES, PLT_COLORS
from fooof.plts.utils import check_ax, check_plot_kwargs
from fooof.plts.style import check_n_style, style_spectrum_plot

plt = safe_import('.pyplot', 'matplotlib')

###################################################################################################
###################################################################################################

@check_dependency(plt, 'matplotlib')
def plot_fm(fm, plot_peaks=None, plot_aperiodic=True, plt_log=False, add_legend=True,
            save_fig=False, file_name=None, file_path=None,
            ax=None, plot_style=style_spectrum_plot,
            data_kwargs=None, model_kwargs=None, aperiodic_kwargs=None, peak_kwargs=None):
    """Plot the power spectrum and model fit results from a FOOOF object.

    Parameters
    ----------
    fm : FOOOF
        Object containing a power spectrum and (optionally) results from fitting.
    plot_peaks : None or {'shade', 'dot', 'outline', 'line'}, optional
        What kind of approach to take to plot peaks. If None, peaks are not specifically plotted.
        Can also be a combination of approaches, separated by '-', for example: 'shade-line'.
    plot_aperiodic : boolean, optional, default: True
        Whether to plot the aperiodic component of the model fit.
    plt_log : boolean, optional, default: False
        Whether to plot the frequency values in log10 spacing.
    add_legend : boolean, optional, default: False
        Whether to add a legend describing the plot components.
    save_fig : bool, optional, default: False
        Whether to save out a copy of the plot.
    file_name : str, optional
        Name to give the saved out file.
    file_path : str, optional
        Path to directory to save to. If None, saves to current directory.
    ax : matplotlib.Axes, optional
        Figure axes upon which to plot.
    plot_style : callable, optional, default: style_spectrum_plot
        A function to call to apply styling & aesthetics to the plot.
    data_kwargs, model_kwargs, aperiodic_kwargs, peak_kwargs : None or dict, optional
        Keyword arguments to pass into the plot call for each plot element.

    Notes
    -----
    Since FOOOF objects store power values in log spacing,
    the y-axis (power) is plotted in log spacing by default.
    """

    ax = check_ax(ax, PLT_FIGSIZES['spectral'])

    # Log settings - note that power values in FOOOF objects are already logged
    log_freqs = plt_log
    log_powers = False

    # Plot the data, if available
    if fm.has_data:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : PLT_COLORS['data'], 'linewidth' : 2.0,
             'label' : 'Original Spectrum' if add_legend else None})
        #plot_spectrum(fm.freqs, fm.power_spectrum, log_freqs, log_powers,
                      #ax=ax, plot_style=None, **data_kwargs)

    # Add the full model fit, and components (if requested)
    if fm.has_model:
        model_kwargs = check_plot_kwargs(model_kwargs,             {'color' : PLT_COLORS['model'], 'linewidth' : 3.0, 'alpha' : 0.5,
             'label' : 'Full Model Fit' if add_legend else None})
        plot_spectrum(fm.freqs, fm.fooofed_spectrum_, log_freqs, log_powers,
                      ax=ax, plot_style=None, **model_kwargs)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs = check_plot_kwargs(aperiodic_kwargs,                 {'color' : PLT_COLORS['aperiodic'], 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'Aperiodic Fit' if add_legend else None})
            plot_spectrum(fm.freqs, fm._ap_fit, log_freqs, log_powers,
                          ax=ax, plot_style=None, **aperiodic_kwargs)

        # Plot the periodic components of the model fit
        if plot_peaks:
            _add_peaks(fm, plot_peaks, plt_log, ax=ax, peak_kwargs=peak_kwargs)

    # Apply style to plot
    check_n_style(plot_style, ax, log_freqs, True)

    # Save out figure, if requested
    if save_fig:
        if not file_name:
            raise ValueError("Input 'file_name' is required to save out the plot.")
        plt.savefig(fpath(file_path, fname(file_name, 'png')))


def _add_peaks(fm, approach, plt_log, ax, peak_kwargs):
    """Add peaks to a model plot.

    Parameters
    ----------
    fm : FOOOF
        FOOOF object containing results from fitting.
    approach : {'shade', 'dot', 'outline', 'outline', 'line'}
        What kind of approach to take to plot peaks.
        Can also be a combination of approaches, separated by '-' (for example 'shade-line').
    plt_log : boolean, optional, default: False
        Whether to plot the frequency values in log10 spacing.
    ax : matplotlib.Axes
        Figure axes upon which to plot.
    peak_kwargs : None or dict
        Keyword arguments to pass into the plot call.
        This can be a flat dictionary, with plot keyword arguments,
        or a dictionary of dictionaries, with keys as labels indicating an `approach`,
        and values which contain a dictionary of plot keywords for that approach.

    Notes
    -----
    This is a pass through function, that takes a specification of one
    or multiple add peak approaches to use, and calls the relevant function(s).
    """

    # Input for kwargs could be None, so check if dict and typecast if not
    peak_kwargs = peak_kwargs if isinstance(peak_kwargs, dict) else {}

    # Split up approaches, in case multiple are specified, and apply each
    for cur_approach in approach.split('-'):

        try:

            # This unpacks kwargs, if it's embedded dictionaries for each approach
            plot_kwargs = peak_kwargs.get(cur_approach, peak_kwargs)

            # Pass through to the peak plotting function
            ADD_PEAK_FUNCS[cur_approach](fm, plt_log, ax, **plot_kwargs)

        except KeyError:
            raise ValueError("Plot peak type not understood.")


def _add_peaks_shade(fm, plt_log, ax, **plot_kwargs):
    """Add a shading in of all peaks.

    Parameters
    ----------
    fm : FOOOF
        FOOOF object containing results from fitting.
    plt_log : boolean
        Whether to plot the frequency values in log10 spacing.
    ax : matplotlib.Axes
        Figure axes upon which to plot.
    **plot_kwargs
        Keyword arguments to pass into the plot call.
    """

    kwargs = check_plot_kwargs(plot_kwargs,
                               {'color' : PLT_COLORS['periodic'], 'alpha' : 0.25})

    for peak in fm.get_params('gaussian_params'):

        peak_freqs = np.log10(fm.freqs) if plt_log else fm.freqs
        peak_line = fm._ap_fit + gen_periodic(fm.freqs, peak)

        ax.fill_between(peak_freqs, peak_line, fm._ap_fit, **kwargs)


def _add_peaks_dot(fm, plt_log, ax, **plot_kwargs):
    """Add a short line, from aperiodic to peak, with a dot at the top.

    Parameters
    ----------
    fm : FOOOF
        FOOOF object containing results from fitting.
    plt_log : boolean
        Whether to plot the frequency values in log10 spacing.
    ax : matplotlib.Axes
        Figure axes upon which to plot.
    **plot_kwargs
        Keyword arguments to pass into the plot call.
    """

    kwargs = check_plot_kwargs(plot_kwargs,
                               {'color' : PLT_COLORS['periodic'],
                                'alpha' : 0.6, 'lw' : 2.5, 'ms' : 6})

    for peak in fm.get_params('peak_params'):

        ap_point = np.interp(peak[0], fm.freqs, fm._ap_fit)
        freq_point = np.log10(peak[0]) if plt_log else peak[0]

        # Add the line from the aperiodic fit up the tip of the peak
        ax.plot([freq_point, freq_point], [ap_point, ap_point + peak[1]], **kwargs)

        # Add an extra dot at the tip of the peak
        ax.plot(freq_point, ap_point + peak[1], marker='o', **kwargs)


def _add_peaks_outline(fm, plt_log, ax, **plot_kwargs):
    """Add an outline of each peak.

    Parameters
    ----------
    fm : FOOOF
        FOOOF object containing results from fitting.
    plt_log : boolean
        Whether to plot the frequency values in log10 spacing.
    ax : matplotlib.Axes
        Figure axes upon which to plot.
    **plot_kwargs
        Keyword arguments to pass into the plot call.
    """

    kwargs = check_plot_kwargs(plot_kwargs,
                               {'color' : PLT_COLORS['periodic'],
                                'alpha' : 0.7, 'lw' : 1.5})

    for peak in fm.get_params('gaussian_params'):

        # Define the frequency range around each peak to plot - peak bandwidth +/- 3
        peak_range = [peak[0] - peak[2]*3, peak[0] + peak[2]*3]

        # Generate a peak reconstruction for each peak, and trim to desired range
        peak_line = fm._ap_fit + gen_periodic(fm.freqs, peak)
        peak_freqs, peak_line = trim_spectrum(fm.freqs, peak_line, peak_range)

        # Plot the peak outline
        peak_freqs = np.log10(peak_freqs) if plt_log else peak_freqs
        ax.plot(peak_freqs, peak_line, **kwargs)


def _add_peaks_line(fm, plt_log, ax, **plot_kwargs):
    """Add a long line, from the top of the plot, down through the peak, with an arrow at the top.

    Parameters
    ----------
    fm : FOOOF
        FOOOF object containing results from fitting.
    plt_log : boolean
        Whether to plot the frequency values in log10 spacing.
    ax : matplotlib.Axes
        Figure axes upon which to plot.
    **plot_kwargs
        Keyword arguments to pass into the plot call.
    """

    kwargs = check_plot_kwargs(plot_kwargs,
                               {'color' : PLT_COLORS['periodic'],
                                'alpha' : 0.7, 'lw' : 1.4, 'ms' : 10})

    ylims = ax.get_ylim()
    for peak in fm.get_params('peak_params'):

        freq_point = np.log10(peak[0]) if plt_log else peak[0]
        ax.plot([freq_point, freq_point], ylims, '-', **kwargs)
        ax.plot(freq_point, ylims[1], 'v', **kwargs)


def _add_peaks_width(fm, plt_log, ax, **plot_kwargs):
    """Add a line across the width of peaks.

    Parameters
    ----------
    fm : FOOOF
        FOOOF object containing results from fitting.
    plt_log : boolean
        Whether to plot the frequency values in log10 spacing.
    ax : matplotlib.Axes
        Figure axes upon which to plot.
    **plot_kwargs
        Keyword arguments to pass into the plot call.

    Notes
    -----
    This line representents the bandwidth (width or gaussian standard deviation) of
    the peak, though what is literally plotted is the full-width half-max.
    """

    kwargs = check_plot_kwargs(plot_kwargs,
                               {'color' : PLT_COLORS['periodic'],
                                'alpha' : 0.6, 'lw' : 2.5, 'ms' : 6})

    for peak in fm.gaussian_params_:

        peak_top = fm.power_spectrum[nearest_ind(fm.freqs, peak[0])]
        bw_freqs = [peak[0] - 0.5 * compute_fwhm(peak[2]),
                    peak[0] + 0.5 * compute_fwhm(peak[2])]

        if plt_log:
            bw_freqs = np.log10(bw_freqs)

        ax.plot(bw_freqs, [peak_top-(0.5*peak[1]), peak_top-(0.5*peak[1])], **kwargs)


# Collect all the possible `add_peak_*` functions together
ADD_PEAK_FUNCS = {
    'shade' : _add_peaks_shade,
    'dot' : _add_peaks_dot,
    'outline' : _add_peaks_outline,
    'line' : _add_peaks_line,
    'width' : _add_peaks_width
}


# In[ ]:


plot_peaks=None 
plot_aperiodic=True,
plt_log=False
add_legend=True
save_fig=False 
file_name=None 
file_path=None
ax=None
plot_style=style_spectrum_plot
data_kwargs=None 
model_kwargs=None 
aperiodic_kwargs=None
peak_kwargs=None
log_freqs = False
log_powers = False
if fm.has_data:
    data_kwargs = check_plot_kwargs(data_kwargs,         {'color' : PLT_COLORS['data'], 'linewidth' : 2.0,
         'label' : 'Original Spectrum' if add_legend else None})
    plot_spectrum(fm.freqs, fm.power_spectrum, log_freqs, log_powers,
                  ax=ax, plot_style=None, **data_kwargs)

# Add the full model fit, and components (if requested)
if fm.has_model:
    model_kwargs = check_plot_kwargs(model_kwargs,         {'color' : PLT_COLORS['model'], 'linewidth' : 3.0, 'alpha' : 0.5,
         'label' : 'Full Model Fit' if add_legend else None})
    plot_spectrum(fm.freqs, fm.fooofed_spectrum_, log_freqs, log_powers,
                  ax=ax, plot_style=None, **model_kwargs)

    # Plot the aperiodic component of the model fit
    if plot_aperiodic:
        aperiodic_kwargs = check_plot_kwargs(aperiodic_kwargs,             {'color' : PLT_COLORS['aperiodic'], 'linewidth' : 3.0, 'alpha' : 0.5,
             'linestyle' : 'dashed', 'label' : 'Aperiodic Fit' if add_legend else None})
        plot_spectrum(fm.freqs, fm._ap_fit, log_freqs, log_powers,
                      ax=ax, plot_style=None, **aperiodic_kwargs)

    # Plot the periodic components of the model fit
    if plot_peaks:
        _add_peaks(fm, plot_peaks, plt_log, ax=ax, peak_kwargs=peak_kwargs)
# Apply style to plot
check_n_style(plot_style, ax, log_freqs, True)


# In[ ]:


plot_fm(fm, plot_peaks=None, plot_aperiodic=True, plt_log=False, add_legend=True,
            save_fig=False, file_name=None, file_path=None,
            ax=None, plot_style=style_spectrum_plot,
            data_kwargs=None, model_kwargs=None, aperiodic_kwargs=None, peak_kwargs=None)


# In[3]:


for s in range(1,115):
# Load the mat file 
    data = loadmat('C:/Users/18146/Desktop/study/data/mat_pick_25overlap_600s/power_spectrum%d.mat'%(s))

    # Unpack data from dictioanry, and squeeze numpy arrays
    freqs = np.squeeze(data['freq'])
    psd = np.squeeze(data['allP'])
    # Initialize FOOOF object
    fm = FOOOF(max_n_peaks = 3)
    # Fit the FOOOF model, and report
    fm.report(freqs, psd, [1, 30])
    # Extract FOOOF results from object
    fooof_results = fm.get_results()

    # Convert FOOOF results to a dictionary
    #  This is useful for saving out as a mat file
    fooof_results_dict = fooof_results._asdict()
    # Save FOOOF results out to a mat file
    savemat('C:/Users/18146/Desktop/study/data/py_600_25over/power_spectrum%d.mat'%(s), fooof_results_dict)


# In[ ]:





# In[ ]:





# In[3]:


# Extract FOOOF results from object
fooof_results = fm.get_results()

# Convert FOOOF results to a dictionary
#  This is useful for saving out as a mat file
fooof_results_dict = fooof_results._asdict()


# In[4]:


# Save FOOOF results out to a mat file
savemat('C:/Users/18146/Desktop/study/foof/foof_rp_result6.mat', fooof_results_dict)


# In[5]:


help(FOOOF)


# In[6]:


help(fooof.plts)


# In[23]:


def plot_fm6(fm1,fm2,fm3,fm4,fm5,fm6, plot_peaks=None, plot_aperiodic=True, plt_log=False, add_legend=True,
            save_fig=False, file_name=None, file_path=None,
            ax=None, plot_style=style_spectrum_plot,
            data_kwargs=None, model_kwargs=None, aperiodic_kwargs=None, peak_kwargs=None):
    """Plot the power spectrum and model fit results from a FOOOF object.

    Parameters
    ----------
    fm : FOOOF
        Object containing a power spectrum and (optionally) results from fitting.
    plot_peaks : None or {'shade', 'dot', 'outline', 'line'}, optional
        What kind of approach to take to plot peaks. If None, peaks are not specifically plotted.
        Can also be a combination of approaches, separated by '-', for example: 'shade-line'.
    plot_aperiodic : boolean, optional, default: True
        Whether to plot the aperiodic component of the model fit.
    plt_log : boolean, optional, default: False
        Whether to plot the frequency values in log10 spacing.
    add_legend : boolean, optional, default: False
        Whether to add a legend describing the plot components.
    save_fig : bool, optional, default: False
        Whether to save out a copy of the plot.
    file_name : str, optional
        Name to give the saved out file.
    file_path : str, optional
        Path to directory to save to. If None, saves to current directory.
    ax : matplotlib.Axes, optional
        Figure axes upon which to plot.
    plot_style : callable, optional, default: style_spectrum_plot
        A function to call to apply styling & aesthetics to the plot.
    data_kwargs, model_kwargs, aperiodic_kwargs, peak_kwargs : None or dict, optional
        Keyword arguments to pass into the plot call for each plot element.

    Notes
    -----
    Since FOOOF objects store power values in log spacing,
    the y-axis (power) is plotted in log spacing by default.
    """
    f1 = 1
    f2 = 1
    f3 = 1
    f4 = 1
    f5 = 1
    f6 = 1
    ax = check_ax(ax, (20,20))

    # Log settings - note that power values in FOOOF objects are already logged
    log_freqs = True
    log_powers = False

    # Plot the data, if available
    if f1!=0:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : 'black', 'linewidth' : 2.0,
             'label' : 'REG5:Original Spectrum' if add_legend else None})
        plot_spectrum(fm1.freqs, fm1.power_spectrum, log_freqs, log_powers,
                      ax=ax, plot_style=None, **data_kwargs)
    if f2!=0:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : 'black', 'linewidth' : 2.0,
             'label' : 'REG10:Original Spectrum' if add_legend else None})
        plot_spectrum(fm2.freqs, fm2.power_spectrum, log_freqs, log_powers,
                      ax=ax, plot_style=None, **data_kwargs)
    if f3!=0:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : 'black', 'linewidth' : 2.0,
             'label' : 'REG20:Original Spectrum' if add_legend else None})
        plot_spectrum(fm3.freqs, fm3.power_spectrum, log_freqs, log_powers,
                      ax=ax, plot_style=None, **data_kwargs)
    if f4!=0:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : 'black', 'linewidth' : 2.0,
             'label' : 'RAND5:Original Spectrum' if add_legend else None})
        plot_spectrum(fm4.freqs, fm4.power_spectrum, log_freqs, log_powers,
                      ax=ax, plot_style=None, **data_kwargs)
    if f5!=0:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : 'black', 'linewidth' : 2.0,
             'label' : 'RAND10:Original Spectrum' if add_legend else None})
        plot_spectrum(fm5.freqs, fm5.power_spectrum, log_freqs, log_powers,
                      ax=ax, plot_style=None, **data_kwargs)
    if f6!=0:
        data_kwargs = check_plot_kwargs(data_kwargs,             {'color' : 'black', 'linewidth' : 2.0,
             'label' : 'RAND20:Original Spectrum' if add_legend else None})
        plot_spectrum(fm6.freqs, fm6.power_spectrum, log_freqs, log_powers,
                      ax=ax, plot_style=None, **data_kwargs)

    # Add the full model fit, and components (if requested)
    if f1!=0:
        if plot_peaks!= False:
            model_kwargs1 = check_plot_kwargs(model_kwargs,                 {'color' : 'red', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'label' : 'REG5 Full Fit' if add_legend else None})
            plot_spectrum(fm1.freqs, fm1.fooofed_spectrum_, log_freqs, log_powers,
                          ax=ax, plot_style=None, **model_kwargs1)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs1 = check_plot_kwargs(aperiodic_kwargs,                 {'color' : 'red', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'REG5 Aperiodic' if add_legend else None})
            plot_spectrum(fm1.freqs, fm1._ap_fit, log_freqs, log_powers,
                          ax=ax, plot_style=None, **aperiodic_kwargs1)
    if f2!=0:
        if plot_peaks!= False:
            model_kwargs2 = check_plot_kwargs(model_kwargs,                 {'color' : 'tab:orange', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'label' : 'REG10 Full Fit' if add_legend else None})
            plot_spectrum(fm2.freqs, fm2.fooofed_spectrum_, log_freqs, log_powers,
                          ax=ax, plot_style=None, **model_kwargs2)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs2 = check_plot_kwargs(aperiodic_kwargs,                 {'color' : 'tab:orange', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'REG10 Aperiodic' if add_legend else None})
            plot_spectrum(fm2.freqs, fm2._ap_fit, log_freqs, log_powers,
                          ax=ax, plot_style=None, **aperiodic_kwargs2)
    if f3!=0:
        if plot_peaks!= False:
            model_kwargs3 = check_plot_kwargs(model_kwargs,             {'color' : 'yellow', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'label' : 'REG20 Full Fit' if add_legend else None})
            plot_spectrum(fm3.freqs, fm3.fooofed_spectrum_, log_freqs, log_powers,ax=ax, plot_style=None, **model_kwargs3)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs3 = check_plot_kwargs(aperiodic_kwargs,                 {'color' : 'yellow', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'REG20 Aperiodic' if add_legend else None})
            plot_spectrum(fm3.freqs, fm3._ap_fit, log_freqs, log_powers,
                          ax=ax, plot_style=None, **aperiodic_kwargs3)
    if f4!=0:
        if plot_peaks!= False:
            model_kwargs4 = check_plot_kwargs(model_kwargs,                 {'color' : 'green', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'label' : 'RAND5 Full Fit' if add_legend else None})
            plot_spectrum(fm4.freqs, fm4.fooofed_spectrum_, log_freqs, log_powers,ax=ax, plot_style=None, **model_kwargs4)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs4 = check_plot_kwargs(aperiodic_kwargs,                 {'color' : 'green', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'RAND5 Aperiodic' if add_legend else None})
            plot_spectrum(fm4.freqs, fm4._ap_fit, log_freqs, log_powers,ax=ax, plot_style=None, **aperiodic_kwargs4)
    if f5 != 0:
        if plot_peaks!= False:
            model_kwargs5 = check_plot_kwargs(model_kwargs,                 {'color' : 'blue', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'label' : 'RAND10 Full Fit' if add_legend else None})
            plot_spectrum(fm5.freqs, fm5.fooofed_spectrum_, log_freqs, log_powers,ax=ax, plot_style=None, **model_kwargs5)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs5 = check_plot_kwargs(aperiodic_kwargs,                 {'color' : 'blue', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'RAND10 Aperiodic' if add_legend else None})
            plot_spectrum(fm5.freqs, fm5._ap_fit, log_freqs, log_powers,ax=ax, plot_style=None, **aperiodic_kwargs5)
    if f6!=0:
        if plot_peaks!= False:
            model_kwargs6 = check_plot_kwargs(model_kwargs,                 {'color' : 'purple', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'label' : 'RADN20 Full Fit' if add_legend else None})
            plot_spectrum(fm6.freqs, fm6.fooofed_spectrum_, log_freqs, log_powers,ax=ax, plot_style=None, **model_kwargs6)

        # Plot the aperiodic component of the model fit
        if plot_aperiodic:
            aperiodic_kwargs6 = check_plot_kwargs(aperiodic_kwargs,                 {'color' : 'purple', 'linewidth' : 3.0, 'alpha' : 0.5,
                 'linestyle' : 'dashed', 'label' : 'RAND20 Aperiodic' if add_legend else None})
            plot_spectrum(fm6.freqs, fm6._ap_fit, log_freqs, log_powers,
                          ax=ax, plot_style=None, **aperiodic_kwargs6)


    # Apply style to plot
    check_n_style(plot_style, ax, log_freqs, True)




# In[28]:


plot_fm6(fm1,fm2,fm3,fm4,fm5,fm6, plot_peaks= 1, plot_aperiodic=True, plt_log=False, add_legend=True,
        save_fig=False, file_name=None, file_path=None,
        ax=None, plot_style=style_spectrum_plot,
        data_kwargs=None, model_kwargs=None, aperiodic_kwargs=None, peak_kwargs=None)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




