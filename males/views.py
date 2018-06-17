from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from males.models import Male
from .forms import MaleForm
from django.http import HttpResponseRedirect
import io
import os
from google.cloud import vision
from google.cloud.vision import types


def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
        return text.description.encode('utf-8')


'''
def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print()
    for text in texts:
        print('\n"{}"'.format(text.description))
    print()
'''

# 'https://img.etimg.com/photo/59421648/sarcasticrofl.jpg'


def main_home(request):
    form = MaleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        queryset = Male.objects.all()
        if len(queryset) >= 1:
            Male.objects.all().delete()
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('response/')
    context = { 
        "form": form,
    }
    return render(request, 'index.html', context)
    

def response(request):
    queryset = Male.objects.all()
    for each in queryset:
        res_text = detect_text(each.image.path)
        astring = res_text.decode().strip('\\n')
    context = {
        "object_list" : queryset,
        "restext": astring,
    }
    return render(request, 'result.html', context)
