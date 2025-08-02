from django.contrib import messages
from django.shortcuts import redirect, render
from core.models import ContactFormSubmission, LetterSubscription, NotifyVistors
from gallery.models import GalleryImage  # Assuming you have a gallery app with GalleryImage model

def home(request):
    featured_GalleryImages = GalleryImage.objects.filter(featured=True)[:8]
    return render(request, 'core/home.html', {'featured_GalleryImages': featured_GalleryImages})

def about(request):
    return render(request, 'core/about.html')

def programs(request):
    return render(request, 'core/programs.html')

def contact(request):
    return render(request, 'core/contact.html')

def donate(request):
    return render(request, 'core/donate.html')

def handle_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Received contact form submission: Name: {name}, Email: {email}, Subject: {subject}, Phone: {phone}, Message: {message}")

        if name and email and message:
            # Here you would typically save the contact form data to the database or send an email
            ContactFormSubmission.objects.create(
                name=name,
                email=email,
                subject=subject,
                phone=phone,
                message=message
            )
            messages.success(request, "Thank you for contacting us!")
        else:
            messages.error(request, "Please fill in all fields.")
    
    return redirect('contact')

def handle_letter_subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscription, created = LetterSubscription.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please provide a valid email address.")
    return redirect('home')

def handle_notify_visitors(request):
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        country_code = request.POST.get('countryCode')
        phone_number = request.POST.get('phone')
        
        # Combine country code and phone number
        full_phone = f"{country_code}{phone_number}" if phone_number else None
        
        # Validate at least one contact method is provided
        if not email and not phone_number:
            messages.error(request, "Please provide at least an email or phone number.")
            return redirect('donate')
        
        # Validate at least one consent is given
        email_consent = 'email-consent' in request.POST
        whatsapp_consent = 'whatsapp-consent' in request.POST
        
        if not email_consent and not whatsapp_consent:
            messages.error(request, "Please select at least one notification method.")
            return redirect('donate')
        
        # Save to database
        try:
            # Create or update notification preference
            obj, created = NotifyVistors.objects.update_or_create(
                email=email if email else None,
                defaults={
                    'phone': full_phone,
                    'email': email,
                    # 'whatsapp_consent': whatsapp_consent
                }
            )
            
            # Prepare success message
            message = "You will be notified of updates!"
            if email_consent and email:
                message += f" We'll email you at {email}."
            if whatsapp_consent and full_phone:
                message += f" We'll WhatsApp you at {full_phone}."
                
            messages.success(request, message)
            return redirect('donate')
            
        except Exception as e:
            messages.error(request, f"Error saving your information: {str(e)}")
            return redirect('donate')
        
    return redirect('donate')


def handle_404(request, exception):
    return render(request, 'core/404.html', status=404)

def handle_500(request):
    return render(request, 'core/500.html', status=500)

