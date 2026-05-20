from django.shortcuts import render

def bmi_berekenen(request):
    resultaat = None
    categorie = None

    if request.method == 'POST':
        gewicht = float(request.POST['gewicht'])
        lengte = float(request.POST['lengte'])
        
        bmi = gewicht / (lengte ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            categorie = "Ondergewicht"
        elif bmi < 25:
            categorie = "Normaal gewicht"
        elif bmi < 30:
            categorie = "Overgewicht"
        else:
            categorie = "Obesitas"
        
        resultaat = bmi

    return render(request, 'bmi.html', {
        'resultaat': resultaat,
        'categorie': categorie
    })