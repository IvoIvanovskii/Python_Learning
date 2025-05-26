import re

text = "Hello World!"
pattern =r"^Hello"
pattern2 = r"!$"

if re.match(pattern, text):
    print("tekstot pochnuva so Hello" )

if re.search(pattern2, text):
    print("tekstot zavrshuva so !" )

text2 = "Hello how are you"
pattern3 = r"\s"
new_text = re.sub(pattern3,"_", text2)
print(new_text)

text3 = "There are 15 apples and 20 oranges"
pattern4 = r"\d+"

match = re.findall(pattern4, text3)
print(match)
