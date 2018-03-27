from django.shortcuts import render, reverse
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'my_blog/index.html')
