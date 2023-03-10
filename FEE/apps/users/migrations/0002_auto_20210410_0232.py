# Generated by Django 3.1.7 on 2021-04-10 02:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='authority',
            field=models.IntegerField(default=0, verbose_name='authority'),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(default='dummy@gmail.com', max_length=254, verbose_name='user email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.IntegerField(default=0, verbose_name='user id'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
