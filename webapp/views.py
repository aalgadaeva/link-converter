from django.shortcuts import render
from django.contrib import messages
from .forms import ConvertForm
from .tasks import convert_load

def main_page(request):
    if request.method == 'POST':
        form = ConvertForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            url = request.get_host()
            convert_load.delay(url, email, link)
            messages.success(request, 'Download link has been sent to your email.')
    else:
        form = ConvertForm()

    return render(request, 'index.html', locals())
