cost = 1000
discount = 20
quantity = 3

total_cost = cost * quantity

print("Стоимость вашего заказа: ",
      total_cost - ((total_cost / 100) * discount), "рублей")
