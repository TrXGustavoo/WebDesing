# Generated by Django 4.1 on 2022-09-02 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_rename_alegia_glt_profile_alegia_gluten_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='alegia_Gluten',
            new_name='intolerancia_a_Gluten',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='alegia_Lactose',
            new_name='intolerancia_a_Lactose',
        ),
    ]
