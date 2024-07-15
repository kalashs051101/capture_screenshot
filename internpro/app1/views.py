from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from .form_submission import submit_to_google_form
from django.shortcuts import render

def submit_form_view(request):
    if request.method == 'POST':
        form_data = {
            'Name': request.POST.get('name'),
            'Contact': request.POST.get('contact_no'),
            'Email': request.POST.get('email'),
            'Address': request.POST.get('Address'),
            'pincode': request.POST.get('pin_code'),
            'Date_of_birth': request.POST.get('DOB'),
            'Gender': request.POST.get('gender'),
            'code': request.POST.get('code'),
        }
        
        screenshot_path = submit_to_google_form(form_data)

        if screenshot_path:
            try:
                # Send email with screenshot attachment
                email = EmailMessage(
                    'Form Submission Confirmation',
                    'Please find attached the screenshot of the confirmation page.',
                    settings.EMAIL_HOST_USER,
                    ['kalash_203057@saitm.org'],  # Replace with your recipient's email
                )
                email.attach_file(screenshot_path)
                email.send()

                return HttpResponse('Form submitted successfully and email sent!')
            except Exception as e:
                return HttpResponse(f'Failed to send email: {e}')
        else:
            return HttpResponse('Failed to submit form to Google Form or capture screenshot!')
    else:
        return render(request, 'submit_form.html')