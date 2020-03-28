from django.shortcuts import render
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def index(request):
	if request.method == 'POST':
		email = request.POST['email']

		# Sending Email
		subject = 'EarnXtraCash Mail'
		html_message = render_to_string('website/mail_template.html', {'email': email})
		plain_message = strip_tags(html_message)
		from_email = 'tom.nyone@outlook.com'
		to = 'tomnyone@outlook.com'
		mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

		return render(request, 'website/thanks.html', {'email': email})

	else:
		return render(request, 'website/index.html', {})


def HomeView(request):
	return render(request, 'website/home.html', {})
