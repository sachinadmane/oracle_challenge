from django.http import HttpResponse,HttpResponseRedirect
from . models import Recipe,RecipeDetails
from django.template import loader
from django.shortcuts import redirect,render
from django.contrib import messages
from . forms import RecipeForm,RecipeDetailsForm

from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    recipe=Recipe.objects.all
    template=loader.get_template('oracle/index.html')
    context={

       'recipe':recipe
    }
    return HttpResponse(template.render(context,request))


def add(request):

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        details=RecipeDetailsForm(request.POST)
        a_valid = form.is_valid()
        b_valid = details.is_valid()
        if a_valid and b_valid:
            obj = form.save(commit=False)
            obj.owner = request.user.get_username()
            fields=request.POST.getlist('recipedescription')
            # fields=recipedescription.split('\r\n')

            a=obj.save()
            obj2=details.save(commit=False)
            for x in range(0,len(fields)):
                y=x+1
                obj2.owner = request.user.get_username()
                obj2.recipe = Recipe.objects.latest('id')
                obj2.number = y
                obj2.recipedescription=fields[x]
                obj2.save()
                obj2.pk=None

            return HttpResponseRedirect("/")
        else:
            print("Error submitting details")
    else:
        messages.error(request, "Error")


    return render(request,'add.html', {'form': RecipeForm(),'details':RecipeDetailsForm})
