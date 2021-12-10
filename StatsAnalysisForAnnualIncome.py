import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the window size of the plot
plt.rcParams["figure.figsize"] = [15, 7]
plt.rcParams["figure.autolayout"] = True

# Set table headers
headers = ['Empty', 'Year', 'Income']

# Get the Data from the CSV file
data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/MedianUSIncome.csv', names=headers)

# Obtaining only the columns for Year and Income
df = pd.DataFrame(data)
df['Year'][7:] = pd.to_numeric(df['Year'][7:])  # Setting the Year column as numeric
df['Income'][7:] = pd.to_numeric(df['Income'][7:])  # Setting the Income column as numeric

# Setting the columns as numbers not objects
x = df['Year'][7:].astype(str).astype(float)
y = df['Income'][7:].astype(str).astype(float)

# Creating linear regression line
m, b = np.polyfit(x, y, 1)

print(np.corrcoef(x, y))  # Print the Correlation Coefficient

# Plotting the graph
plt.xticks(np.arange(min(x), max(x)+1, 2))
plt.yticks(np.arange(50000, 72500, 2500))
plt.scatter(x, y, color="none", edgecolor="b")
plt.plot(x, m*x + b, color="r")

# Setting up the look of the graph
plt.legend(["Median Household Income ($)", "Regression Line: y = " + str(m)+"x - " + str(abs(b))])
plt.xlabel("Year")
plt.ylabel("Median Household Income in US Dollars ($)")
plt.title("Median household income in the United States from 1990 to 2020")

plt.show() # Showing the graph
