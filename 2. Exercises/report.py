from medical import calculate_bmi

def fitness_message(weight, height):
    
    bmi = calculate_bmi(weight, height)
    
    if bmi > 25:
        return "Overweight"
    elif bmi < 18.5:
        return "Underweight"
    else:
        return "Normal Weight"
    
if __name__ == "__main__":
    weight = 83
    height = 1.85
    
    print(fitness_message(weight, height))