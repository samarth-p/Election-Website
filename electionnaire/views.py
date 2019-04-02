from django.shortcuts import render, render_to_response
from electionnaire.forms import CaptchaTestForm,PostForm
from django.shortcuts import redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,authenticate,logout
from twilio.rest import Client
from random import random
from .models import Voter,Post
from django.contrib import messages
from django.shortcuts import render, render_to_response, get_object_or_404
from electionnaire.forms import CaptchaTestForm
from .models import Post, Candidate, Constituency, User, Party, Eci, Voter
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	logout(request)
	request.session['id'] = -100
	return render(request, 'electionnaire/home.html',{'posts':Post.objects.order_by('-post_time')})

def login(request):
	context = {'error':''}
	if request.POST and request.session['id']<0:
		print(request.POST)
		voter_id = int(request.POST['voter_id'])
		aadhar = request.POST['aadhar']
		phone = str(request.POST['phone'])
		try:
			voter = Voter.objects.get(voter_id=voter_id)
			comp = Voter.objects.get(aadhar_no=aadhar)
			ccomp = Voter.objects.get(phone=phone)
			if(voter==comp and comp==ccomp):
				request.session['id'] = voter_id
				otp = 10000-(random()*10000)
				otp = int(otp)
				request.session['otp'] = otp
				print(request.session['otp'])
				phone = '+91'+str(phone)
				account = "AC788cc259fbbd98c5c06317072e09e300"
				token = "4a595adea5b6701d2b506b2ee2798b43"
				client = Client(account, token)
				message = client.messages.create(to=phone, from_="+13023973912", body=str(request.session['otp']))
				return HttpResponseRedirect(reverse('electionnaire:confirm',args=(voter_id,)))
		except:
			context['error'] = 'Invalid credentials. Try again.'
			return render(request,'electionnaire/login.html',context)
			pass
	else:
		context['error'] = 'Enter valid credentials or refresh the page.'
		return render(request, 'electionnaire/login.html',context)

def confirm(request,voter_id):
	if request.session['id']==voter_id:
		return render(request, 'electionnaire/otp.html',{'voter_id':voter_id})
	else:
		return HttpResponseRedirect(reverse('electionnaire:home'))

def verify(request,voter_id):
	print('verify')
	print('voter_id')
	print(request.POST)
	print(request.session['id'],voter_id)
	if request.POST:
		print('started')
		print(request.POST,request.session['id'],request.session['otp'],'done')
		if int(request.session['otp']) == int(request.POST['otp']):
			return HttpResponseRedirect(reverse('electionnaire:loggedIn',args=(voter_id,)))
	return HttpResponseRedirect(reverse('electionnaire:login'))


def loggedIn(request,voter_id):
	if request.session['id'] == voter_id:
		voter = Voter.objects.get(voter_id=voter_id)
		posts = Post.objects.order_by('-post_time')
		form = PostForm()
		return render(request, 'electionnaire/loggedIn.html',{
			'voter':voter,
			'posts':posts,
			'form':form,
			})

def upload(request):
	print(request.POST)
	if request.method == 'POST':		
		form = PostForm(request.POST,request.FILES)		
		if form.is_valid():
			image = form.cleaned_data['image']
			caption = form.cleaned_data['caption']
			latitude = request.POST['latitude']
			longitude = request.POST['longitude']
			severity = request.POST['severity']
			Post.objects.create(
				image=image,
				voter=Voter.objects.get(voter_id=request.session['id']),
				caption=caption,
				latitude=latitude,
				longitude=longitude,
				severity=severity
			)
	else:
		form = PostForm()
	return HttpResponseRedirect(reverse('electionnaire:loggedIn',args=(request.session['id'],)))

def success(request):
	return render(request, 'electionnaire/success.html')

def vote(request, voter_id):
    voter = get_object_or_404(Voter, voter_id=voter_id)
    consti = voter.constituency
    candidate_list = Candidate.objects.filter(constituency=consti)
    context = {
        'candidate_list': candidate_list,
        'voter_id': voter_id,
    }
    return render(request, 'electionnaire/vote.html', context)

def process_vote(request, voter_id):
    voter = get_object_or_404(Voter, voter_id=voter_id)
    voter.voted = True
    voter.save()
    print(request.POST)
    candidate_id = request.POST['vote']
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.votes += 1
    candidate.save()
    return render(request, 'electionnaire/success.html',{'voter_id':voter.voter_id})


def eci_login(request):
	return render(request, 'electionnaire/eci_login.html')


@login_required
def loggedIn_eci(request):
	return render(request, 'electionnaire/loggedIn_eci.html',{'posts':Post.objects.order_by("-post_time")})

@login_required
def const(request):
    const_list = Constituency.objects.all()
    return render(request, 'electionnaire/results_1.html', {'const_list': const_list})

# @login_required
# def const_result(request, const_id):
#     const = get_object_or_404(Constituency, id=const_id)
#     candidate_list = const.candidate_set.all()
#     return render(request, 'electionnaire/results_2.html', {'candidate_list': candidate_list})

@login_required
def results(request):
	return render(request, 'electionnaire/results.html')

@login_required
def results_const(request, const_id):
    const = get_object_or_404(Constituency, id=const_id)
    candidate_list = const.candidate_set.all()
    candidate_list = sorted(candidate_list, key=lambda x: x.votes, reverse=True)
    return render(request, 'electionnaire/results_const.html', {'candidate_list': candidate_list})

@login_required
def results_party(request):
    party_list = Party.objects.all()
    party_list = sorted(party_list, key=lambda x: x.total_votes, reverse=True)
    return render(request, 'electionnaire/results_party.html', {'party_list': party_list})


# from twilio.rest import Client

# account = "AC788cc259fbbd98c5c06317072e09e300"
# token = "4a595adea5b6701d2b506b2ee2798b43"
# client = Client(account, token)

# message = client.messages.create(to="+918618225880", from_="+13023973912",
#                                  body="let's get to work")
