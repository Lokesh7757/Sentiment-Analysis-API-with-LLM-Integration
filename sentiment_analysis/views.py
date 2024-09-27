from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd

@api_view(['POST'])
def sentiment_analysis(request):
    file = request.FILES.get('file')

    if not file:
        return JsonResponse({"error": "No file provided"}, status=400)

    try:
        # Process file (CSV or XLSX)
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return JsonResponse({"error": "Invalid file format. Only CSV and XLSX supported."}, status=400)
        
        if 'Review' not in df.columns:
            return JsonResponse({"error": "Missing 'Review' column in the file."}, status=400)

        reviews = df['Review'].tolist()
        sentiment_result = perform_sentiment_analysis(reviews)

        return JsonResponse(sentiment_result, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def perform_sentiment_analysis(reviews):
    # Simulate sentiment analysis logic (replace with actual API integration)
    positive, negative, neutral = 0, 0, 0

    for review in reviews:
        if "good" in review.lower() or "great" in review.lower():
            positive += 1
        elif "bad" in review.lower() or "terrible" in review.lower():
            negative += 1
        else:
            neutral += 1

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }
