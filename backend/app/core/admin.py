from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.apps import apps

# from core import models, resources_models, config_tables_sb_models, reports_models

from .forms import CustomUserCreationForm, CustomUserChangeForm
from core import models


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.User
    list_display = ('soeid', 'is_staff', 'is_active',)
    list_filter = ('soeid', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {
            'fields': (
                'soeid',
                'password'
            ),
        }),
        (_('Personal Info'), {
            'fields': (
                'name',
                'email',
            ),
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff'
            ),
        }),
        (_('Important dates'), {
            'fields': (
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('soeid', 'password1', 'password2', 'email', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('soeid', 'email',)
    ordering = ('soeid', 'email',)


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


admin.site.register(models.User, CustomUserAdmin)

app_models = apps.get_models()

for model in app_models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
