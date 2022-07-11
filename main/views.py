from django.shortcuts import render
# Create your views here.
def index(request):
    global exp
    exp=""
    return render(request, "index.html")
def input(request):
    global exp
    exp+=request.POST['val']
    return render(request, "index.html", {"result": exp})

def eq(request):
    global exp
    exp=request.POST['answer']
    return render(request, "index.html", {"result": exp})

def ac(request):
    global exp
    exp=""
    return render(request, "index.html", {"result": exp})
def bs(request):
    global exp
    exp=exp[:-1]
    return render(request, "index.html", {"result": exp})
def equate(request):
    global exp
    if exp=="":
        exp='0'
    exp=str(eval(exp))
    return render(request, "index.html", {"result": exp})