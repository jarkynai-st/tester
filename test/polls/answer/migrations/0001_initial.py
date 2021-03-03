# Generated by Django 3.1.7 on 2021-03-02 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('true_answer', models.CharField(max_length=40)),
                ('poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='answer.polls')),
            ],
        ),
    ]
