from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import pandas as pd

@api_view(['POST'])
def sentiment_analysis(request):
    file = request.FILES.get('file')

    if not file:
        return JsonResponse({"error": "No file provided"}, status=400)

    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return JsonResponse({"error": "Invalid file format. Only CSV and XLSX supported."}, status=400)
        
        reviews = df['Review'].tolist()
        sentiment_result = sentiment_analysis(reviews)
        return JsonResponse(sentiment_result, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
