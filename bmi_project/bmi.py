def bereken_bmi(gewicht, lengte):
    bmi = gewicht / (lengte ** 2)
    
    if bmi < 18.5:
        categorie = "Ondergewicht"
    elif bmi < 25:
        categorie = "Normaal gewicht"
    elif bmi < 30:
        categorie = "Overgewicht"
    else:
        categorie = "Obesitas"
    
    return round(bmi, 2), categorie

# Test
gewicht = 70  # kg
lengte = 1.75  # meter
bmi, categorie = bereken_bmi(gewicht, lengte)
print(f"BMI: {bmi}")
print(f"Categorie: {categorie}")