from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	template_name = "index.html"
	blogs = BlogPost.objects.all() #queryset
	context = {'greeting':'Hello', 'name':'Dipesh', 'blogs':blogs, 'title':'Home'}
	return render(request, template_name, context)

def contact(request):
	template_name = "contact.html"
	context = {'Phone':'9861247561', 'title':'Contact'}
	return render(request, template_name, context)


def about(request):
	template_name = "about.html"
	context = {'About':'Now is Better than Never----Django', 'title':'AboutUs'}
	return render(request, template_name, context)

@login_required()
def createblog(request):
	if request.method=='POST':
		form = BlogPostForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
			return redirect("home")
	else:
		form = BlogPostForm()
	context={'form':form, 'title':'New Blog Post'}
	template_name = 'blog_create.html'
	return render(request, template_name, context)

def detail(request, pk):
	template_name = "post.html"
	blog = get_object_or_404(BlogPost,pk=pk)
	context = {'blog':blog, 'title':'Details'}
	return render(request, template_name, context)


def signup(request):
	template_name ="registration/signup.html"
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	context= {'form':form}
	return render(request, template_name, context)