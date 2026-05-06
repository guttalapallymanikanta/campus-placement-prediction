from django.db import models

class Prediction(models.Model):
    """Model to store prediction history"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tenth_score = models.FloatField()
    twelfth_score = models.FloatField()
    degree = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    degree_percentage = models.FloatField()
    cgpa = models.FloatField()
    salary = models.FloatField(default=0)
    
    prediction = models.IntegerField()  # 0 or 1
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {'Placed' if self.prediction == 1 else 'Not Placed'}"
    
    class Meta:
        ordering = ['-created_at']
