cars = ['audi', 'bmw', 'subaru', 'toyota']

made_in_japan = ['sony', 'subaru', 'toyota', 'suzuki', 'kawasaki']

for car in cars:
    if car.lower() in made_in_japan:
        print(f"{car.title()} - made in Japan!")
    else:
        print(car.title())