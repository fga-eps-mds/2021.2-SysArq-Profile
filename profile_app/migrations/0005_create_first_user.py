from django.db import migrations
from django.contrib.auth.hashers import make_password
import os

def create_first_user(apps, _):
    User = apps.get_model('profile_app', 'User')

    username,  password = os.getenv('FIRST_USER').split(' ')

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