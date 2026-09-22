import sys
import re

parameter = len(sys.argv)-1
text = ""
if parameter == 1:
    keyword = "z"
    target_string = sys.argv[1]
    matches = re.findall(re.escape(keyword), target_string)
    if matches:
        for i in matches:
           text+=i
        print(text)
    else:
        print("none")
else:
    print("none")