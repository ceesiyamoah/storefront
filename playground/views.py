from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage


def say_hello(request):

    try:
        # send_mail('Test Mail', 'this is the message on everything',
        #           'info@cyrilyamoah.com', ['ccyamoah@gmail.com'])
        message = EmailMessage('Test Mail', 'this is the message on everything',
                               'info@cyrilyamoah.com', ['ccyamoah@gmail.com'])
        message.attach_file('playground/static/images/pic.png')
        message.send()

    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Cyril', 'result': []})
