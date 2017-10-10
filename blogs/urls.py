""" Defines the URL patterns for learning_logs. """

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home Page that displays all post
	url(r'^$', views.home, name='home'),

	# Page for a user to crreate a new blog post.
	url(r'^new_post/$', views.new_post, name='new_post'),

	# Page for editing a post.
	url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),

	]