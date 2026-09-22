import sys

match sys.argv[1:]:
    case []:
        print("none")
    case args:
        for arg in args:
            if not arg.endswith("ism"):
                print(f"{arg}ism")