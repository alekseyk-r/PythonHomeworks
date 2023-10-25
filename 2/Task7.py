def shorten_name():
    full_name = input()
    first_name, middle_name, last_name = full_name.split()
    return f"{first_name} {middle_name[0]}.{last_name[0]}."

print(shorten_name())
