from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import *
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        User_form = UserCreationForm(request.POST)
        Profile_form = ProfileForm(request.POST)
        if User_form.is_valid() and Profile_form.is_valid():
            user = User_form.save()
            auth_login(request, user)
            user.save()
            profile = Profile_form.save()
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        User_form = UserCreationForm()
        Profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': User_form, 'profile_form': Profile_form})


# def newBooth(request):
#   if request.method == 'POST':
#      form = BoothForm(request.POST, request.FILES)
#     if form.is_valid():
#        booth = form.save(commit=False)
#       booth.created_by = request.user
#      booth.save()
#     request.user.profile.has_booth = True
#    return redirect('home')
# else:
#   form = BoothForm()
# return render(request, 'new_booth.html', {'form': form})


class newBoothView(View):
    form_class = BoothForm
    template = 'new_booth.html'

    def getReverseValidFormPost(self):
        return reverse('home')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            booth = form.save(commit=False)
            booth.created_by = request.user
            booth.save()
            request.user.profile.has_booth = True
            request.user.profile.save()
            return HttpResponseRedirect(self.getReverseValidFormPost())
        return render(request, self.template, {'form': form})


def viewBooth(request, pk):

    booth = Booth.objects.get(pk=pk)
    return render(request, 'viewbooth.html', {'booth': booth})


def newArtwork(request, pk):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.booth = Booth.objects.get(pk=pk)
            artwork.save()
            return redirect('home')
    else:
        form = ArtworkForm()
    return render(request, 'new_artwork.html', {'form': form})

def exploreBooths(request):
    booths = Booth.objects.all()

    return render(request,'explorebooths.html', {'booths': booths})
