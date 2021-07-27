# Generated by Django 3.2.5 on 2021-07-27 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('departamentos', '0003_alter_departamento_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]