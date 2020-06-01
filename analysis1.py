import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv("data/dataset_1.csv")

    plt.plot(data['timestamp'], data['min1'])
    plt.show()



    print(data)
