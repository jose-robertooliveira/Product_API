# Generated by Django 4.0 on 2021-12-26 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
