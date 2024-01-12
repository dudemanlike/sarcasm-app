def capitalize_every_other(input_string):
    result = ""
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

while True:
    user_input = input("Enter a string (type 'quit' to exit): ").strip()

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    output_text = capitalize_every_other(user_input)
    print("Result:", output_text)
