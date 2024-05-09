# Generated by Django 3.2 on 2024-05-03 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Mes', '0001_initial'),
        ('TipoValor', '0001_initial'),
        ('Año', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes_anterior', models.CharField(max_length=250)),
                ('mes_año_anterior', models.CharField(max_length=250)),
                ('dic_mes_anterior', models.CharField(max_length=250)),
                ('var_mensual', models.CharField(max_length=250)),
                ('año', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Año.año')),
                ('mes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mes.mes')),
                ('tipo_valor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TipoValor.tipovalor')),
            ],
        ),
    ]
