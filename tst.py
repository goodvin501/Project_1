import matplotlib.pyplot as plt

class YourClass:
    def __init__(self, sizes, labels):
        self.sizes = sizes
        self.labels = labels
    
    def display_pie_chart(self):
        fig, ax = plt.subplots()
        ax.pie(self.sizes, labels=self.labels, autopct=lambda p: '({:.1f}%)'.format(p))
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

# Example usage:
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

your_instance = YourClass(sizes, labels)
your_instance.display_pie_chart()
