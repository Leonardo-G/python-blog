# Generated by Django 4.0.4 on 2022-07-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_nosotros'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='Post', max_length=100),
            preserve_default=False,
        ),
    ]