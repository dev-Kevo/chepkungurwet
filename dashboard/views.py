from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from donations.models import Donation
from core.models import Program, ContentPage
from django.contrib.auth import get_user_model
from gallery.models import GalleryImage
from django.contrib.auth import logout, authenticate, login


def admin_check(user):
    return user.is_authenticated and user.is_staff

def account_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting login for user: {username}")  # Debugging line
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'admin/login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin/login.html')

def account_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('account_login')

# Base Admin View
class AdminBaseView(View):
    template_name = None
    page_title = "Admin"
    
    @method_decorator(login_required)
    @method_decorator(user_passes_test(admin_check))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = kwargs
        context['page_title'] = self.page_title
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

# Dashboard View
class DashboardView(AdminBaseView):
    template_name = 'admin/dashboard.html'
    page_title = "Dashboard Overview"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        User = get_user_model()
        
        # Add dashboard statistics
        context.update({
            'total_donations': Donation.objects.total_amount(),
            'recent_activity': self.get_recent_activity(),
        })
        return context
    
    def get_recent_activity(self):
        # This would be replaced with actual recent activity logic
        return [
            {'type': 'donation', 'message': 'New $500 donation received', 'time': '2 hours ago'},
            {'type': 'volunteer', 'message': 'New volunteer registered', 'time': '5 hours ago'},
            {'type': 'gallery', 'message': '5 new photos added', 'time': '1 day ago'},
        ]

# Donations Management View
class DonationsAdminView(AdminBaseView):
    template_name = 'admin/donations_admin.html'
    page_title = "Donations Management"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donations = Donation.objects.all().select_related('donor', 'program').order_by('-date')
        
        context.update({
            'donations': donations,
            # 'total_amount': sum(d.amount for d in donations),
        })
        return context

class MessagesAdminView(AdminBaseView):
    template_name = 'admin/messages_admin.html'
    page_title = "Messages Management"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            'messages': messages,
        })
        return context

# Programs Management View
class ProgramsAdminView(AdminBaseView):
    template_name = 'admin/programs_admin.html'
    page_title = "Programs Management"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        programs = Program.objects.all().prefetch_related('beneficiaries')
        
        context.update({
            'programs': programs,
            # 'active_count': programs.filter(is_active=True).count(),
        })
        return context

# Gallery Management View
class GalleryAdminView(AdminBaseView):
    template_name = 'admin/gallery_admin.html'
    page_title = "Gallery Management"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = GalleryImage.objects.all().select_related('program')
        
        context.update({
            'images': images,
            'programs': Program.objects.all(),
        })
        return context

# Content Management View
class ContentManagementView(AdminBaseView):
    template_name = 'admin/content_management.html'
    page_title = "Content Management"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pages = ContentPage.objects.all()
        
        context.update({
            'pages': pages,
        })
        return context

# User Management View
class UserManagementView(AdminBaseView):
    template_name = 'admin/user_management.html'
    page_title = "User Management"


# Settings View
class SettingsView(AdminBaseView):
    template_name = 'admin/settings.html'
    page_title = "Settings"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any settings-related context here
        return context