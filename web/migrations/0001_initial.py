# Generated by Django 2.1.7 on 2019-04-29 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10, verbose_name='航班号')),
                ('flight_name', models.CharField(max_length=100, verbose_name='航班名')),
                ('business_class', models.IntegerField(default=0, verbose_name='商务舱座位数')),
                ('tourist_class', models.IntegerField(default=0, verbose_name='经济舱座位数')),
            ],
            options={
                'verbose_name': '飞机信息',
                'verbose_name_plural': '飞机信息',
                'db_table': 'flight',
            },
        ),
        migrations.CreateModel(
            name='FlightLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_city', models.CharField(max_length=10, null=True, verbose_name='出发城市')),
                ('arrive_city', models.CharField(max_length=10, null=True, verbose_name='到达城市')),
                ('start_airport', models.CharField(max_length=10, null=True, verbose_name='起飞机场')),
                ('arrive_airport', models.CharField(max_length=10, null=True, verbose_name='到达机场')),
                ('leave_date', models.DateField(null=True, verbose_name='出发日期')),
                ('leave_time', models.DateTimeField(null=True, verbose_name='出发时间')),
                ('arrive_time', models.DateTimeField(null=True, verbose_name='到达时间')),
                ('fly_time', models.TimeField(null=True, verbose_name='飞行时长')),
                ('business_price', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='商务舱价格')),
                ('tourist_price', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='经济舱价格')),
                ('for_sale', models.IntegerField(null=True, verbose_name='剩余数量')),
                ('already_sale', models.IntegerField(default=0, null=True, verbose_name='已售数量')),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Flight', verbose_name='乘坐飞机')),
            ],
            options={
                'verbose_name': '航线信息',
                'verbose_name_plural': '航线信息',
                'db_table': 'flight_line',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabin', models.IntegerField(choices=[(1, '经济舱'), (2, '商务舱')], null=True, verbose_name='乘坐舱位')),
                ('is_back', models.IntegerField(choices=[(1, '已订票'), (0, '已退票')], default=1, null=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now=True, null=True)),
                ('flight_line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.FlightLine', verbose_name='乘坐航班')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='用户名')),
                ('real_name', models.CharField(max_length=10, verbose_name='乘客姓名')),
                ('password', models.CharField(max_length=255)),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='注册时间')),
                ('sex', models.IntegerField(choices=[(1, '男'), (0, '女')], verbose_name='性别')),
                ('card_id', models.CharField(max_length=18, verbose_name='身份证号')),
            ],
            options={
                'verbose_name': '乘客信息',
                'verbose_name_plural': '乘客信息',
                'db_table': 'passenger',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='passenger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Passenger', verbose_name='乘客'),
        ),
    ]
