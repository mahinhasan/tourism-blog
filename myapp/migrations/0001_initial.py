# Generated by Django 2.1.5 on 2021-11-03 09:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('details', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]