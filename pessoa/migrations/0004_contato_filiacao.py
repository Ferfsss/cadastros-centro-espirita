# Generated by Django 4.1.1 on 2022-10-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_dadospessoa_contato_alugado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='filiacao',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]
