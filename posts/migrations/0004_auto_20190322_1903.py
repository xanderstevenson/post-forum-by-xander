# Generated by Django 2.1.7 on 2019-03-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190322_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(default='dstatic/default.png', upload_to='static/'),
        ),
    ]
