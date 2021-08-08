from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.urls import reverse
import os

from django.views.generic import View
from django.core.files import File
from .apps import ConverterConfig

@csrf_exempt 
def index(request):

    try:
        print(request)
        file = request.FILES['file']
        print(type(request.FILES['file']))

        if file.content_type not in ['image/png', 'image/jpeg', 'image/gif']:
            return HttpResponse('이미지 파일을 업로드 해주세요');

        inputFileName = "input" + os.path.splitext(str(file))[1]
        pwd = os.path.dirname(__file__)
        inputFileDir = pwd + '/input/' + inputFileName
        
        with open( inputFileDir, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        
        print("image saved")
        # os.system('python AngelinaReader/run_local.py ')
        print(ConverterConfig)


        res = ConverterConfig.recognizer.run(img= inputFileDir,
                                               lang='EN', 
                                               draw_refined=ConverterConfig.recognizer.DRAW_NONE,
                                               find_orientation=True,
                                               align_results=True,
                                               process_2_sides=False,
                                               repeat_on_aligned=False,
                                               )
        return HttpResponse("\n".join(res['braille']))


    except Exception as e:
        print(Exception )
        return HttpResponse('에러가 발생하였습니다')

