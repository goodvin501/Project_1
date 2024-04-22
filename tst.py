import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

labels = ['Walk', 'Talk', 'Sleep', 'Work']
sizes = [23, 45, 12, 20]
colors = ['red', 'blue', 'green', 'yellow']

patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')

plt.show()