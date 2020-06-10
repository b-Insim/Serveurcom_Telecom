# Generated by Django 2.1.7 on 2020-06-10 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bars',
            name='comptoir',
        ),
        migrations.AlterField(
            model_name='comptoir',
            name='bars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bars'),
        ),
    ]
