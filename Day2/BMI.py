print("BMI Calculator")

height = input("Please enter your weight:\t")
weight = input("Please enter your height:\t")

height_as_float = float(height)
weight_as_float = float(weight)

bmi = weight_as_float / height_as_float ** 2

bmi_as_str = str(bmi)

print("This is your BMi:" + bmi_as_str)