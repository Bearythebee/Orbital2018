# Generated by Django 2.0.6 on 2018-06-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_remove_showreview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='showlist',
            name='rating',
            field=models.DecimalField(blank=0.0, decimal_places=1, max_digits=11, null=True),
        ),
    ]