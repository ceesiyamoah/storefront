from django.shortcuts import render
import requests
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
# from playground.tasks import notify_customers


logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('http://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')

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
