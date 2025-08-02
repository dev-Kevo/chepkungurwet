from django.urls import path
from .views import (
    DashboardView, DonationsAdminView, MessagesAdminView, ProgramsAdminView, 
    GalleryAdminView, ContentManagementView, UserManagementView, SettingsView, account_login, account_logout
)

urlpatterns = [

    path('login/', account_login, name='account_login'),
    path('logout/', account_logout, name='admin_logout'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('donations/', DonationsAdminView.as_view(), name='donations_admin'),
    path('messages/', MessagesAdminView.as_view(), name='messages_admin'),
    path('programs/', ProgramsAdminView.as_view(), name='programs_admin'),
    path('gallery/', GalleryAdminView.as_view(), name='gallery_admin'),
    path('content/', ContentManagementView.as_view(), name='content_management'),
    path('users/', UserManagementView.as_view(), name='user_management'),
    path('settings/', SettingsView.as_view(), name='settings'),
    
    # Add other admin URLs as needed
]