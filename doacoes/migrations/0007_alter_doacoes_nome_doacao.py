# Generated by Django 4.1.1 on 2022-11-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0006_alter_doacoes_calc_numero_homem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacoes',
            name='nome_doacao',
            field=models.CharField(max_length=256),
        ),
    ]