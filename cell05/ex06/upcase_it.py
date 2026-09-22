import sys

parameter = len(sys.argv)-1
if parameter >= 1:
    print(sys.argv[1].upper())
else:
    print("none")