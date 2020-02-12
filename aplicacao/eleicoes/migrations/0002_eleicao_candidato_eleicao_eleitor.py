# Generated by Django 2.2.6 on 2020-02-12 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('eleicoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eleicao_eleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleicao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eleicoes.Eleicao')),
                ('eleitor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao_candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
                ('eleicao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eleicoes.Eleicao')),
            ],
        ),
    ]