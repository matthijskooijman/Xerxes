# Generated by Django 2.2.13 on 2021-08-27 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0007_convert_field_type_to_konst'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationfield',
            options={'ordering': ('order', 'id'), 'verbose_name': 'registration field', 'verbose_name_plural': 'registration fields'},
        ),
        migrations.AlterModelOptions(
            name='registrationfieldoption',
            options={'ordering': ('order', 'id'), 'verbose_name': 'registration field option', 'verbose_name_plural': 'registration field options'},
        ),
    ]
