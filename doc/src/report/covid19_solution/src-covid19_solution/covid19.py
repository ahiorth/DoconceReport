#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def get_corona_data(location, data_file='../data/corona_data.dat'):
    """
    Extracts COVID-19 data for a specific location.

    :param location: The name of the location (case-sensitive).
    :param data_file: Path to file holding the COVID-19 data.
                      It is expected that columns of data are
                      separated by tabs, and that there is a
                      column called "LOCATION" with names of
                      each country, region, etc.
    :return: A pandas Data Frame with COVID-19 data for the
             input location.
    """
    df = pd.read_csv(data_file, sep='\t')
    try:
        df = df[df['LOCATION'] == location]
    except:
        print(f'Could not find data for location {location}...')
        return None
    return df
#---------

def plot_confirmed_cases(location, data_file='../data/corona_data.dat'):
    """
    Plots the number of confirmed COVID-19 cases for a specific
    location.

    :param location: The name of the location (case-sensitive).
    :param data_file: Path to file holding the COVID-19 data.
                      It is expected that columns of data are
                      separated by tabs, and that there is a
                      column called "LOCATION" with names of
                      each country, region, etc.
    :return: A matplotlib.pyplot.figure object.
    """
    # Get data
    df = get_corona_data(location, data_file)
    time = df['ELAPSED_TIME_SINCE_OUTBREAK'].to_numpy()
    confirmed = df['CONFIRMED'].to_numpy()

    # Make plot
    fig, ax = plt.subplots()
    ax.set_title(location)
    ax.grid()
    ax.set_xlabel('Time since initial outbreak (days)')
    ax.set_ylabel('Number of confirmed cases')
    ax.scatter(time, confirmed, color='black')
    return fig
#---------------

def compare_confirmed_cases_with_model(location, S0, I0, beta,
                                       data_file='../data/corona_data.dat'):
    """
    Plots the number of confirmed COVID-19 cases for a specific
    location.

    :param location: The name of the location (case-sensitive).
    :param S0: The initial number of susceptibles in the model.
    :param I0: The initial number of infected people in the model.
    :param beta: The model disease transmission rate parameter.
    :param data_file: Path to file holding the COVID-19 data.
                      It is expected that columns of data are
                      separated by tabs, and that there is a
                      column called "LOCATION" with names of
                      each country, region, etc.
    :return: A matplotlib.pyplot.figure object.
    """
    # Calculate S(t) and I(t) from the analytical solution
    t = np.linspace(0, 250, 251)
    St, It = calc_SI_model(t, S0, I0, beta)

    # Plot the data, and return the data
    fig = plot_confirmed_cases(location, data_file)
    # Add modelled I(t) to the same figure
    ax = fig.axes[0]
    ax.plot(t, It)
    return fig
 #------------