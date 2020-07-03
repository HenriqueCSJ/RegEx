import re

phrase = "THe adventures of Batman"

# 0 ou 1 ocorrências (?)
batRegEx = re.compile(r"Bat(wo)?man")
mo = batRegEx.search(phrase)

print(mo.group())

phrase = "THe adventures of Batwoman"

mo = batRegEx.search(phrase)
print(mo.group())

mo = batRegEx.search("The adventures of Batwowowoman")
mo == None

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneRegex.search("Call me tomorrow at my number 123-456-7890")
print(mo.group())

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo = phoneRegex.search("Call me tomorrow at my number 456-7890")
print(mo.group())

# Zero or more times (*)

batRegEx = re.compile(r"Bat(wo)*man")
mo = batRegEx.search("The adventures of Batwowowoman")
print(mo.group())

# 1 or more (+)

batRegEx = re.compile(r"Bat(wo)+man")

mo = re.search(batRegEx, "The adventures of Batwoman")
print(mo.group())

# Specific number of repetitions (){x}

haRegex = re.compile(r"(ha){3}")
mo = re.search(haRegex, "He said 'hahaha' and left the building")
print(mo.group())

phoneRegex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?( )?){4}")
mo = re.search(phoneRegex, "Hi, please, call this numbers: 123-456-7890, 456-0987 123-123-1234,555-555-5555")
print(mo.group())

# at least X, at max Y (){X, Y}

phoneRegex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?( )?){3,4}")
mo = re.search(phoneRegex, "Hi, please, call this numbers: 123-456-7890, 456-0987 123-123-1234,555-555-5555")
print(mo.group())

"""
During a search, regex in python is greedy by default. That means
that during a (){3,5} search, python tries to match 5 ocurrences always.
"""

# Non greedy (){3,5}?

### This is greedy
digitsRegex = re.compile(r"(\d){3,5}")
mo = re.search(digitsRegex, "1234567890")
print(mo.group())

### This is not greedy
digitsRegex = re.compile(r"(\d){3,5}?")
mo = re.search(digitsRegex, "1234567890")
print(mo.group())

