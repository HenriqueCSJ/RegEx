import re

phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

# search busca apenas a primeira ocorrência, findall busca todas

phone = """
Located in: Premier House
Address: 1401 Ocean Ave, Brooklyn, NY 11230, United States
Phone: +1 718-258-3419
Address: 4740 21st St, Long Island City, NY 11101, United States
Hours: Open ⋅ Closes 4:45PM
Independence Day (Observed) might affect these hours
Phone: +1 718-482-4900
Address: 22234 96th Ave, Jamaica, NY 11429, United States
Phone: +1 718-776-6080
Suggest an edit · Own this business?
Add missing information
Add business hours
"""

mo = re.search(phoneRegex, phone)
print(mo.group())

mo = re.findall(phoneRegex, phone)
mo

phoneRegex = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")

mo = re.findall(phoneRegex, phone)
mo

### Character classes
### \d = dígitos numéricos
### \D não um número
### \w qquer dígito que é letra, número ou underscore
### \W qquer dígito que NÃO é letra, número ou underscore
### \s qquer espaço, tab ou nova linha
### \s qquer NÃO espaço, tab ou nova linha

song = """        4 calling birds
        5 gold rings
        6 geese a-laying
        7 swans a-swimming
        8 maids a-milking
        9 ladies dancing
        10 lords a-leaping
        11 pipers piping
        12 drummers drumming"""

xmasRegex = re.compile(r"\d+\s\w+\s\w+-?\w+")

mo = re.findall(xmasRegex, song)
print(mo)


### Create own character classes

vowelRegex = re.compile(r"[aeiouAEIOU]")
lowLettersRegex = re.compile(r"[a-z]")
allLettersRegex = re.compile(r"[a-zA-Z]")
mo = re.findall(vowelRegex, song)
print(mo)

doublevowelRegex = re.compile(r"[aeiouAEIOU]{2}")
mo = re.findall(doublevowelRegex, song)
print(mo)

### Negative character classes

consonantsRegex = re.compile(r"[^aeiouAEIOU\s]")
mo = re.findall(consonantsRegex, song)
print(mo)