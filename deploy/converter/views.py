from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse


# Create your views here.
def index(request):
    return HttpResponse('hi')