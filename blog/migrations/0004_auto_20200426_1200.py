# Generated by Django 2.1.4 on 2020-04-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_aluno_trajeto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunotrajeto',
            name='passagens',
            field=models.IntegerField(null=True),
        ),
    ]