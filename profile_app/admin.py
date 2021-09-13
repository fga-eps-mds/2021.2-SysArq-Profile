from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'first_name', 'last_name', 'cpf')
    list_filter = ('username', 'first_name', 'is_superuser', )
    list_display = ('username', 'first_name',
                    'last_name', 'cpf')
    # fieldsets = (
    #     (None, {'fields': ('username', 'first_name', 'last_name', 'cpf',)}),
    #     ('Permissions', {'fields': ('is_superuser')}),
    # )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name',
                       'cpf', 'password1', 'password2', 'is_superuser')}
         ),
    )


admin.site.register(User, UserAdminConfig)