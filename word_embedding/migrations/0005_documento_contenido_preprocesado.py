# Generated by Django 4.2.6 on 2023-11-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_embedding', '0004_alter_documento_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='contenido_preprocesado',
            field=models.TextField(blank=True, null=True),
        ),
    ]
