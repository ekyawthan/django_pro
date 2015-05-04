from django.views.generic import View
from django.http import HttpResponse


class MyView(View):
    greeting = "Good Morning"

    def get(self, request):

        return HttpResponse(self.greeting)
