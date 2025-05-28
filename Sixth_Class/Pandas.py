import pandas as pd


dictionary={

    "Ime" : ["Ana", "Angela", "Tea", "Stefan"],
    "Prezime" : ["Markov", "Markovska", "Stoilkova", "Mirchevski"],
    "department " : ["IT", "HR", "Finance", "IT"],
    "e-mail" : ["ana@gmail.com", "Angela@gmail.com", "SOilkova@gmail.com", "Mirchesvski@gmail.com"], 
    "vozrast" : [19,22,25,35]

}

print(dictionary)

print("--------------------------------------------------------------------------------------------")

df = pd.DataFrame(dictionary)
print(df)

print("--------------------------------------------------------------------------------------------")

filter = (df["Prezime"] == "Markov") |( df["Prezime"] == "Mirchevski")
print(filter)

print("--------------------------------------------------------------------------------------------")

df = pd.read_csv('Products.csv')
print(df)

print("--------------------------------------------------------------------------------------------")

print(df.head(10))
print("--------------------------------------------------------------------------------------------")
print(df.tail(10))
print("--------------------------------------------------------------------------------------------")
print(df.columns)
print("--------------------------------------------------------------------------------------------")
print(df.info())
print("--------------------------------------------------------------------------------------------")
print(df.describe())
print("--------------------------------------------------------------------------------------------")
print(df['Genre'].value_counts())

print("--------------------------------------------------------------------------------------------")

print(df[df["Shipping_Cost"] > 3])
print("--------------------------------------------------------------------------------------------")

print(df[df["Product_ID"] == 274777])
print("--------------------------------------------------------------------------------------------")
print(df.duplicated(subset=["Category","Genre"]))
print("--------------------------------------------------------------------------------------------")

print(df.sort_values(by="Cost", ascending=False))
print("--------------------------------------------------------------------------------------------")

df1 = df[['Cost', 'Retail_Price']]
correlation = df[['Cost', 'Retail_Price']].corr()
print(correlation)
print("--------------------------------------------------------------------------------------------")


Ime = ["Ana", "Angela", "Tea", "Stefan"]
Prezime = ["Markov", "Markovska", "Stoilkova", "Mirchevski"]
poeni = [90, 48, 50, 83]

dict={"ime":Ime, "prezime":Prezime, "poeni":poeni}

df = pd.DataFrame(dict)
print(df)
df.to_csv('ucenici.csv', index=False, header=True )

df1 = df.query('poeni > 60 and prezime=="Markov"')

print(df1)

print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")




dictionary={

    "Ime" : ["Ana", "Angela", "Tea", "Stefan"],
    "Prezime" : ["Markov", "Markovska", "Stoilkova", "Mirchevski"],
    "department " : ["IT", "HR", "HR", "IT"],
    "e-mail" : ["ana@gmail.com", "Angela@gmail.com", "SOilkova@gmail.com", "Mirchesvski@gmail.com"], 
    "vozrast" : [19,22,25,35]

}

print(dictionary)

print("--------------------------------------------------------------------------------------------")

df = pd.DataFrame(dictionary)
print(df)

#Da se isprinta vo df site vraboteni vo IT

df1 = df[df['department '] == "IT"]
print(df1)

#Da se najde sredna vrednost na godini po department



df2 = df.groupby('department ')['vozrast'].mean()
print(df2)
