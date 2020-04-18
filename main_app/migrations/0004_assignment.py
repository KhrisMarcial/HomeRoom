# Generated by Django 3.0.4 on 2020-04-18 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('grade', models.IntegerField()),
                ('date_created', models.DateField(verbose_name='date created')),
                ('due_date', models.DateField(verbose_name='due date')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Classroom')),
            ],
        ),
    ]
