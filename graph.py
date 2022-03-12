from numpy import float64
import pandas as pd
from datetime import date, datetime
import matplotlib.pyplot as plt

# not perfect because cpi package doesn't have march yet
inflation_date = date(2022, 2, 1)

prices = pd.read_csv("gas_prices_trimmed.csv", usecols = ['Date','Cost'], parse_dates=['Date'])

inflationAdjusted = [None] * len(prices)

# refresh cpi data
print("Updating cpi data, this might take a while...")
import cpi

dropRows = []

# inflation adjust costs
for index, row in prices.iterrows():
    if not row["Cost"]:
        # continue
        dropRows.append(index)
        continue
    dateVal = row["Date"].date()
    if dateVal < inflation_date:
        try:
            inflationAdjusted[index] = float(cpi.inflate(row["Cost"], dateVal, to=inflation_date))
        except:
            dropRows.append(index)
            continue
    else:
        # admittedly flawed workaround for not having march inflation data
        inflationAdjusted[index] = float(row["Cost"])

prices.drop(dropRows)

prices["Inflation Adjusted"] = inflationAdjusted

# plot the dataframe
prices.plot(x="Date", y=["Inflation Adjusted"], kind="line", figsize=(9, 8))

plt.title('Gas price (adjusted for inflation) over time', fontsize=24)

# Selecting the axis-X making the bottom and top axes False.
plt.xlabel(None)
plt.ylabel("Price per gallon\n(inflation adjusted $)", fontsize=18)

plt.legend().remove()

# Selecting the axis-X making the bottom and top axes False.
plt.tick_params(axis='x', which='both', bottom=False, top=False)
  
# Selecting the axis-Y making the right and left axes False
plt.tick_params(axis='y', which='both', right=False, left=False)

plt.ylim(ymin=0)
  
# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['left', 'right', 'top']:
    plt.gca().spines[pos].set_visible(False)

# print bar graph
plt.savefig('output.png')
    
