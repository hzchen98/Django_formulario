# Generated by Django 3.0.5 on 2020-05-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genpdf',
            name='origin_pdf',
            field=models.FileField(upload_to='polls/upload'),
        ),
    ]
