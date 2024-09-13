# PlotMagic

**PlotMagic** is a Python package designed to create advanced visualizations with minimal input, making data visualization effortless and accessible for users. Whether you're a beginner or an expert, **PlotMagic** generates high-quality plots with just a few lines of code.

## Features

- Simple Line Charts
- Bar Charts
- Scatter Plots
- Heatmaps
- Pie Charts
- Box Plots
- Histograms
- Pair Plots

# Usage
Here is how you can use the functions in PlotMagic to create various visualizations:


from plot_magic import viz

## Create a line chart
- data = [10, 20, 30, 25, 15]
- viz.line_chart(data)

## Create a bar chart
- categories = ['A', 'B', 'C']
- values = [15, 30, 45]
- viz.bar_chart(categories, values)

## Create a heatmap
- import numpy as np
- heatmap_data = np.random.rand(10, 10)
- viz.heatmap(heatmap_data)

## Create a scatter plot
- x = [1, 2, 3, 4, 5]
- y = [10, 15, 8, 12, 18]
- viz.scatter_plot(x, y)

## Create a pie chart
- labels = ['Category 1', 'Category 2', 'Category 3']
- sizes = [30, 45, 25]
- viz.pie_chart(labels, sizes)

## Visualizations

- Line Chart: Displays trends over time or categories.
- Bar Chart: Compares different categories with clear bar representation.
- Scatter Plot: Visualizes relationships between two variables.
- Heatmap: Displays data using color gradients, perfect for correlation matrices.
- Pie Chart: Shows proportion data in a circular layout.
- Box Plot: Displays data distribution based on quartiles.
- Histogram: Visualizes the frequency distribution of data.
- Pair Plot: Creates a grid of scatter plots for multivariate data analysis.

## Installation

You can install the package using `pip`:

```bash
pip install PlotMagic

