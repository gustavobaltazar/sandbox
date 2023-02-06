# Generated by Django 4.1 on 2022-08-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso_bosch', models.CharField(max_length=50)),
                ('nome_curso_senai', models.CharField(max_length=50)),
                ('duracao_bosch', models.IntegerField()),
                ('duracao_senai', models.IntegerField()),
                ('qtd_aprendizs', models.IntegerField()),
                ('descritivo', models.TextField()),
                ('mais_informacoes', models.CharField(max_length=100)),
            ],
        ),
    ]