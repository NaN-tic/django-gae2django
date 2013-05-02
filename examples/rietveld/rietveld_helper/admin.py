from django.contrib import admin
from codereview import models


from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from django.contrib.auth.models import User
from rietveld_helper.models import CodereviewProfile


class CodereviewProfileInline(admin.StackedInline):
    """ As you are noticed your profile will be edited as inline form """
    model = CodereviewProfile
    can_delete = False


class UserAdmin(OriginalUserAdmin):
    """ Just add inlines to the original UserAdmin class """
    inlines = [CodereviewProfileInline, ]

try:
    admin.site.unregister(User)
finally:
    admin.site.register(User, UserAdmin)


# Patch in some simple lambda's, Django uses them.
#models.Issue.__unicode__ = lambda self: self.subject
#models.PatchSet.__unicode__ = lambda self: self.message or ''


#class PatchSetInlineAdmin(admin.TabularInline):
#    model = models.PatchSet


#class PatchSetAdmin(admin.ModelAdmin):
#    list_filter = ('issue', 'owner')
#    list_display = ('issue', 'message')
#    search_fields = ('issue__subject', 'message')


#class IssueAdmin(admin.ModelAdmin):
#    list_filter = ('closed', 'owner')
#    list_display = ('id', 'subject', 'owner', 'modified', 'n_comments')
#    list_display_links = ('id', 'subject')
#    inlines = [PatchSetInlineAdmin]

#admin.site.register(models.Issue, IssueAdmin)
#admin.site.register(models.PatchSet, PatchSetAdmin)
