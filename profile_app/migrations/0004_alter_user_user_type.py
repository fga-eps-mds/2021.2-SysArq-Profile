# Generated by Django 3.2.6 on 2022-03-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('AD', 'Administrador'), ('AL', 'Alimentador'), ('VI', 'Visualizador')], default='VI', max_length=2),
        ),
    ]
