# Generated by Django 5.1.3 on 2025-01-14 15:40

from django.db import migrations, models

from shapes.models import Shape

def migrate_data_forward(apps, schema_editor):
    for instance in Shape.objects.all():
        instance.key = str(instance.id)
        instance.save()

def migrate_data_backward(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='license',
            field=models.TextField(blank=True, help_text='SPDX identifier of the license if available.'),
        ),
        migrations.AlterField(
            model_name='shape',
            name='attribution_text',
            field=models.TextField(blank=True),
        ),

        migrations.AddField(
            model_name='shape',
            name='admin',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shape',
            name='attribution_html',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='shape',
            name='key',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),

        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),

        migrations.AlterField(
            model_name='shape',
            name='key',
            field=models.SlugField(max_length=255,  null=False, unique=True),
        ),
    ]