# Generated by Django 2.2.12 on 2020-04-18 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200417_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioEscola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_escola', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='escole_codigo', to='blog.Localidade')),
                ('codigo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EscolaEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Empresa')),
                ('escola_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Escola')),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaTrajeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Empresa')),
                ('trajeto_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Trajeto')),
            ],
        ),
        migrations.CreateModel(
            name='AlunoTrajeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passagens', models.IntegerField()),
                ('dt_mes', models.DateField()),
                ('aluno_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Aluno')),
                ('trajeto_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Trajeto')),
            ],
        ),
        migrations.CreateModel(
            name='AlunoPeriodoEscola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Aluno')),
                ('empresa_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Empresa')),
                ('periodo_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Periodo')),
            ],
        ),
    ]