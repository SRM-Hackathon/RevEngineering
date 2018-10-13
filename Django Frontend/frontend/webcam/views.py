from django.shortcuts import render
from webcam.models import UploadForm,Upload
from django.http import HttpResponseRedirect
#from webcam.train1 import testmodel
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import json
from django.views.decorators.csrf import csrf_exempt
import re
import base64
from webcam.lastfm_rec import nameinput
text="Outside"

class HomePageView(TemplateView):
    template_name = "index.html"


def output1(request):
        #py_obj = 10
        py_obj=testmodel('F:\\facial-frontend\\frontend\\media\\'+uploaded_file_url)
        return render(request, 'output.html' ,{'output': py_obj})


def webcam(request):

    return render(request, 'webcam.html')


@csrf_exempt
def imgdata(request):
    if request.is_ajax():
        url = request.POST.get('image_data')
        print("Received!!!!!")
        text="inside"

        with open('/media/arkochatterjee/MISC/GitHub/SRMHackathon/RevEngineering/Django Frontend/frontend/media/webcam/webcam.png', 'wb') as f:
            f.write(base64.decodestring(url.split(',')[1].encode()))
        return render(request, 'index.html')
    return render(request,'output.html',{'output':'Not Received'})


def emotion(request):
    text="Hey! I'm inside!"
    return render(request,'index0.html')



def textinput(request):
    if 'ArticleS' in request.POST:
        screenname = request.POST.get("Article", None)
        t=nameinput(screenname)
        return render(request, 'output.html' ,{'output': t})

    return render(request,'textinput.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = (filename)
        #py_obj=testmodel('media\\'+uploaded_file_url)
        return render(request, 'output.html' ,{'output': 'hey'})

    return render(request, 'simple_upload.html')
