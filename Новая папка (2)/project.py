products = {
    'доска': 100,
    'балка': 250,
    'бревно': 300,
    'плита': 150
}

sales = []

def add_product(name, price):
    if name in products:
        print(f"Товар '{name}' уже существует.")
    else:
        products[name] = price
        print(f"Товар '{name}' добавлен с ценой {price} сом.")

def add_sale(product_name, quantity):
    if product_name not in products:
        print(f"Товар '{product_name}' не найден.")
        return

    sale_amount = products[product_name] * quantity
    sales.append({'product': product_name, 'quantity': quantity, 'total': sale_amount})
    print(f"Продано {quantity} шт. '{product_name}' на сумму {sale_amount} сом.")

def view_sales():
    print("Все продажи:")
    for sale in sales:
        print(f"{sale['quantity']} шт. '{sale['product']}' - {sale['total']} сом.")

def total_revenue():
    total = sum(sale['total'] for sale in sales)
    print(f"Общая выручка: {total} сом.")

add_product('фанера', 200)
add_product('гвоздь', 300)
add_sale('фанера', 10)
add_sale('доска', 7)
add_sale('балка', 3)
add_sale('гвоздь', 3)
view_sales()
total_revenue()
