# Generated by Django 2.1.4 on 2020-04-26 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200426_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunotrajeto',
            name='dt_mes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.Periodo'),
        ),
    ]
