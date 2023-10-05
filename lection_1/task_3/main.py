unit = input("Select the temperature unit you want to convert to (C/F): ")
temp = float(input("Enter the temperature: "))

#temp_C = float(20.2)
#temp_F = float(68.4)



if unit == "F":
    temp = round((temp * 1.8) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "C":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsium is: {temp}°C")
else:
    print(f"You have to choose between Celsius and Fahrenheit")