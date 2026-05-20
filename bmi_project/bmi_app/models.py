from django.db import models

class BMIBerekening(models.Model):
    gewicht = models.FloatField()
    lengte = models.FloatField()
    bmi = models.FloatField()
    categorie = models.CharField(max_length=50)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BMI: {self.bmi} - {self.categorie}"