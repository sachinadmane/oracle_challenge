#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from oracle.models import Recipe,RecipeDetails
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	all_recipe = Recipe.objects.all()

	template = loader.get_template('home.html')
	context = {

		'query': all_recipe

	}
	return HttpResponse(template.render(context, request))
	# //return render(request,"home.html")