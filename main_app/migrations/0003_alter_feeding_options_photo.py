# Generated by Django 4.2.3 on 2023-08-03 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_finch_habitat_feeding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
        ),
    ]
