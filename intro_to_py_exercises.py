#file for all intro to python exercises


current_year = 2023
birth_year = 1998
age = current_year - birth_year
print("My age is " + str(age))

#exercise 2

first_name = 'Maximilian'
middle_name = 'Myles Douglas'
last_name = 'Arkell'
print('My full name is ' + first_name + ' ' + middle_name + ' ' + last_name)

#exercise 3 - ints

length = 92
width = 48.8
area = length * width
print('area is ' + str(round(area, 2)))

money_given = 20
money_required = 9 * 1.49
money_back = money_given - money_required
print('My change is ' + str(money_back))

length_sq = 5.5
area_sq = length_sq**2
total_cost = area_sq * 500
print('Total cost of surface tiling is ' + str(total_cost))

num_bin = 17
print('The binary format for 17 is: ', format(num_bin, 'b'))

#exercise 4 - strings
street = '10 Finch Lane'
city = 'London'
country = 'United Kingdom'
full_address = street+ '\n' + city + '\n' + country
print(full_address)
address2 = f'{street}\n{city}\n{country}'
print("address using f string: "+address2)

exercise2String = "Earth revolves around the sun"
print(exercise2String[6:14]) #Slicing 1 word
print(exercise2String[-3:]) #slicing using negative index

numberFruit = 5
numberVeg = 6
print(f"I eat {numberVeg} veggies and {numberFruit} fruits daily")

s = 'maine 200 banana khaye'
s=s.replace("banana", "samosa").replace("200", "10")
print("Replacing parts of string: "+s)

#Exercise 5 - lists

expenses = [2200, 2350, 2600, 2130, 2190]
differenceJanuaryFebruary = expenses[1] - expenses[0]
print("I spent " + str(differenceJanuaryFebruary) + " extra in February")
totalFirstQuarter = sum(expenses[:3])
print("Total expenses in the first quarter: " + str(totalFirstQuarter))
print("Did I spend 2000 in any month?", 2000 in expenses)
expenses.append(1980) #concatenate list using append
print(expenses)
expenses[3] = expenses[3] - 200 #edit number in list
print(expenses)