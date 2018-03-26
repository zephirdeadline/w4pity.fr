# Generated by Django 2.0.2 on 2018-02-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_site_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='subTitle',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]