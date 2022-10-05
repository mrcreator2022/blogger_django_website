from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Blog


def index(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.order_by('-pub_date')[:5]
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)


def blog_detail(request, blog_slug=0):
    blog = get_object_or_404(Blog, blog_slug=blog_slug)
    context = {'blog': blog}
    return render(request, 'blog-detail.html', context)

def contact(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'contact.html', context)


def services(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'services.html', context)

def about(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'about.html', context)


def portfolio(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'portfolio.html', context)

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