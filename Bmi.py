while True:
    try:
        mass = float(input("Please state your mass (kg): ").replace(',', '.'))  # Substitui , por .
        break
    except ValueError:
        print("Invalid input. Please utilize '.' instead of ','.")

while True:
    try:
        height = float(input("Please state your height (m): ").replace(',', '.'))  # Substitui , por .
        break
    except ValueError:
        print("Invalid input. Please utilize '.' instead of ','.")

bmi = mass / height ** 2  

print(f"Your BMI is: {bmi:.2f}")
