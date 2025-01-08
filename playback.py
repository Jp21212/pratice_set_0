def main():

    print(add_dots())

def add_dots():
    text_input = input().split()
    spaced_input = '...'.join(text_input)
    return spaced_input

main()