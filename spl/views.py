from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from spl.models import Books
from comments.models import Comments
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
	name = 'HOME INDEX'
	t = get_template('main/home.html')
	html = t.render(Context({'name':name,'books':Books.objects.all()}))
	return HttpResponse(html)
	
	# return HttpResponse("Hello World!")
	# return render_to_response("main/home.html", {'hello': "Hello World!"})
	# return render_to_response("main/home.html", {'hello': "Hello World!",'books':Books.objects.all()})


def book(request, book_slug=0):
	book = Books.objects.get(slug=book_slug)
	comments = Comments.objects.filter(book_id=book.id)
	cs = comments.count
	c = {}
	c.update(csrf(request))
	if request.user.is_authenticated():
		userdetails = request.user
	else:
		userdetails = None
	t = get_template('books/single.html')
	html = t.render(Context({'name':'single.html','book':book,'comments':comments,'userdetails':userdetails,'cs':cs}, c))
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


def account(request):
	if request.user.is_authenticated():
		return render_to_response('main/account.html', {'userdetails':request.user})
	else:
		c = {}
		c.update(csrf(request))
		return render_to_response('main/login.html',c)

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('main/login.html',c)


def logout(request):
	auth.logout(request)
	return render_to_response('main/login.html',{'error':'You are now logged out.'})

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/books/')
	else:
		return render_to_response('main/login.html',{'error':'Incorrect username or password'})
	

def signup(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#require email and send activation code etc here...
			return HttpResponseRedirect('/accounts/login/',{'error':'Your account is now created. Please login.'})
	

def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	
	return render_to_response('main/register.html',args)
	

def commentedit(request, comment_id):
	comment = Comments.objects.get(id=comment_id)
	c = {}
	c.update(csrf(request))
	if request.user.is_authenticated():
		userdetails = request.user
	else:
		userdetails = None
	if userdetails.is_staff:
		c['comment'] = comment
		c['userdetails'] = userdetails
		return render_to_response('comments/single.html',c)
	else:
		return HttpResponseRedirect('/books/')
	

def commentupdate(request):
	comment = request.POST.get('comment','')
	data = request.POST.get('data','')
	c = Comments.objects.get(id=data)
	c.body = comment
	c.save()
	thisbook = Books.objects.get(id=c.book_id)
	slug = thisbook.slug
	return HttpResponseRedirect('/books/details/'+slug)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	