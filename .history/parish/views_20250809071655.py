from django.shortcuts import render
from .models import Announcement

def home(request):
    announcements = Announcement.objects.order_by('-date')
    return render(request, 'parish/home.html', {'announcements': announcements})
