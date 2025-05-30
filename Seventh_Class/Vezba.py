#ZADACA 1
# Procitaj gi podatocite so pandas, dodaj nova kolona
# so ime profit koja se presmetuva kako:
#Profit = Retail_Price - Cost - Shipping_Cost
#grupiraj go po genre
#presmetaj ja Prosechnata dobivka za sekoj genre
#vizueliziraj gi dobivkite po genre preku hist vo ista figura, mediana i mean

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Products.csv')
# print(df)
df['Profit'] = df["Retail_Price"] - df["Cost"] - df["Shipping_Cost"]
print(df)

midProfit = df.groupby("Genre")["Profit"].mean()
print(midProfit)

print("---------------------------------------------------------")

meadianProfit = df.groupby("Genre")["Profit"].median()
print(meadianProfit)

plt.subplot(1,2,1)
midProfit.plot(kind="bar")
plt.title("Profit po kategorija")
plt.xlabel("Genre")
plt.ylabel("Vrednost")

plt.subplot(1,2,2)
meadianProfit.plot(kind="bar")
plt.title("Profit po kategorija")
plt.xlabel("Genre")
plt.ylabel("medijana")


plt.show()