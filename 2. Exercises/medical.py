def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

if __name__ == '__main__':
    name = "David"
    weight = 83
    height = 1.85
    
    bmi = calculate_bmi(weight, height)
    print(f"{name}'s BMI is: {bmi:.2f}")