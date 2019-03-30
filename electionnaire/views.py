from django.shortcuts import render, render_to_response
from electionnaire.forms import CaptchaTestForm
# Create your views here.
def home(request):
	return render(request, 'electionnaire/home.html')

def login(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render_to_response('electionnaire/login.html',locals())

def confirm(request):
	return render(request, 'electionnaire/otp.html')

def loggedIn(request):
	return render(request, 'electionnaire/loggedIn.html')

def success(request):
	return render(request, 'electionnaire/success.html')

def vote(request):
	return render(request, 'electionnaire/vote.html')

def eci_login(request):
	return render(request, 'electionnaire/eci_login.html')

def loggedIn_eci(request):
	return render(request, 'electionnaire/loggedIn_eci.html')