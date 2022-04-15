weight = input("enter your weight in kg:\n")
height = input("enter your height in m:\n")
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
print(bmi)
bmi_as_int = int(bmi)
print(bmi_as_int)
