# Generated by Django 3.0.3 on 2020-05-23 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tez', '0006_auto_20200507_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guvenlikduvari',
            old_name='wafAdi',
            new_name='isim',
        ),
        migrations.RemoveField(
            model_name='guvenlikduvari',
            name='waf_id',
        ),
        migrations.RemoveField(
            model_name='guvenlikduvari',
            name='yukdengeleyici_id',
        ),
    ]
