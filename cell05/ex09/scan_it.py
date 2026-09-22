import sys
import re

parameter = len(sys.argv)-1
if parameter == 2:
    keyword = sys.argv[1]
    target_string = sys.argv[2]
    matches = re.findall(re.escape(keyword), target_string)
    if matches:
        print(len(matches)+1)
    else:
        print("none")
else:
    print("none")