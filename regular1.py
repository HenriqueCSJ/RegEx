import re

message = "Call me 415-555-1233 tomorrow, or at 415-555-1234 at my office during commercial time"

phoneNumRegEx = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegEx.search(message)

print(mo.group())
