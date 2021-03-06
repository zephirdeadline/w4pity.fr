# Generated by Django 2.0.2 on 2018-02-15 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='/static/upload/montagne.jpg', upload_to='static/upload/'),
            preserve_default=False,
        ),
    ]
