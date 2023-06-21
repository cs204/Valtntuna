def convert_to_snake_case(variable_name):
    snake_case = ""
    for char in variable_name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip("_")

def main():
    camel_case = input("Верблюжий стиль: ")
    snake_case = convert_to_snake_case(camel_case)
    print(snake_case)
main()
