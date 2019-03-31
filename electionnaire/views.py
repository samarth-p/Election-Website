from django.shortcuts import render, render_to_response, get_object_or_404
from electionnaire.forms import CaptchaTestForm
from .models import Post, Candidate, Constituency, User, Party, Eci, Voter
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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
    return render(request, 'electionnaire/success.html')


def eci_login(request):
	return render(request, 'electionnaire/eci_login.html')



def loggedIn_eci(request):
	return render(request, 'electionnaire/loggedIn_eci.html')


def const(request):
    const_list = Constituency.objects.all()
    return render(request, 'electionnaire/results_1.html', {'const_list': const_list})


def const_result(request, const_id):
    const = get_object_or_404(Constituency, id=const_id)
    candidate_list = const.candidate_set.all()
    return render(request, 'electionnaire/results_2.html', {'candidate_list': candidate_list})


def results(request):
	return render(request, 'electionnaire/results.html')


def results_const(request, const_id):
    const = get_object_or_404(Constituency, id=const_id)
    candidate_list = const.candidate_set.all()
    candidate_list = sorted(candidate_list, key=lambda x: x.votes, reverse=True)
    return render(request, 'electionnaire/results_const.html', {'candidate_list': candidate_list})

def results_party(request):
    party_list = Party.objects.all()
    party_list = sorted(party_list, key=lambda x: x.total_votes, reverse=True)
    return render(request, 'electionnaire/results_party.html', {'party_list': party_list})
