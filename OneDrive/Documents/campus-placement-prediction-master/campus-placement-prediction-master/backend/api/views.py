from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Prediction
from .serializers import PredictionSerializer, PredictInputSerializer
from .ml_utils import get_ml_model


class PredictionViewSet(viewsets.ModelViewSet):
    """ViewSet for Prediction model"""
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    
    @action(detail=False, methods=['post'])
    def predict(self, request):
        """
        Make a new prediction
        
        POST /api/predictions/predict/
        """
        serializer = PredictInputSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Get ML model
            ml_model = get_ml_model()
            
            # Make prediction
            result = ml_model.predict(serializer.validated_data)
            
            # Save to database
            prediction_obj = Prediction.objects.create(
                **serializer.validated_data,
                prediction=result['prediction'],
                confidence=result['confidence']
            )
            
            # Return result
            response_serializer = PredictionSerializer(prediction_obj)
            return Response({
                'success': True,
                'message': f"Student {result['status']} with confidence {result['confidence']}",
                'data': response_serializer.data
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Get prediction statistics
        
        GET /api/predictions/stats/
        """
        total = Prediction.objects.count()
        placed = Prediction.objects.filter(prediction=1).count()
        not_placed = Prediction.objects.filter(prediction=0).count()
        
        placement_rate = (placed / total * 100) if total > 0 else 0
        
        return Response({
            'total_predictions': total,
            'placed': placed,
            'not_placed': not_placed,
            'placement_rate': round(placement_rate, 2)
        })


class HealthCheckView(APIView):
    """Health check endpoint"""
    
    def get(self, request):
        """Check API health"""
        try:
            ml_model = get_ml_model()
            return Response({
                'status': 'healthy',
                'model_loaded': ml_model.model is not None
            })
        except Exception as e:
            return Response({
                'status': 'unhealthy',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
