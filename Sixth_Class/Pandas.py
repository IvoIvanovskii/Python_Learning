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

