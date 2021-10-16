# Generated by Django 3.2.8 on 2021-10-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tittle', models.TextField()),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('SE', 'Sent'), ('FA', 'Failed')], default='PE', max_length=2)),
                ('receivers', models.TextField()),
                ('body', models.TextField()),
            ],
            options={
                'db_table': 'Email',
            },
        ),
    ]
