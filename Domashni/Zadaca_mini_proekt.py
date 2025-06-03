import pandas as pd
import re
import matplotlib.pyplot as plt


df = pd.read_excel("Company.xlsx")


def fix_id(value):
    value = re.sub(r'\D', '', str(value))  
    if len(value) < 13:
        return value.zfill(13) 
    else:
        return value[-13:]  

df['ID'] = df['ID'].apply(fix_id)


def fix_phone(value):
    digits = re.sub(r'\D', '', str(value))
    if len(digits) >= 7:
        return '07' + digits[-7:]
    return pd.NA  

df['Phone'] = df['Phone'].apply(fix_phone)

df['Product'] = df['Product'].apply(lambda x: re.sub(r'\D', '', str(x)))

def fix_gender(g):
    g = str(g).strip().upper()
    if g.startswith("M"):
        return "M"
    elif g.startswith("F"):
        return "F"
    else:
        return pd.NA

df['Gender'] = df['Gender'].apply(fix_gender)

def convert_salary(val):
    try:
        val = str(val).replace(",", "").replace("$", "").strip()    
        val = float(val)
        return round(val * 61.5)
    except:
        return pd.NA 



df['Salary'] = df['Salary'].apply(convert_salary)

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, str(email)) is not None

df['Email'] = df['Email'].apply(lambda x: x if is_valid_email(x) else pd.NA)

avg_salary_by_dept = df.groupby('Department')['Salary'].mean().round(2)

print("\Prosecna plata po Department:")
print(avg_salary_by_dept)

plt.subplot(1,3, 1)
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index)
plt.title("Odnosot po Gender")

plt.subplot(1, 3, 2)
dept_counts = df['Department'].value_counts()
plt.pie(dept_counts, labels=dept_counts.index)
plt.title("Sektorski vraboteni")

plt.subplot(1, 3, 3)
plt.bar(avg_salary_by_dept.index, avg_salary_by_dept.values, color='skyblue')
plt.title("Prosecna plata po sektor")
plt.ylabel("Plata vo denari")

plt.show()


df.to_csv("Company1.csv")