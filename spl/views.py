from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Books
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def home(request):
	
	name = 'HOME INDEX'
	t = get_template('main/home.html')
	html = t.render(Context({'name':name,'books':Books.objects.all()}))
	return HttpResponse(html)
	
	# return HttpResponse("Hello World!")
	# return render_to_response("main/home.html", {'hello': "Hello World!"})
	# return render_to_response("main/home.html", {'hello': "Hello World!",'books':Books.objects.all()})


def book(request, article_id=0):
	book = Books.objects.get(id=book_id)
	name = 'book'
	t = get_template('books/single.html')
	html = t.render(Context({'name':name,'books':books}))
	return HttpResponse(html)


def books(request):
	books = Books.objects.all()
	name = 'books'
	t = get_template('books/all.html')
	html = t.render(Context({'name':name,'books':books}))
	return HttpResponse(html)


def hello(request):
	
	name = 'hello'
	t = get_template('spl/home.html')
	html = t.render(Context({'name':name}))
	return HttpResponse(html)