# Generated by Django 4.1 on 2022-09-06 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoa', '0004_alter_profile_intolerancia_a_gluten_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]