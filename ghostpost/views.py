from ghostpost.models import BoastRoast
from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.forms import CreateForm
from ghostpost.serializers import BoastRoastSerializer
from rest_framework import viewsets


class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all()
    serializer_class = BoastRoastSerializer


def index(request):
    html = "index.html"

    items = BoastRoast.objects.all().order_by('-post_date')

    votes = BoastRoast.objects.all().order_by('-upvotes')
    boasts = items.filter(boolean=True)
    roasts = items.filter(boolean=False)

    new_list = items

    return render(request, html, {
        'boasts': boasts,
        'roasts': roasts,
        'new_list': new_list,
        'votes': votes
        })


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


def upvote(request, id):
    item = BoastRoast.objects.filter(id=id).first()
    item.upvotes += 1
    item.save()

    return HttpResponseRedirect(reverse('homepage'))


def downvote(request, id):
    item = BoastRoast.objects.filter(id=id).first()
    item.downvotes -= 1
    item.save()

    return HttpResponseRedirect(reverse('homepage'))
