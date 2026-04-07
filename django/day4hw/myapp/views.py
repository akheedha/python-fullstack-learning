from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        data = request.POST

        return render(request, 'result.html', {
            'name': name,
            'color': color,
            'data': data
        })
    return render(request, 'home.html')