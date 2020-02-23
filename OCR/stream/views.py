from django.shortcuts import render
import requests
from . import ocr
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import cStringIO
from PIL import Image
import re
from io import BytesIO
import base64
import re

import pytesseract as pyt


def init(request):
    return render(request, 'front.html')


@csrf_exempt
def stream(request):
    link = request.POST.get('link', None)
    # text = ocr.get_text()
    link = re.search(r'base64,(.*)', link).group(1)

    link = base64.b64decode(link)
    # link = StringIO(link.decode('base64'))

    tempimg = BytesIO(link)

    img = Image.open(tempimg)
    text = pyt.image_to_string(img, lang="eng")
    return render(request, 'front.html', {'data': text})
