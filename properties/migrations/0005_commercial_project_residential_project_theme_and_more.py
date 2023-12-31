# Generated by Django 4.2.7 on 2023-12-11 02:44

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_residential_project_meta_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propert_type', models.CharField(choices=[('Residential Land', 'Residential Land'), ('Residential Apartment', 'Residential Apartment'), ('Independent House/Villa', 'Independent House/Villa'), ('Studio Apartment', 'Studio Apartment'), ('Independent/Builder Floor', 'Independent/Builder Floor'), ('Serviced Apartments', 'Serviced Apartments'), ('Farm House', 'Farm House')], max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=25)),
                ('construction_status', models.CharField(choices=[('Under Construction', 'Under Construction'), ('New Launch', 'New Launch'), ('Partially Ready To Move', 'Partially Ready To Move'), ('Ready To Move', 'Ready To Move')], max_length=25)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='residential_project',
            name='theme',
            field=models.CharField(choices=[('Theme1', 'Theme1'), ('Theme2', 'Theme2'), ('Theme3', 'Theme3'), ('Theme4', 'Theme4'), ('Theme5', 'Theme5')], default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='developer',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='locality',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='locality',
            name='keywords',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='residential_project',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='residential_project',
            name='propert_type',
            field=models.CharField(choices=[('Office Space', 'Office Space'), ('Shop/Showroom', 'Shop/Showroom'), ('Commercial Land', 'Commercial Land'), ('Warehouse/Godown', 'Warehouse/Godown'), ('Industrial Building', 'Industrial Building'), ('Industrial Shed', 'Industrial Shed')], max_length=25),
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propert_type', models.CharField(choices=[('Residential Plot', 'Residential Plot'), ('Commercial land', 'Commercial land'), ('Agricultural Land', 'Agricultural Land')], max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=25)),
                ('construction_status', models.CharField(choices=[('Under Construction', 'Under Construction'), ('New Launch', 'New Launch'), ('Partially Ready To Move', 'Partially Ready To Move'), ('Ready To Move', 'Ready To Move')], max_length=25)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.city')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.developer')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.locality')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='properties.plat')),
                ('possession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.possession_in')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Commercial_Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.commercial_project')),
                ('Plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.plat')),
                ('Residential_Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.residential_project')),
            ],
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.city'),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.developer'),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.locality'),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='properties.commercial_project'),
        ),
        migrations.AddField(
            model_name='commercial_project',
            name='possession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.possession_in'),
        ),
    ]
