# Generated by Django 2.2.9 on 2020-04-02 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djpmp', '0004_wbs_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='man_day_price',
            field=models.FloatField(default=0, verbose_name='人天单价'),
        ),
    ]