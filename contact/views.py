from django.shortcuts import render, redirect
from contact.models import Contact, Inquiry
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact_name = request.POST['contact_name']
        contact_phone = request.POST['contact_phone']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']

        contact = Contact(contact_name=contact_name, contact_phone=contact_phone, contact_email=contact_email,
                          contact_message=contact_message)
        contact.save()

        send_mail(
            'Restaurant Contact Message',
            'You have gotten a message from ' + contact_name + '. Sign into the Admin Panel to see it!',
            'emmandukwe26@gmail.com',
            ['ellamoves01@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your Message has been successfully sent. We will get in Touch with you in 48 hours!')

    return render(request, 'contact/contact.html')


def inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        people = request.POST['people']
        date = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']

        inquiry = Inquiry(name=name, email=email, phone=phone, people=people, date=date, time=time, message=message)

        inquiry.save()


        send_mail(
            subject='Restaurant Contact Message',
            message=f'A reservation has been made by {name} for {people} on {date} at {time}pm.\n'
                    f'Message: {message}',
            from_email='emmandukwe26@gmail.com',
            recipient_list=['ellamoves01@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Reservation has been successfully sent. '
                                  'An email will be send to confirm your reservation')

        return redirect(to='index')
    else:
        return render(request, 'pages/index.html')