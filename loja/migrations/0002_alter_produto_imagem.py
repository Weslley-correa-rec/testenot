# Generated by Django 5.0.6 on 2024-07-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, max_length=400, null=True, upload_to=''),
        ),
    ]
