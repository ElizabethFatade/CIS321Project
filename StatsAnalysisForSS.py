import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the window size of the plot
plt.rcParams["figure.figsize"] = [7, 7]
plt.rcParams["figure.autolayout"] = True

# ---- FOR SUGAR AND SWEETS ----

# Set table headers
headers = ['Series ID', 'Year', 'Period', 'Label', 'Value']

# Get the Data from the CSV file
data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/SS.csv', names=headers)

# Obtaining only the columns for Year and Value
df = pd.DataFrame(data, columns=['Year', 'Value'])
df['Value'][2:] = pd.to_numeric(df['Value'][2:])  # Setting the Value column as numeric

w = 0.4  # Width of each bar of data
x = [2016, 2017, 2018, 2019, 2020]  # x value labels

# Obtaining the Value data for each social class
y_low = df['Value'][2:7]
y_mid = df['Value'][7:12]
y_up = df['Value'][12:]

# Creating each bar for each social class
bar1 = np.arange(0, 10, 2)
bar2 = [i+w for i in bar1]
bar3 = [i+(2*w) for i in bar1]

# Plotting the bars
plt.bar(bar1, y_low, w, label="lower")
plt.bar(bar2, y_mid, w, label="middle")
plt.bar(bar3, y_up, w, label="upper")

# Setting up the look of the graph
plt.legend(["Lower Class", "Middle Class", "Upper Class"])
plt.xlabel("Year")
plt.ylabel("Expenditure in US Dollars($)")
plt.title("Money Spent on Sugar and Sweets")
plt.xticks(bar1+w, x)

plt.show()  # Showing the graph

# ---- FOR MEAT, POULTRY, FISH AND EGGS ----
"""data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/MPFE.csv', names=headers)
df = pd.DataFrame(data, columns=['Year', 'Value'])

df['Value'][2:] = pd.to_numeric(df['Value'][2:])

w = 0.4
x = [2016, 2017, 2018, 2019, 2020]

y_low = df['Value'][2:7]
y_mid = df['Value'][7:12]
y_up = df['Value'][12:]

bar1 = np.arange(0, 10, 2)
bar2 = [i+w for i in bar1]
bar3 = [i+(2*w) for i in bar1]

plt.bar(bar1, y_low, w, label="lower")
plt.bar(bar2, y_mid, w, label="middle")
plt.bar(bar3, y_up, w, label="upper")

plt.legend(["Lower Class", "Middle Class", "Upper Class"])
plt.xlabel("Year")
plt.ylabel("Expenditure in US Dollars($)")
plt.title("Money Spent on Meat, Poultry, Fish and Eggs")
plt.xticks(bar1+w, x)

plt.show()"""

# ---- FOR DAIRY ----
"""data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/DAIRY.csv', names=headers)
df = pd.DataFrame(data, columns=['Year', 'Value'])

df['Value'][2:] = pd.to_numeric(df['Value'][2:])

w = 0.4
x = [2016, 2017, 2018, 2019, 2020]

y_low = df['Value'][2:7]
y_mid = df['Value'][7:12]
y_up = df['Value'][12:]

bar1 = np.arange(0, 10, 2)
bar2 = [i+w for i in bar1]
bar3 = [i+(2*w) for i in bar1]

plt.bar(bar1, y_low, w, label="lower")
plt.bar(bar2, y_mid, w, label="middle")
plt.bar(bar3, y_up, w, label="upper")

plt.legend(["Lower Class", "Middle Class", "Upper Class"])
plt.xlabel("Year")
plt.ylabel("Expenditure in US Dollars($)")
plt.title("Money Spent on Dairy Products")
plt.xticks(bar1+w, x)

plt.show()"""

# ---- FOR FRESH FRUIT ----
"""data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/FRUIT.csv', names=headers)
df = pd.DataFrame(data, columns=['Year', 'Value'])

df['Value'][2:] = pd.to_numeric(df['Value'][2:])

w = 0.4
x = [2016, 2017, 2018, 2019, 2020]

y_low = df['Value'][2:7]
y_mid = df['Value'][7:12]
y_up = df['Value'][12:]

bar1 = np.arange(0, 10, 2)
bar2 = [i+w for i in bar1]
bar3 = [i+(2*w) for i in bar1]

plt.bar(bar1, y_low, w, label="lower")
plt.bar(bar2, y_mid, w, label="middle")
plt.bar(bar3, y_up, w, label="upper")

plt.legend(["Lower Class", "Middle Class", "Upper Class"])
plt.xlabel("Year")
plt.ylabel("Expenditure in US Dollars($)")
plt.title("Money Spent on Fresh Fruit")
plt.xticks(bar1+w, x)

plt.show()"""

# ---- FOR FRESH VEGETABLES ----
"""data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/VEG.csv', names=headers)
df = pd.DataFrame(data, columns=['Year', 'Value'])

df['Value'][2:] = pd.to_numeric(df['Value'][2:])

w = 0.4
x = [2016, 2017, 2018, 2019, 2020]

y_low = df['Value'][2:7]
y_mid = df['Value'][7:12]
y_up = df['Value'][12:]

bar1 = np.arange(0, 10, 2)
bar2 = [i+w for i in bar1]
bar3 = [i+(2*w) for i in bar1]

plt.bar(bar1, y_low, w, label="lower")
plt.bar(bar2, y_mid, w, label="middle")
plt.bar(bar3, y_up, w, label="upper")

plt.legend(["Lower Class", "Middle Class", "Upper Class"])
plt.xlabel("Year")
plt.ylabel("Expenditure in US Dollars($)")
plt.title("Money Spent on Fresh Vegetables")
plt.xticks(bar1+w, x)

plt.show()"""

# ---- FOR GRAINS ----
"""data = pd.read_csv('/Users/elizabethfatade/Documents/statsdata/GRAINS.csv', names=headers)
df = pd.DataFrame(data, columns=['Year', 'Value'])

df['Value'][2:] = pd.to_numeric(df['Value'][2:])

w = 0.4
x = [2016, 2017, 2018, 2019, 2020]

y_low = df['Value'][2:7]
y_mid = df['Value'][7:12]
y_up = df['Value'][12:]

bar1 = np.arange(0, 10, 2)
bar2 = [i+w for i in bar1]
bar3 = [i+(2*w) for i in bar1]

plt.bar(bar1, y_low, w, label="lower")
plt.bar(bar2, y_mid, w, label="middle")
plt.bar(bar3, y_up, w, label="upper")

plt.legend(["Lower Class", "Middle Class", "Upper Class"])
plt.xlabel("Year")
plt.ylabel("Expenditure in US Dollars($)")
plt.title("Money Spent on Grains")
plt.xticks(bar1+w, x)

plt.show()"""