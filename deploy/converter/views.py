from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse 
import os
from .apps import ConverterConfig

@csrf_exempt 
def index(request):

    try:
        file = request.FILES['file']

        lang = 'EN'
        if(request.POST.get('lang', False) and request.POST['lang'] in ['RU', 'EN', 'UZ', 'UZL', 'LV', 'GR']):
            lang = request.POST['lang']

        if file.content_type not in ['image/png', 'image/jpeg', 'image/gif']:
            return HttpResponse('이미지 파일을 업로드 해주세요');

        inputFileName = "input" + os.path.splitext(str(file))[1]
        pwd = os.path.dirname(__file__)
        inputFileDir = pwd + '/input/' + inputFileName
        
        with open( inputFileDir, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        print("# image saved in" + inputFileDir)
        print("# lang: " + lang)

        res = ConverterConfig.recognizer.run(img= inputFileDir,
                                               lang=lang, 
                                               draw_refined=ConverterConfig.recognizer.DRAW_NONE,
                                               find_orientation=True,
                                               align_results=True,
                                               process_2_sides=False,
                                               repeat_on_aligned=False,
                                               )
        return HttpResponse("\n".join(res['braille']))


    except Exception as e:
        print(Exception)
        return HttpResponse('에러가 발생하였습니다')

