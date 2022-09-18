import pandas as pd
from multifit import peak_detect, create_axis
import os
import glob
import matplotlib.pyplot as plt
from scipy import leastsq
import numpy as np

if __name__ == '__main__':
    data_path = os.path.abspath(os.environ['HOME'] + '/Documents/GaN/data/')    
    fig_path = os.path.abspath(os.environ['HOME'] + '/Documents/GaN/figures')

    calibration_data = pd.read_csv(data_path + '/calibration' + "/calibration.csv", header=0, sep=",")
    calibration_data['Column'] += 1

    max_vals, minvals = peak_detect(calibration_data['Intensity'], delta=50, x=calibration_data['Column'])
    wavelength_axis = create_axis(max_vals[:-5][:, 0])
   
    filenames = [i for i in os.listdir(data_path) if not os.path.isdir(os.path.join(data_path, i))]
    print(filenames)
    files = glob.glob(data_path + '/*.csv')    # spec_data = {}
    spec_data = [pd.read_csv(f, header=0, sep=',')['Intensity'] for f in files]
    for i in range(len(spec_data)):
        fig, ax = plt.subplots()
        ax.plot(wavelength_axis, spec_data[i])
        ax.set_xlabel('Wavelength (nm)')
        ax.set_ylabel('Intensity (arb. units)')
        ax.tick_params(left=False)
        ax.set_title(filenames[i][:-26])
        fig.savefig(fig_path + '/' + filenames[i][:-4])