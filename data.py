import csv , os



gender = input("assis gender(man or woman):  ")
if gender == 'woman':
    gender = 1
else:
    gender = 0
gender = str(gender)
name = input('your name: ')
country = input('whats your country: ')
city = input('whats your city: ')
gm = input('whats your gmail: ')
pgm = input('whats your gmail pass(for sign in or make acount): ')


data = [
    ["country", "name", "gmail","gender","city",'gmail password'],
    [country, name, gm, gender,city,pgm]
]
 

with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

os.remove('data.py')

