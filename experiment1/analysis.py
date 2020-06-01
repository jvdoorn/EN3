import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy.stats.stats import linregress

if __name__ == '__main__':
    for file_name in ["exp1", "exp1-1500", "exp1-1520", "exp1-1540", "exp1-1560", "exp1-1580", "exp1-1600"]:
        data = pd.read_csv("../data/experiment1/{0}.csv".format(file_name))

        peaks, peak_heights = find_peaks(data['max1'], height=data['max1'].mean())
        peaks = data['timestamp'].take(peaks)

        peak_heights = peak_heights['peak_heights']
        peak_heights_ln = np.log(peak_heights)

        slope, intercept, r_value, p_value, std_err = linregress(peaks, peak_heights_ln)

        plt.clf()
        plt.plot(data['timestamp'], data['max1'])
        plt.title("Data set: {0}".format(file_name))
        plt.ylabel("voltage IR-sensor (V)")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}.png".format(file_name))

        plt.clf()
        plt.plot(peaks, peak_heights)
        plt.title("Data set: {0}, extracted peaks".format(file_name))
        plt.ylabel("voltage IR-sensor (V)")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}-peaks.png".format(file_name))

        plt.clf()
        plt.plot(peaks, peak_heights_ln)
        plt.title("Data set: {0}, ln of extracted peaks".format(file_name))
        plt.ylabel("ln of voltage IR-sensor (ln(V))")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}-peaks-ln.png".format(file_name))

        plt.clf()
        plt.plot(peaks, peak_heights_ln, label="data")
        plt.plot(peaks, slope * peaks + intercept, label="lin. fit")
        plt.legend()
        plt.suptitle("Data set: {0}, decay fit".format(file_name))
        plt.title("(d.r. {0} std.err. {1})".format(1 / slope, std_err / (2 * slope ** 2)))
        plt.ylabel("ln of voltage IR-sensor (ln(V))")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}-decay.png".format(file_name))

    for file_name in ["exp2"]:
        data = pd.read_csv("../data/experiment1/{0}.csv".format(file_name))

        peaks, peak_heights = find_peaks(data['ch1'], height=data['ch1'].mean())
        peaks = data['timestamp'].take(peaks)

        peak_heights = peak_heights['peak_heights']
        peak_heights_ln = np.log(peak_heights)

        peaks = peaks[:7]
        peak_heights = peak_heights[:7]
        peak_heights_ln = np.log(peak_heights)

        slope, intercept, r_value, p_value, std_err = linregress(peaks, peak_heights_ln)

        plt.clf()
        plt.plot(data['timestamp'], data['ch1'], label="Channel 1")
        plt.plot(data['timestamp'], data['ch2'], label="Channel 2")
        plt.legend()
        plt.title("Data set: {0}".format(file_name))
        plt.ylabel("voltage (V)")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}.png".format(file_name))

        plt.clf()
        plt.plot(peaks, peak_heights)
        plt.title("Data set: {0}, extracted peaks".format(file_name))
        plt.ylabel("voltage (V)")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}-peaks.png".format(file_name))

        plt.clf()
        plt.plot(peaks, peak_heights_ln)
        plt.title("Data set: {0}, ln of extracted peaks".format(file_name))
        plt.ylabel("ln of voltage (ln(V))")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}-peaks-ln.png".format(file_name))

        plt.clf()
        print(peaks)
        plt.plot(peaks, peak_heights_ln, label="data")
        plt.plot(peaks, slope * peaks + intercept, label="lin. fit")
        plt.legend()
        plt.suptitle("Data set: {0}, decay fit".format(file_name))
        plt.title("(d.r. {0} std.err. {1})".format(-1 / slope, std_err / (2 * slope ** 2)))
        plt.ylabel("ln of voltage (ln(V))")
        plt.xlabel("timestamp (s)")
        plt.savefig("../output/experiment1/{0}-decay.png".format(file_name))
