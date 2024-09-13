import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set some default styling
sns.set(style="whitegrid")

def line_chart(data, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
    """Generates a simple line chart."""
    plt.figure(figsize=(8, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def bar_chart(categories, values, title="Bar Chart"):
    """Generates a bar chart with given categories and values."""
    plt.figure(figsize=(8, 6))
    sns.barplot(x=categories, y=values)
    plt.title(title)
    plt.show()

def heatmap(data, title="Heatmap"):
    """Generates a heatmap for correlation matrices or any 2D data."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title(title)
    plt.show()

def scatter_plot(x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    """Generates a scatter plot."""
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='b', marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def pie_chart(labels, sizes, title="Pie Chart"):
    """Generates a pie chart with default settings."""
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title(title)
    plt.show()

def box_plot(data, title="Box Plot"):
    """Generates a box plot for visualizing distribution."""
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data)
    plt.title(title)
    plt.show()

def histogram(data, bins=10, title="Histogram"):
    """Generates a histogram to show data distribution."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.show()

def pairplot(data, title="Pair Plot"):
    """Generates a pair plot for multi-dimensional data."""
    sns.pairplot(data)
    plt.suptitle(title, y=1.02)
    plt.show()

# Sample usage function (can be removed in the final package)
def sample_usage():
    # Sample data
    categories = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 25]
    line_data = np.random.randn(100)
    scatter_x = np.random.rand(50)
    scatter_y = np.random.rand(50)
    correlation_matrix = np.corrcoef(np.random.randn(10, 5).T)

    # Visualizations
    bar_chart(categories, values)
    line_chart(line_data)
    scatter_plot(scatter_x, scatter_y)
    heatmap(correlation_matrix)
    pie_chart(categories, values)
    histogram(line_data)
