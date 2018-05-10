from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Blog,Category

# Create your views here.
def index(request):
	blog=Blog.objects.all().order_by('publicationdate')
	
	paginator=Paginator(blog,3)
	page=request.GET.get('page')
	try:
		p=paginator.page(page)
	except PageNotAnInteger:
		p=paginator.page(1)
	except EmptyPage:
		p=paginator.page(paginator.num_pages)
		

	return render(request,'index.html',{'blog':blog,'blog':p})

def blog_detail(request):
	blog_detail=Blog.objects.all()
	return render(request,'blog_detail.html',{'blog_detail':blog_detail})

def author_detail(request,pk):
	author_detail=get_object_or_404(Blog,pk=pk)
	return render(request,'author_detail.html',{'author_detail':author_detail})

def author(request):
	blog=Blog.objects.all()
	return render(request,'author.html',{'blog':blog})

def article(request):
	blog=Blog.objects.all()
	return render(request,'article.html',{'blog':blog})


