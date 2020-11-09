from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # fs = FileSystemStorage()
        # filename = fs.save(file.name, file)
        # uploaded_file_url = fs.url(filename)
        # return render(request, 'index.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    context = {}
    return render(request, "index.html", context)
