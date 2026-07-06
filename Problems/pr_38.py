
# QUESTION: Write a python program using function to convert celsius to fahrenheit.

# °F = (°C × 1.8) + 32
def fah(cel):
    return(cel*(1.8))+32

c = 0
f = fah(c)
print(f"Fahrenheit Temperature is {f}")