# Generated by Django 2.1.7 on 2019-02-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='doc_type',
            field=models.IntegerField(choices=[(1, 'Muqavile'), (2, 'Hesab Faktura')], default=0),
            preserve_default=False,
        ),
    ]