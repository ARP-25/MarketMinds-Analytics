from django.shortcuts import render

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def render_custom_404(request):
    """ Direct Access Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html")