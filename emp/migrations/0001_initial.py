# Generated by Django 4.0.2 on 2022-02-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpMaster',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('gender', models.CharField(max_length=1)),
                ('deptno', models.IntegerField()),
            ],
        ),
    ]