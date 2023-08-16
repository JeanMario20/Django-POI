from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .forms import CheckForm

# Create your views here.

##def input(request):
    ##template = loader.get_template('check.html')
    ##submitbutton = request.POST.get("submit")
    ##firstnumber = 0
    ##secondnumber = 0

    ##form = CheckForm(request.POST or None)
    ##if form.is_valid():
        ##firstnumber = form.cleaned_data.get("checkNumber1")
        ##secondnumber = form.cleaned_data.get("checkNumber2")

    ##context ={'form':form, 'firstnumber':firstnumber,'secondnumber':secondnumber,
            ##'submitbutton':submitbutton}
    ##context['form']= CheckForm()
    ##return render(request, "check.html", context)
    ##----return HttpResponse(template.render())


def input(request):
    form = CheckForm(request.POST)
    if request.method == "POST":
        firstnumber = 0
        
        if form.is_valid():
            firstnumber = form.cleaned_data.get("checkNumber1")
            CheckForm(firstnumber)
            check = True
            if not firstnumber % 2:
                check = True
                return render(request, "check.html", {"form":form, "check":check})
            else:
                check = False
                return render(request, "check.html", {"form":form, "check":check})
            ##return HttpResponse(Total)
        else:
            form = CheckForm()
    return render(request, "check.html", {"form":form})

