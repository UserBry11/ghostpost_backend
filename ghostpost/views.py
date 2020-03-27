from ghostpost.models import BoastRoast
from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.forms import CreateForm
from ghostpost.serializers import BoastRoastSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all().order_by('-post_date')
    serializer_class = BoastRoastSerializer

# detail view we don't. Why get newest item detail view because we only have 1 there.
# /api/boastroast/popular/
# detail=True for single get object
    @action(methods=['get'], detail=False)
    def popular(self, request, pk=None):

        def myFunc(event):
            return event.vote_score

        popular = sorted(self.get_queryset(), key=myFunc, reverse=True)
        serializer = self.get_serializer(popular, many=True)

        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='upvote')
    def upvote(self, request, pk=None):
        id_value = request.query_params['id']
        item = BoastRoast.objects.filter(id=id_value).first()
        item.upvotes += 1
        item.save()

        serializer = self.get_serializer(item, many=False)

        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def downvote(self, request):
        id_value = request.query_params['id']
        item = BoastRoast.objects.filter(id=id_value).first()
        item.downvotes += 1
        item.save()
        serializer = self.get_serializer(item, many=False)

        return Response(serializer.data)


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
    item.downvotes += 1
    item.save()

    return HttpResponseRedirect(reverse('homepage'))
