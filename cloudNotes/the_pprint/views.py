from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from forms import FileForms
from models import UploadFile
from datetime import datetime
# Create your views here.

def fileUpload_page(req):
    if req.method == "POST":
        file = UploadFile()
        file.file_name = req.FILES.dict().get("file")
        file.upload_time = datetime.now()
        file.uploader = "zero"
        file.save()
        return HttpResponse("hello,world")
    return render(req, 'index.html')

# @csrf_exempt
def register(request):
    if request.method == "POST":
        uf = FileForms(request.POST, request.FILES)
        if uf.is_valid():
            uploadFile = uf.cleaned_data['file']
            file = UploadFile()
            file.file_name = uploadFile
            file.upload_time = datetime.now()
            file.uploader = "zero"
            file.save()
            return HttpResponse('upload ok!')
    else:
        uf = FileForms()
    return render_to_response('sss.html', {'uf': uf})