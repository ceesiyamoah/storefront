from django.shortcuts import render
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator

# from playground.tasks import notify_customers


class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self, request):
        response = requests.get('http://httpbin.org/delay/2')
        data = response.json()

        return render(request, 'hello.html', {'name': data, 'result': []})

# @cache_page(5*60)
# def say_hello(request):

    # notify_customers.delay('Hello from the outside')
    # return render(request, 'hello.html', {'name': 'Cyril', 'result': []})


# def say_hello(request):

#     try:
#         # send_mail('Test Mail', 'this is the message on everything',
#         #           'info@cyrilyamoah.com', ['ccyamoah@gmail.com'])

#         # message = EmailMessage('Test Mail', 'this is the message on everything',
#         #                        'info@cyrilyamoah.com', ['ccyamoah@gmail.com'])
#         # message.attach_file('playground/static/images/pic.png')
#         # message.send()

#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name': 'Cyril'}
#         )
#         message.send(['ccyamoah@gmail.com'])

#     except BadHeaderError:
#         pass

#     return render(request, 'hello.html', {'name': 'Cyril', 'result': []})
