celsius = input("Please enter a temperature in the form of a number followed by the letter C: ")
celsius = celsius[:-1]
fahrenheit = ((float(celsius) * (9/5)) + 32)
formatted = str(round(fahrenheit, 2)) + 'F'
print(formatted)
