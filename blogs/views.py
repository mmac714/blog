from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import PostForm, EditForm

# Create your views here.

@login_required
def home(request):
	""" The home page for Blog Post. """
	posts = BlogPost.objects.order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'blogs/home.html', context)

@login_required
def new_post(request):
	""" Add a new blog post. """
	if request.method != 'POST':
		# No data submitted, create a blank form
		form = PostForm()
	else:
		# POST data submitted; process data.
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:home'))

	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
	""" Edit an existing post. """
	post = BlogPost.objects.get(id=post_id)
	if post.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Initial request, prefill form with the current post.
		form = EditForm(instance=post)
	else:
		# Post data submitted, process data.
		form = EditForm(instance= post, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:home'))

	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)






