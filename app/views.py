from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def result(request):
    var1 = int(request.POST['num1'])
    var2 = int(request.POST['num2'])
    var3 = var1 * var2



    return render(request, 'result.html', {'var3':var3})
