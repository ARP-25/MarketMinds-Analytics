from django.shortcuts import render

# Create your views here.
def Bag(request):
    """
    A View to return index page
    """
    return render(request, 'bag/bag.html')