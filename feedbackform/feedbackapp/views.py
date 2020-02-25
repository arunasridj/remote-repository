from django.shortcuts import render
from feedbackapp.models import feedbackData
from feedbackapp.forms import feedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()
def feedbackview(request):
    if request.method=="POST":
        fform=feedbackForm(request.POST)
        print(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=feedbackData(
            name=name,
            rating=rating,
            feedback=feedback,
            date=date1,
            )
            data.save()
            feedbacks=feedbackData.objects.all()
            fform=feedbackForm()
            return render(request,'feedbackfile.html',{'fform':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("user missed some value")
    else:
        fform=feedbackForm()
        feedbacks=feedbackData.objects.all()
        return render(request,'feedbackfile.html',{'fform':fform,'feedbacks':feedbacks})

