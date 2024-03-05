import re


pa=re.compile("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
inp="https://en.wikipedia.org/wiki/OK"
if pa.match(inp):
    print(f"{inp}  -  is proper")
else:
    print(f"{inp}  -   is not proper url ")