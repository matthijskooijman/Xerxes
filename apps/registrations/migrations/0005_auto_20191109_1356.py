# Generated by Django 2.2.7 on 2019-11-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_auto_20191109_1355'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='registrationfieldvalue',
            constraint=models.UniqueConstraint(fields=('registration', 'field'), name='one_value_per_field_per_registration'),
        ),
    ]