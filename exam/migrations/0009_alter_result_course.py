# Generated by Django 4.0.3 on 2022-06-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_alter_result_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.course'),
        ),
    ]
