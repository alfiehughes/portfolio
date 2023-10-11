def c_to_f():
    converted = (celsius * (9/5) + 32)
    rounded = str(round(converted, 2))
    print(rounded)


def f_to_c():
    converted = (fahrenheit - 32) * (5/9)
    rounded = str(round(converted, 2))
    print(rounded)


celsius = float(input("Please enter a temperature in celsius"))
c_to_f()
fahrenheit = float(input("Please enter a temperature in fahrenheit"))
f_to_c()