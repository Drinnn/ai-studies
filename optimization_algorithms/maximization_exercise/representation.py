products = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]

available_space = 3


def print_shipped_products(schedule):
    total_price = 0
    space_occupied = 0
    print('Shipped products:')
    print('=================')
    for i in range(len(products)):
        if schedule[i] == 1:
            product_name = products[i][0]
            product_shipping_size = products[i][1]
            product_price = products[i][2]
            space_occupied += product_shipping_size
            total_price += product_price
            print('{} occupying {} - R${}'.format(product_name,
                                                  product_shipping_size, product_price))
    print('=================')
    print('Space occupied: {}'.format(space_occupied))
    print('Total price: R${}'.format(total_price))


def fitness_function(schedule):
    cost = 0
    shipping_space = 0
    for i in range(len(schedule)):
        if schedule[i] == 1:
            cost += products[i][2]
            shipping_space += products[i][1]
    if shipping_space > available_space:
        return 1

    return cost


# print_shipped_products([0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1])
