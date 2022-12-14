from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages

from .models import Blog,Customer


def index(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.order_by('-pub_date')[:5]
    context = {'blogs': blogs}
    messages.success(request, "Welcome to blog page")
    return render(request, 'blog.html', context)


def blog_detail(request, blog_slug=0):
    blog = get_object_or_404(Blog, blog_slug=blog_slug)
    context = {'blog': blog}
    messages.success(request, "Welcome to blog detail page")
    return render(request, 'blog-detail.html', context)

def contact(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    messages.success(request, "Welcome to contact page")
    return render(request, 'contact.html', context)


def services(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    messages.success(request, "Welcome to our services page")
    return render(request, 'services.html', context)

def about(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    messages.success(request, "Welcome to about page")
    return render(request, 'about.html', context)


def portfolio(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    messages.success(request, "Welcome to portfolio page")
    return render(request, 'portfolio.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    del request.session['customer_detail']
    return redirect('/login/')

def login(request):
    if 'customer_detail' not in request.session:
        return render(request, 'login.html')
    else:
        return redirect('/dashboard/')

def signin(request):
    msg=''
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (Customer.objects.filter(email=email,password=password)).exists():
           customerDetail = Customer.objects.filter(email=email).first()
           request.session['customer_detail'] = {"customer_email":customerDetail.email,"customer_id":customerDetail.id,'msg':'Successfull login'}
           return redirect('/dashboard/')
        else:
            request.session['customer_detail'] = {"customer_email":'',"customer_id":'','msg':'invalid login'}

    return render(request, 'login.html',{'msg':msg})



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'management/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'management/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'management/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('management:results', args=(question.id,)))