# Generated by Django 2.2.24 on 2022-06-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_medical_details_fix_description_typo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaldetails',
            name='food_allergies',
            field=models.TextField(blank=True, help_text='Please specify any allergies or other restrictions our kitchen staff should take into account. Please also mention the severity. Do not use this field for food you dislike (we cannot accomodate that), only enter things that can cause real problems. Leave blank when you have no allergies.', verbose_name='Food allergies'),
        ),
    ]