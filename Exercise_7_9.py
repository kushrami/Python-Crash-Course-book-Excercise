#No pastrami:
sandwich_orders = ['maxican','pastrami','aloo','pastrami','spicypoteto''pastrami','lulu']

finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print("We are out of pastrami.")
        continue
    print("I made your",sandwich,"sandwich")
    finished_sandwich.append(sandwich)

for sandwich in finished_sandwich:
    print(sandwich,"Sandwich is ready.")
