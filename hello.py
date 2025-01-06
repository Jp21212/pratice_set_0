"""name = input("whats your name? ").strip().title() #Ask user for name
print(f"hello, {name}") #Say hello

def hello():
    print (f"Hello, {name}")

hello()"""

def main():
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")

main()