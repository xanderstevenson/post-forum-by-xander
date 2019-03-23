# Generated by Django 2.1.7 on 2019-03-20 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='categories.Categories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
