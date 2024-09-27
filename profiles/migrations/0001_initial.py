# Generated by Django 4.2.16 on 2024-09-27 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_contact', models.EmailField(max_length=100)),
                ('profile_type', models.IntegerField(choices=[(0, 'Academic'), (2, 'Company'), (3, 'Professional Speleologist'), (4, 'Speleology Enthusiast'), (5, 'Governmental Agency')], default=0)),
                ('bio', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
