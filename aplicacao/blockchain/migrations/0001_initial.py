# Generated by Django 2.2.6 on 2020-03-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block_eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.CharField(max_length=26)),
                ('data', models.CharField(max_length=200)),
                ('previous_hash', models.CharField(max_length=64)),
                ('hash', models.CharField(max_length=64)),
            ],
        ),
    ]