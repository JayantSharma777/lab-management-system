# Generated by Django 3.2.9 on 2022-01-12 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_remove_userleavestatus_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='YearLeaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentTypeLeaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveName', models.CharField(blank=True, max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yearleaves')),
            ],
        ),
    ]
