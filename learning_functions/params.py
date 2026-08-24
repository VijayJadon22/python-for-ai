def check_weather(temp):
    if temp>25:
        print("Its Hot!")
    elif temp<=20:
        print("Its Moderate!")
    else:
        print("Its Cold!")

check_weather(22)

def greet_vijay(name):
    print(f"Hello {name}")

greet_vijay(name="jatin")
def greet_user(first_name,last_name):
    print(f"Hello {first_name} {last_name}")

greet_user("Jatin","Gahlot")

# def greet_default(first_name="Vijay",last_name="Jadon"):
#     print(f"Hello {first_name} {last_name}")

# greet_default()
def greet_default(last_name, first_name="Vijay"): #if there's no default value to last_name then it has to be in first place and the the default values one
    print(f"Hello {first_name} {last_name}")

greet_default("Singh")

def calculate_total(price,tax_rate,discount):
    tax=price*tax_rate
    total=price+tax-discount
    print(f"Total price is ${total}")

calculate_total(price=100,tax_rate=0.08,discount=10)

def calculate_price(price,tax,discount):
    tax_price=price*tax/100
    total_price=price+tax_price-discount
    print(f"Total price of the product is {total_price}")

calculate_price(1000,20,50)