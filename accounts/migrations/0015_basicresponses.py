# Generated by Django 2.1.11 on 2020-08-13 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_merge_20190821_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans1', models.TextField(default='')),
                ('ans2', models.TextField(default='')),
                ('ans3', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
    ]
