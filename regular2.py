import re

message = "You can contact me at my personal number: 555-123-1234"

phoneRegExp = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo = phoneRegExp.search(message)
print(mo.group())

# Separando os padrões em grupos
phoneRegExp = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneRegExp.search(message)

print(mo.group(0)) # Tudo
print(mo.group(1))
print(mo.group(2))

# Buscando caracteres literais: escapados

message = "Call me at (123) 555-5555"

phoneRegExp = re.compile(r"\(\d\d\d\) \d\d\d-\d\d\d\d")
mo = phoneRegExp.search(message)
print(mo.group())

# Buscando vários ṕadrões ao mesmo tempo
phrase = "Batmobile lost a wheel!"

batRegEx = re.compile(r"Bat(man|mobile|copter)")
mo = batRegEx.search(phrase)

print(mo.group())
print(mo.group(1))