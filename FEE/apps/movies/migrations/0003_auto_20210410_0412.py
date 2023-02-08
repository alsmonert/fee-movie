# Generated by Django 3.1.7 on 2021-04-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210410_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='cast',
            field=models.CharField(max_length=100, verbose_name='principle cast'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='outline',
            field=models.TextField(verbose_name='plot outline'),
        ),
    ]