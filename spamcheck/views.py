from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

# Create your views here.

def predictor(request):
    if request.method == 'POST':
        email = request.POST['emailBody']
        emailPredict = model.predict([email])
        ans = "check"
        if emailPredict[0]==0:
            ans = "not a spam"
        else:
            ans = "a spam"
        return render(request, 'main.html', {'ans': ans})
    return render(request, 'index.html')




    