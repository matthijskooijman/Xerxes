# Generated by Django 2.0.5 on 2018-05-19 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Registered'), (1, 'Waiting list'), (2, 'Cancelled')], verbose_name='Status')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'registrations',
                'verbose_name': 'registration',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(through='events.Registration', to=settings.AUTH_USER_MODEL),
        ),
    ]
