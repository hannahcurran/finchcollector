from django.shortcuts import render

finches = [
    {'name': 'Susie', 'breed': 'Zebra', 'age': 5, 'habitat': 'grasslands'},
    {'name': 'Jazz', 'breed': 'Society', 'age': 8, 'habitat': 'urban'},
    {'name': 'Tootsie', 'breed': 'Spice', 'age': 6, 'habitat': 'forests'},
]

# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches':finches
    })