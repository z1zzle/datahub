# Generated by Django 5.0.7 on 2024-07-24 19:52

from django.db import migrations, models
from django.utils.text import slugify

from datalayers.models import Category

def migrate_data_forward(apps, schema_editor):
    for instance in Category.objects.all():
        instance.key = slugify(instance.name)
        instance.save()

def migrate_data_backward(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('datalayers', '0002_alter_datalayersource_datalayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='key',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),
        migrations.AlterField(
            model_name='category',
            name='key',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]