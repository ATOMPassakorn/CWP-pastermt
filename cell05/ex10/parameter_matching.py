import sys

parameter = len(sys.argv)-1
if parameter >= 1:
    text = str(input("What was the parameter? "))
    if text == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")