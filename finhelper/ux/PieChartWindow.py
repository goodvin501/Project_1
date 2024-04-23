import matplotlib.pyplot as plt


class PieCahrt():

    def __init__(self, sizes, labels):
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        self.sizes = sizes
        self.labels = labels

        fig, ax = plt.subplots()
        ax.pie(self.sizes, labels=self.labels, autopct='%1.1f%%')

        plt.show()