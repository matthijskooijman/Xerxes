# Generated by Django 2.2.24 on 2022-04-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(help_text='For pending payments, this is the creation timestamp', verbose_name='Transaction date/time'),
        ),
    ]