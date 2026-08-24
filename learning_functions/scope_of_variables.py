discount=25 #variable declared in global scope so acccessible inside function

def calculate_temp(price):
    discount=30
    total_price=price-discount
    age=25 #variable declared in local scope so not acccessible outside function
    print(f"Total price is {total_price}")

calculate_temp(100)

# print(age) #age varaible no accessible in global scope

print(discount)