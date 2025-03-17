from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage


def say_hello(request):

    try:
        # send_mail('Test Mail', 'this is the message on everything',
        #           'info@cyrilyamoah.com', ['ccyamoah@gmail.com'])

        # message = EmailMessage('Test Mail', 'this is the message on everything',
        #                        'info@cyrilyamoah.com', ['ccyamoah@gmail.com'])
        # message.attach_file('playground/static/images/pic.png')
        # message.send()

        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Cyril'}
        )
        message.send(['ccyamoah@gmail.com'])

    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Cyril', 'result': []})
