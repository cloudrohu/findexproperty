# Generated by Django 4.2.7 on 2023-12-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_alter_developer_address_alter_developer_contact_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercial_project',
            name='theme',
            field=models.CharField(choices=[('Theme1', 'Theme1'), ('Theme2', 'Theme2'), ('Theme3', 'Theme3'), ('Theme4', 'Theme4'), ('Theme5', 'Theme5')], default=1, max_length=25),
            preserve_default=False,
        ),
    ]
