from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'article/index.html', context={
            'app': 'Article'
        })


class CustomView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'article/custom.html', context=kwargs)
