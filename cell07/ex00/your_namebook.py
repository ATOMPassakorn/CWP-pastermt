def array_of_names(persons):
    name = []
    for firstname, lastname in persons.items():
        name.append(f"{firstname.capitalize()} {lastname.capitalize()}")
    return name

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))