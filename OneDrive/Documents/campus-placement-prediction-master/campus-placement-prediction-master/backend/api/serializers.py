from rest_framework import serializers
from .models import Prediction


class PredictionSerializer(serializers.ModelSerializer):
    """Serializer for Prediction model"""
    
    class Meta:
        model = Prediction
        fields = [
            'id', 'name', 'email', 'tenth_score', 'twelfth_score', 
            'degree', 'specialization', 'degree_percentage', 
            'cgpa', 'salary',
            'prediction', 'confidence', 'created_at'
        ]
        read_only_fields = ['id', 'prediction', 'confidence', 'created_at']


class PredictInputSerializer(serializers.Serializer):
    """Serializer for prediction input"""
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    tenth_score = serializers.FloatField()
    twelfth_score = serializers.FloatField()
    degree = serializers.CharField(max_length=50)
    specialization = serializers.CharField(max_length=50)
    degree_percentage = serializers.FloatField()
    cgpa = serializers.FloatField()
    salary = serializers.FloatField(default=0)
