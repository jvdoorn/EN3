import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

if __name__ == '__main__':
    data = pd.read_csv("data/exp2dataset1.csv", delimiter=",")

    peaks, peak_heights = find_peaks(data['ch1'], distance=20, height=0)
    # peaks = pd.Series(data['time'], index=[peaks])
    peak_heights = peak_heights['peak_heights']

    peaks = np.array(data['timestamp'].take(peaks))[:5]
    peak_heights = np.array(peak_heights)[:5]
    peak_heights_ln = np.log(peak_heights)

    print(peaks)
    print(peak_heights)
    print(peak_heights_ln)

    slope, intercept, r_value, p_value, std_err = stats.linregress(peaks, peak_heights_ln)

    print(slope)
    print(std_err)
    print(-1 / slope)

    plt.plot(peaks, peak_heights_ln)
    plt.plot(peaks, peak_heights)
    plt.show()
