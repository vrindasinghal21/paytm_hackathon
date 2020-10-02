# Generated by Django 2.1.5 on 2019-01-12 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dropdown',
            fields=[
                ('uniq_id', models.AutoField(primary_key=True, serialize=False)),
                ('field', models.TextField()),
                ('value', models.TextField()),
                ('uid', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('authsize', models.TextField()),
                ('status', models.CharField(default='INSERT', max_length=25000)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('standardsize', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('approval_status', models.CharField(default='PENDING', max_length=10)),
                ('required', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('uniq_id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.BigIntegerField()),
                ('password', models.CharField(default='KIET123', max_length=250)),
                ('email', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='govt_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jyot.Signin'),
        ),
        migrations.AddField(
            model_name='request',
            name='user_id_added_by_uniq_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jyot.Materials'),
        ),
    ]
