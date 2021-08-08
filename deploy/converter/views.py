from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
# Create your views here.
def index(request):
    if request.method == 'POST':
        
        return HttpResponse('hi')