from django.shortcuts import render, redirect, get_object_or_404

from .models import Site
from .utils import create_shortcut

def index(request):
    if request.method == 'POST':
        context = {
            'status': 'success',
        }

        site_url = request.POST['title']

        site = Site(site_url=site_url, shortcut=create_shortcut())
        site.save()

        context['shortcut'] = site.shortcut
        return render(request, 'index.html', context)
       
    return render(request, 'index.html')
        

def redirect_to_base_url(request, shortcut):
    site = get_object_or_404(Site, shortcut=shortcut)
    return redirect(site.site_url)


    