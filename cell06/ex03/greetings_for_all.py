def greetings(name="noble stranger"):
    if str(name).isnumeric():
        return print("Error! It was not a name.")
    else:
        return print(f"Hello, {name}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
