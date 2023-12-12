# Generated by Django 4.2.7 on 2023-12-12 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
        ('properties', '0008_commercial_project_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cfacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cproject_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('carpet_area', models.CharField(blank=True, max_length=50)),
                ('floor_plan', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Cproject_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=50)),
                ('carpet_area', models.CharField(blank=True, max_length=50)),
                ('floor_plan', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Rfacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rproject_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Rproject_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=50)),
                ('carpet_area', models.CharField(blank=True, max_length=50)),
                ('floor_plan', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='max_area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='max_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='min_area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='min_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='residential_project',
            name='max_area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='residential_project',
            name='max_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='residential_project',
            name='min_area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='residential_project',
            name='min_price',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='rproject_price',
            name='Residential_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.residential_project'),
        ),
        migrations.AddField(
            model_name='rproject_images',
            name='Residential_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.residential_project'),
        ),
        migrations.AddField(
            model_name='rfacilities',
            name='Residential_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.residential_project'),
        ),
        migrations.AddField(
            model_name='rfacilities',
            name='amenities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.amenities'),
        ),
        migrations.AddField(
            model_name='cproject_price',
            name='Residential_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.residential_project'),
        ),
        migrations.AddField(
            model_name='cproject_images',
            name='Commercial_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.commercial_project'),
        ),
        migrations.AddField(
            model_name='cfacilities',
            name='Commercial_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.commercial_project'),
        ),
        migrations.AddField(
            model_name='cfacilities',
            name='amenities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.amenities'),
        ),
    ]
