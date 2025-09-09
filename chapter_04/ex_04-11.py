pizzas = ['salami', 'napoli', 'tonno', 'fungi']

friends_pizzas = pizzas[:]

friends_pizzas.append('diabolo')

pizzas.append('margharita')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print('\nMy friends favorite pizzas are:')
for pizza in friends_pizzas:
    print(pizza.title())