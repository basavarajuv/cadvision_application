from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from gameapp.models import *

# Create your views here.
def index(request):
	post_data = list_post(request)
	print(post_data)
	context = {"post_data": post_data}

	return render(request,'index.html', context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))

def user_login(request):
	'''this function will work for the login
	'''
	if request.method == 'POST':
	    username = request.POST.get('username')
	    password = request.POST.get('password')
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request,user)
	            return HttpResponseRedirect(reverse('index'))
	        else:
	            return HttpResponse("Your account was inactive.")
	    else:
	        print("Someone tried to login and failed.")
	        print("They used username: {} and password: {}".format(username,password))
	        return HttpResponse("Invalid login details given")
	else:
	    return render(request, 'index.html', {})

def game_post(request):
	'''this function will work for the post the description
	'''
	if request.method == 'POST':
		description = request.POST.get('description')
		result = GamePost.objects.create(
					user = request.user,
					description = description
					)
		return HttpResponseRedirect(reverse('index'))

def list_post(request):
	'''function for the list the existing posts
	'''
	post_query = GamePost.objects.values()
	for post in post_query:
		reply_data = Reply.objects.filter(description__id=post['id']).values('reply')
		post['reply'] = reply_data
		
	return post_query
	
	# return render(request, 'index.html', context)

def like_count(request, id):
	'''function for the to increase the like count
	'''
	if request.method == 'POST':
		data_qs = GamePost.objects.filter(id = id).first()
		if data_qs:
			data_qs.like_count += 1
			data_qs.save()
			return redirect('/')
			
		return render(request, 'index.html', {})

def dislike_count(request, id):
	'''function for the to increase the dislike count
	'''	
	if request.method == 'POST':
		data_qs = GamePost.objects.filter(id = id).first()
		if data_qs:
			data_qs.dislike_count += 1
			data_qs.save()
			return redirect('/')

		return render(request, 'index.html', {})

def post_reply(request, id):
	'''function for post the reply or comment for particular post
	'''
	if request.method == 'POST':
		post_reply = request.POST.get('post_reply')
		data_qs = GamePost.objects.filter(id=id).first()
		if data_qs:
			reply_created = Reply.objects.create(
						user = request.user,
						description = data_qs,
						reply = post_reply
						)
		return redirect('/')

		return render(request, 'index.html', {})

def get_reply(request, id):
	'''function for post the reply or comment for particular post
	'''
	data_qs = GamePost.objects.filter(id=id).first()
	if data_qs:
		reply_data = Reply.objects.filter(description = data_qs)
		print(reply_data,'=====')

	return reply_data
