from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'reviews/home.html')

def sentiment_analysis(request):
    result = None
    if request.method == "POST":
        text = request.POST.get('text')
        if text:  # Check if text is not None or empty
            # Implement your sentiment analysis logic here
            result = "Sentiment analysis result for: " + text  # Replace with actual logic
        else:
            result = "No text provided for analysis."
        
    return render(request, 'reviews/sentiment_analysis.html', {'result': result})
