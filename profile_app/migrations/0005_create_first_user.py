from django.db import migrations
from django.contrib.auth.hashers import make_password
import os

def create_first_user(apps, _):
    User = apps.get_model('profile_app', 'User')

    username = os.getenv('FIRST_USERNAME')
    password = os.getenv('FIRST_PASSWORD')

    u = User(
        username=username,
        password=make_password(password),
        is_superuser=True,
        user_type='AD'
    )
    u.save()

class Migration(migrations.Migration):
    dependencies = [
        ('profile_app', '0004_alter_user_user_type'),
    ]

    operations = [
        migrations.RunPython(create_first_user),
    ]