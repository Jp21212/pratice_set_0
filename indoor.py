def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("")

    result = convert(user_input)
    print(result)

if __name__ == "__main__":
    main()
