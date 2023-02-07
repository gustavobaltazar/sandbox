# Generated by Django 4.1 on 2022-10-03 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_cliente_sexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartao',
            name='cliente',
        ),
        migrations.AddField(
            model_name='cartao',
            name='limite',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='cartao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.cartao'),
            preserve_default=False,
        ),
    ]
