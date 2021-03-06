# Generated by Django 3.1.6 on 2021-02-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='lahijan', verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='taghi taghizade', max_length=200, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='test@tes.te', max_length=254, unique=True, verbose_name='ایمیل'),
        ),
    ]
