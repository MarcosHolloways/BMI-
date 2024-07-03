weight = input("Enter your weight in kg: ")
height = float(input("Enter your height in m: "))* 100

bmi = int(weight) / float(( height ** 2 ))
bmi_as_int = int(bmi)
print(f"Your bmi is {bmi_as_int} ")
