print()
food_prices = {'chicken': 1.59, 'beef': 1.99, 'cheese': 1.00, 'milk': 2.50}

family_age = {'otis': 16, 'mom': 42, 'dad': 44, 'cerjuana': 7}
otis_age = family_age['otis']
print(otis_age)

family_age['cerjuana'] = 8
print(family_age)


shoes = {'jordan_13': 1, 'yeezy': 8, 'foamposites': 10, 'air_max': 5, 'sb_dunk': 20}
shoes['sb_dunk'] -= 2
shoes['yeezy'] = 9
shoes['jordan_13'] += 7
shoes['yeezy'] += 7
shoes['foamposites'] += 7
shoes['air_max'] += 7
shoes['sb_dunk'] += 7
shoes['jordan_13'] -= 3
shoes['yeezy'] -= 3
shoes['foamposites'] -= 3
shoes['air_max'] -= 3
shoes['sb_dunk'] -= 3
print(shoes)

family_age['kahlil'] = 23
family_age['enasia'] = 21
family_age['montel'] = 24
print(family_age)

del family_age['mom']
del family_age['dad']
print(family_age)

list_of_cities = ['Oakland', 'Atlanta', 'New York City', 'Seattle', 'Memphis', 'Miami', 'Boston', 'Los Angeles', 'Denver', 'New Orleans']
print(list_of_cities)

Apple_Products = ['iPhone', 'iMac', 'MacBook', 'Airpods', 'iPod', 'iPad', 'Apple_Watch', 'Apple_TV', 'Airpod_Pros', 'Apple_Card']
print(Apple_Products)


print(Apple_Products[0])
print(Apple_Products[5])
print(Apple_Products[8])

print(Apple_Products[4:8])

Apple_Products[0] = 'Apple Watch'
print(Apple_Products[0])

Apple_Products[1] = 'Apple_TV'
print(Apple_Products[1])

Apple_Products[3] = 'iPod'
print(Apple_Products[3])

Apple_Products[4] = 'Airpods'
print(Apple_Products[4])

Apple_Products.append('iPhone')
Apple_Products.extend(['Apple_Controller', 'Apple_Game', 'Apple_Light'])
Apple_Products.insert(8, 'Apple_Game_Console')
print(Apple_Products)

del Apple_Products[6]
Apple_Products.pop(9)
Apple_Products.remove('Airpods')