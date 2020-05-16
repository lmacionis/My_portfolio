from django.shortcuts import render
from projects.models import Project, Comments, About
from .forms import CommentForm


def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                project=project
            )
            comment.save()

    comments = Comments.objects.filter(project=project)
    context = {
        "project": project,
        "comments": comments,
        "form": form,
    }
    return render(request, "project_detail.html", context)


def about_index(request):       # creates a response to html files
    about = About.objects.get()
    context = {"about": about}
    return render(request, "about_index.html", context)


def home(request):
    return render(request, "home.html", {})
