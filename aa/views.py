import os
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File
from django.conf import settings
from .forms import ProcessForm
from super_resolution.execute import resolve
def home(request):
    ctx = {
        "process": None
    }
    if request.method == "POST":
        upload = request.FILES.get('upload')
        form = ProcessForm(request.POST, request.FILES)
        if form.is_valid():
            process = form.save()
            result = resolve(process.upload.path)
            mr = settings.MEDIA_ROOT
            relpath = os.path.relpath(result, mr)
            process.result.name = relpath
            process.save()
            ctx['process'] = process
    return render(request, "home.html", ctx)