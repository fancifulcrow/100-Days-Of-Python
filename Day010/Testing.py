def format_name(f_name, l_name):
    """This is a Docstring. It uses 3 sets of double quotation marks.
    It can work across multiple lines.
    Every thing inside the docstring would show in the documentation of this function.
    Sometimes it is also used as multi-line comments."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("NGoZi", "agiLI"))
print(format_name(input("What is your first name?"), input("What is your last name?")))


# Functions can be nested apparently
def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)