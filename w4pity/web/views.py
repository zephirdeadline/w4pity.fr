from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Site
# Create your views here.


def found(request):
    projects = Post.objects.filter(isProject=True, tags__contains=request.GET.get('search')).order_by("-date")
    posts = Post.objects.filter(isProject=False, tags__contains=request.GET.get('search')).order_by("-date")
    site = Site.objects.last()
    return render(request, "web/found.html", locals())


def main(request, type_view="tips", page=1):
    is_project = True if type_view == "project" else False
    if is_project:
        projects_active = "active"
    else:
        tips_active = "active"
    all_post = Post.objects.filter(isProject=is_project).order_by("-date")
    paginator = Paginator(all_post, 2)
    posts = paginator.get_page(page)
    site = Site.objects.last()
    current_page = int(page)
    max_page = int(paginator.num_pages)

    return render(request, "web/index.html", locals())


def contact(request):
    if request.method == "POST":
        email = EmailMessage('Message de W4pity.fr',
                             request.POST["name"] + '\n'
                             + request.POST['phone'] + '\n'
                             + request.POST['email'] + '\n\n'
                             + request.POST['content'] + '\n',
                             to=['w4pity@gmail.com'])
        email.send()
    site = Site.objects.last()
    return render(request, "web/contact.html", locals())


def about(request):

    site = Site.objects.last()
    return render(request, "web/about.html", locals())


def post(request, id_post):
    site = Site.objects.last()
    post = Post.objects.get(id=id_post)
    return render(request, "web/post.html", locals())
