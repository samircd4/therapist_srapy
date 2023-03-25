from django.shortcuts import render
from .models import Profile
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def main(request):
    return render(request, 'core/index.html')

def search(request):
    q = ''
    if 'q' in request.GET:
        q = request.GET['q']
        profiles = Profile.objects.filter(Q(name__icontains=q) | Q(city__icontains=q) | Q(zip__icontains=q)).order_by('name')
    else:
        profiles = Profile.objects.filter(Q(name__icontains=q)).order_by('name')
    paginator = Paginator(profiles, per_page=20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    page_range = page.paginator.page_range
    context={
        'profiles':page,
        'page_range':page_range,
    }
    return render(request, 'search.html', context)

def addProfile(request):
    ...