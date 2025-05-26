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
pattern4 = r"\d{2}"

match = re.findall(pattern4, text3)
print(match)

text4 = "Mojot telefonski broj e 078-553-183"
pattern5 = r"\d{3}-\d{3}-\d{3}"
match = re.search(pattern5, text4)
print(match)
print(match.group())

text5 = "Alice and Bob went to New Yourk"
pattern6 = r"\b[A-Z][a-zA-Z]*\b"
match = re.findall(pattern6, text5)
print(match)

text6 = "apples, pineapples, strawberry, banana"
pattern7 = r"[a-z]+"
match = re.findall(pattern7, text6)
print(match)