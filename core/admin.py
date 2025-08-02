from django.contrib import admin
from .models import Program, ContentPage, LetterSubscription, ContactFormSubmission, NotifyVistors


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):   
    pass

@admin.register(ContentPage)
class ContentPageAdmin(admin.ModelAdmin):
    pass

@admin.register(LetterSubscription)
class LetterSubscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    pass

@admin.register(NotifyVistors)
class NotifyVistorsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'created', 'modified')
    search_fields = ('email', 'phone')
    list_filter = ('created', 'modified')
    ordering = ('-created',)
    