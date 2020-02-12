from ghostpost.models import BoastRoast
from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostpost.forms import CreateForm


def index(request):
    html = "index.html"

    items = BoastRoast.objects.all()
    boasts = BoastRoast.objects.filter(boolean=True)
    roasts = BoastRoast.objects.filter(boolean=False)

    new_list = sortitem(items)
    boasts = sortitem(boasts)
    roasts = sortitem(roasts)

    return render(request, html, {
        'boasts': boasts,
        'roasts': roasts,
        'new_list': new_list
        })


def sortitem(args):
    my_list, new_list = [], []
    for each in args:
        my_list.append({each: each.post_date})

    def myFunc(e):
        return e.items()

    my_list.sort(key=myFunc)

    for each in my_list:
        for x in each:
            new_list.append(x)
    return new_list


def add_form(request):
    html = "addform.html"

    if request.method == "POST":
        form = CreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            BoastRoast.objects.create(
                title=data['title'],
                boolean=data['boolean'],
                content=data['content'],
                upvotes=data['upvotes'],
                downvotes=data['downvotes'],
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = CreateForm()

    return render(request, html, {'form': form})
