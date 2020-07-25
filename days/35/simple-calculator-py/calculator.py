def main(value):
    s = value.split("*")
    print(s)
    operations = ["(", "-", "^", "*", "/", "+", "-"]

    while value not in operations:
        if "(" in value:
            brackets = calculate_values_in_brackets(value)
            replace_nums_in_brackets_with_value = 1
        if "-" in value:
            pass
        if "^" in value:
            pass
        if "*" in value:
            pass


def calculate_values_in_brackets(value):
    pass
