#!python
# log/views.py
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from oracle.models import Recipe, RecipeDetails
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from oracle.forms import RecipeForm, RecipeDetailsForm

from django.utils.html import escape


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="/")
def view(request):
    username = request.user.username
    if 'id' in request.GET:
        recipeid = request.GET['id']
    else:
        recipeid = False
    if recipeid:

        recipeprimaryid = get_object_or_404(Recipe, pk=recipeid)
        details = get_list_or_404(RecipeDetails, recipe__pk=recipeid)

        template = loader.get_template('view.html')
        context = {

            'id': recipeid,
            'query': details,
            'recipe': recipeprimaryid

        }
        return HttpResponse(template.render(context, request))

    else:

        return HttpResponse("<h1> The requested page cannot be found </h1>")


@csrf_exempt
def delete(request):
    username = request.user.username

    if 'id' in request.POST:
        recipeid = request.POST['id']
    else:
        recipeid = False

    if recipeid is not False:
        Recipe.objects.filter(id=recipeid).delete()

        return HttpResponse("deleted")


@login_required(login_url="/")
def edit(request):
    username = request.user.username

    if 'id' in request.GET:
        recipeid = request.GET['id']
    else:
        recipeid = False

    if recipeid:
        recipeprimaryid = get_object_or_404(Recipe, pk=recipeid)
        details = get_list_or_404(RecipeDetails, recipe__pk=recipeid)
        if hasattr(recipeprimaryid, 'owner'):
            if username == recipeprimaryid.owner:
                template = loader.get_template('edit.html')
                context = {'id': recipeid, 'recipe': recipeprimaryid, 'query': details}
                return HttpResponse(template.render(context, request))
            else:
                return HttpResponse("<h1> You are not authorized to edit this page.</h1>")

    else:

        return HttpResponse("<h1> The URL you requested is invalid.</h1>")


def update(request):
    if request.method == 'POST':

        if 'recipeid' in request.POST:
            recipeid = request.POST['recipeid']
        else:
            recipeid = False

        if 'recipedescription' in request.POST:
            steps = request.POST.getlist('recipedescription')
        if recipeid:
            recipeprimaryid = get_object_or_404(Recipe, pk=recipeid)

            recipeprimaryid.name = escape(request.POST["name"])

            recipeprimaryid.description = escape(request.POST["description"])

            recipeprimaryid.save()

            details = get_list_or_404(RecipeDetails, recipe__pk=recipeid)

        for item,item2 in zip(details,steps):
            item.recipedescription = escape(item2)

            item.save()

    return HttpResponseRedirect('/')
