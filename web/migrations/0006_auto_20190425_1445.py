# Generated by Django 2.1.7 on 2019-04-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20190417_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportid', models.IntegerField()),
                ('taskid', models.IntegerField()),
                ('caseid', models.IntegerField()),
                ('casestate', models.IntegerField()),
                ('requestinfo', models.TextField()),
                ('log', models.TextField()),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.IntegerField()),
                ('casenumber', models.IntegerField()),
                ('passnumber', models.IntegerField()),
                ('failnumber', models.IntegerField()),
                ('passrate', models.FloatField()),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='case',
            name='relatedtask',
        ),
        migrations.AddField(
            model_name='case',
            name='taskid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='caseid',
            field=models.IntegerField(null=True),
        ),
    ]
