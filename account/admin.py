from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm


User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'password', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        ('ユーザー情報', {'fields': ('email', 'password')}),
        ('権限付与', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    ordering = ('email',)

admin.site.unregister(Group)
admin.site.register(User, CustomizeUserAdmin)
