india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name = input("Enter a city name: ")
city_name = str(city_name)

if city_name in india:
    print("This city is in India!")
elif city_name in pakistan:
    print("This city is in Pakistan!")
elif city_name in bangladesh:
    print("This city is in Bangladesh!")
else:
    print("Sorry I cant identify which area this city is in")