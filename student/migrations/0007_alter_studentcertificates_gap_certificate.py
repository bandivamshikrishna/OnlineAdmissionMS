# Generated by Django 4.0.3 on 2022-06-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studentcertificates_permanent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcertificates',
            name='gap_certificate',
            field=models.ImageField(blank=True, null=True, upload_to='certificates/'),
        ),
    ]