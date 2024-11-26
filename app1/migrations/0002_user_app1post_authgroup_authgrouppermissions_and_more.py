# Generated by Django 5.1.3 on 2024-11-26 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='USERID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(db_column='Email', max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('f', models.CharField(blank=True, db_column='F', max_length=1, null=True)),
                ('s', models.CharField(blank=True, db_column='S', max_length=1, null=True)),
                ('n', models.CharField(blank=True, db_column='N', max_length=1, null=True)),
                ('w', models.CharField(blank=True, db_column='W', max_length=1, null=True)),
                ('c', models.CharField(blank=True, db_column='C', max_length=1, null=True)),
                ('d', models.CharField(blank=True, db_column='D', max_length=1, null=True)),
                ('r', models.CharField(blank=True, db_column='R', max_length=1, null=True)),
                ('a', models.CharField(blank=True, db_column='A', max_length=1, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'app1_post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('b_number', models.AutoField(db_column='B_Number', primary_key=True, serialize=False)),
                ('product_amount', models.DecimalField(db_column='Product_Amount', decimal_places=2, max_digits=10)),
                ('sell', models.IntegerField(blank=True, db_column='SELL', null=True)),
                ('store', models.IntegerField(blank=True, db_column='STORE', null=True)),
                ('optimum_temperature_to_store', models.DecimalField(blank=True, db_column='Optimum_temperature_to_store', decimal_places=2, max_digits=5, null=True)),
                ('optimum_humidity_to_store', models.DecimalField(blank=True, db_column='Optimum_humidity_to_store', decimal_places=2, max_digits=5, null=True)),
                ('product_unit_price', models.DecimalField(db_column='Product_Unit_price', decimal_places=2, max_digits=10)),
                ('kg', models.DecimalField(blank=True, db_column='KG', decimal_places=2, max_digits=10, null=True)),
                ('ton', models.DecimalField(blank=True, db_column='TON', decimal_places=2, max_digits=10, null=True)),
                ('mon', models.DecimalField(blank=True, db_column='MON', decimal_places=2, max_digits=10, null=True)),
                ('batch_description', models.TextField(blank=True, db_column='Batch_Description', null=True)),
                ('date_time_batch_created', models.DateTimeField(db_column='Date_Time_Batch_Created')),
            ],
            options={
                'db_table': 'batch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseRequest',
            fields=[
                ('pid', models.AutoField(db_column='PID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('unitprice', models.DecimalField(db_column='UnitPrice', decimal_places=2, max_digits=10)),
                ('p_date', models.DateField(db_column='P_Date')),
                ('payment_status', models.CharField(db_column='Payment_Status', max_length=50)),
            ],
            options={
                'db_table': 'purchase_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('hid', models.AutoField(db_column='HID', primary_key=True, serialize=False)),
                ('season', models.CharField(db_column='SEASON', max_length=50)),
                ('qualitygrade', models.CharField(blank=True, db_column='QualityGrade', max_length=10, null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'harvest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HarvestFields',
            fields=[
                ('fields_id', models.AutoField(db_column='FIELDS_ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'harvest_fields',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensorid', models.AutoField(db_column='SensorID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('nextservingdate', models.DateField(blank=True, db_column='NextServingDate', null=True)),
                ('lastphysicalcheckeddate', models.DateField(blank=True, db_column='LastPhysicalCheckedDate', null=True)),
            ],
            options={
                'db_table': 'sensor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('lid', models.AutoField(db_column='LID', primary_key=True, serialize=False)),
                ('v_yes', models.IntegerField(blank=True, db_column='V_YES', null=True)),
                ('v_no', models.IntegerField(blank=True, db_column='V_NO', null=True)),
                ('why_loan_need', models.TextField(blank=True, db_column='WHY_LOAN_NEED', null=True)),
                ('amount', models.DecimalField(db_column='AMOUNT', decimal_places=2, max_digits=10)),
                ('video_link', models.CharField(blank=True, db_column='Video_Link', max_length=2083, null=True)),
            ],
            options={
                'db_table': 'loan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(db_column='Location_ID', primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(blank=True, db_column='Latitude', decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, db_column='Longitude', decimal_places=6, max_digits=9, null=True)),
                ('street', models.CharField(blank=True, db_column='Street', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=100, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=100, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=100, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=20, null=True)),
                ('altitude', models.IntegerField(blank=True, db_column='Altitude', null=True)),
                ('timezone', models.CharField(blank=True, db_column='Timezone', max_length=100, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MarketPlace',
            fields=[
                ('market_id', models.AutoField(db_column='MARKET_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('traditional', models.IntegerField(blank=True, db_column='Traditional', null=True)),
                ('wholeseller', models.IntegerField(blank=True, db_column='Wholeseller', null=True)),
                ('starttime', models.TimeField(db_column='StartTime')),
                ('endtime', models.TimeField(db_column='EndTime')),
            ],
            options={
                'db_table': 'market_place',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(db_column='Product_ID', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='Product_Name', max_length=255)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SampleResult',
            fields=[
                ('certifications_id', models.AutoField(db_column='CERTIFICATIONS_ID', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('status', models.CharField(db_column='Status', max_length=50)),
                ('certification_details', models.TextField(blank=True, db_column='Certification_Details', null=True)),
            ],
            options={
                'db_table': 'sample_result',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('seed_id', models.AutoField(db_column='SEED_ID', primary_key=True, serialize=False)),
                ('type_of_seed_name', models.CharField(blank=True, db_column='Type_of_Seed_name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'seed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeedStock',
            fields=[
                ('seed_stock_id', models.AutoField(db_column='Seed_Stock_id', primary_key=True, serialize=False)),
                ('stock_seed_expirydate', models.DateField(blank=True, db_column='Stock_Seed_ExpiryDate', null=True)),
                ('stock_quantity_total', models.IntegerField(blank=True, db_column='Stock_Quantity_Total', null=True)),
            ],
            options={
                'db_table': 'seed_stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wirehouse',
            fields=[
                ('warehousehouseid', models.AutoField(db_column='WarehouseHouseID', primary_key=True, serialize=False)),
                ('warehousename', models.CharField(blank=True, db_column='WarehouseName', max_length=255, null=True)),
                ('warehousenumber', models.CharField(blank=True, db_column='WarehouseNumber', max_length=100, null=True)),
            ],
            options={
                'db_table': 'wirehouse',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.CreateModel(
            name='AgriculturalOfficer',
            fields=[
                ('aid', models.OneToOneField(db_column='AID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
                ('region', models.CharField(blank=True, db_column='Region', max_length=255, null=True)),
            ],
            options={
                'db_table': 'agricultural_officer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.OneToOneField(db_column='CID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DistributorCompany',
            fields=[
                ('did', models.OneToOneField(db_column='DID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
            ],
            options={
                'db_table': 'distributor_company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('fid', models.OneToOneField(db_column='FID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
            ],
            options={
                'db_table': 'farmer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nutritionists',
            fields=[
                ('nid', models.OneToOneField(db_column='NID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
            ],
            options={
                'db_table': 'nutritionists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('rid', models.OneToOneField(db_column='RID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
                ('storename', models.CharField(blank=True, db_column='StoreName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'retailer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('sid', models.OneToOneField(db_column='SID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WirehouseManager',
            fields=[
                ('wid', models.OneToOneField(db_column='WID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.user')),
            ],
            options={
                'db_table': 'wirehouse_manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BatchPurchaseRequest',
            fields=[
                ('pid', models.OneToOneField(db_column='PID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.purchaserequest')),
            ],
            options={
                'db_table': 'batch_purchase_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('pid', models.OneToOneField(db_column='PID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.purchaserequest')),
                ('d_time_date', models.DateTimeField(db_column='D_Time_DATE')),
                ('delivery_status', models.CharField(db_column='Delivery_Status', max_length=50)),
                ('delivered_by', models.CharField(blank=True, db_column='Delivered_By', max_length=255, null=True)),
                ('is_pickedup', models.IntegerField(blank=True, db_column='IS_PickedUp', null=True)),
                ('is_on_the_way', models.IntegerField(blank=True, db_column='IS_on_the_Way', null=True)),
                ('fromwherepickup_loc', models.CharField(blank=True, db_column='FromWherePickup_Loc', max_length=255, null=True)),
                ('delivery_address', models.CharField(blank=True, db_column='Delivery_Address', max_length=255, null=True)),
                ('is_satisfy_customer', models.IntegerField(blank=True, db_column='IS_satisfy_Customer', null=True)),
                ('delivery_method', models.CharField(blank=True, db_column='Delivery_Method', max_length=50, null=True)),
            ],
            options={
                'db_table': 'delivery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HarvestHarvestFields',
            fields=[
                ('hid', models.OneToOneField(db_column='HID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.harvest')),
                ('time_date_of_harvest_from_fields', models.DateTimeField(db_column='TIME_DATE_OF_Harvest_From_Fields')),
                ('quantity', models.DecimalField(db_column='Quantity', decimal_places=2, max_digits=10)),
                ('unitofmeasure', models.CharField(db_column='UnitOfMeasure', max_length=50)),
            ],
            options={
                'db_table': 'harvest_harvest_fields',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HarvestFieldsCropsType',
            fields=[
                ('fields', models.OneToOneField(db_column='FIELDS_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.harvestfields')),
                ('crop_type', models.CharField(db_column='CROP_TYPE', max_length=255)),
            ],
            options={
                'db_table': 'harvest_fields_crops_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HarvestFieldsSoilType',
            fields=[
                ('fields', models.OneToOneField(db_column='FIELDS_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.harvestfields')),
                ('soil_type', models.CharField(db_column='SOIL_TYPE', max_length=255)),
            ],
            options={
                'db_table': 'harvest_fields_soil_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LiveTemperatureHumidityMonitoringOfProductBatches',
            fields=[
                ('humidity', models.DecimalField(db_column='Humidity', decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(db_column='Temperature', decimal_places=2, max_digits=5)),
                ('sid', models.OneToOneField(db_column='SID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.sensor')),
                ('recorded_time', models.DateTimeField(db_column='Recorded_Time')),
            ],
            options={
                'db_table': 'live_temperature_humidity_monitoring_of_product_batches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MarketPlaceProductSold',
            fields=[
                ('market', models.OneToOneField(db_column='MARKET_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.marketplace')),
                ('products_sold', models.CharField(db_column='Products_Sold', max_length=255)),
            ],
            options={
                'db_table': 'market_place_product_sold',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loan20',
            fields=[
                ('aid', models.OneToOneField(db_column='AID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.agriculturalofficer')),
                ('timedate', models.DateTimeField(db_column='TIMEDATE')),
                ('notes', models.TextField(blank=True, db_column='NOTES', null=True)),
            ],
            options={
                'db_table': 'loan2_0',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeedStock20',
            fields=[
                ('aid', models.OneToOneField(db_column='AID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.agriculturalofficer')),
                ('distributed_date_time', models.DateTimeField(db_column='DISTRIBUTED_DATE_Time')),
            ],
            options={
                'db_table': 'seed_stock_2_0',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DistributorCompanyDemandForProduct',
            fields=[
                ('did', models.OneToOneField(db_column='DID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.distributorcompany')),
                ('demandamount', models.DecimalField(db_column='DemandAmount', decimal_places=2, max_digits=10)),
                ('ton', models.DecimalField(blank=True, db_column='TON', decimal_places=2, max_digits=10, null=True)),
                ('mon', models.DecimalField(blank=True, db_column='MON', decimal_places=2, max_digits=10, null=True)),
                ('kg', models.DecimalField(blank=True, db_column='KG', decimal_places=2, max_digits=10, null=True)),
                ('demand_date_time', models.DateTimeField(db_column='Demand_Date_Time')),
                ('city', models.CharField(blank=True, db_column='CITY', max_length=100, null=True)),
                ('state', models.CharField(blank=True, db_column='STATE', max_length=100, null=True)),
                ('area', models.CharField(blank=True, db_column='AREA', max_length=255, null=True)),
                ('season', models.CharField(blank=True, db_column='SEASON', max_length=50, null=True)),
                ('price_should_be', models.DecimalField(blank=True, db_column='Price_Should_be', decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=50, null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'distributor_company_demand_for_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerReqVisitToFarmer',
            fields=[
                ('fid', models.OneToOneField(db_column='FID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.farmer')),
                ('visit_date', models.DateField(db_column='Visit_Date')),
                ('time_slot', models.CharField(db_column='Time_Slot', max_length=100)),
                ('person_in_visit', models.CharField(blank=True, db_column='Person_In_Visit', max_length=255, null=True)),
                ('visit_charge_set_by_farmer', models.DecimalField(blank=True, db_column='Visit_Charge_Set_By_Farmer', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'customer_req_visit_to_farmer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmerSeedDemand',
            fields=[
                ('fid', models.OneToOneField(db_column='FID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.farmer')),
                ('quantity', models.IntegerField(db_column='QUANTITY')),
                ('urgent_need', models.IntegerField(blank=True, db_column='URGENT_NEED', null=True)),
                ('delivery_soon', models.IntegerField(blank=True, db_column='DELIVERY_SOON', null=True)),
                ('high_demand', models.IntegerField(blank=True, db_column='HIGH_DEMAND', null=True)),
            ],
            options={
                'db_table': 'farmer_seed_demand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmerSeedStock',
            fields=[
                ('fid', models.OneToOneField(db_column='FID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.farmer')),
                ('quantity', models.IntegerField(db_column='QUANTITY')),
            ],
            options={
                'db_table': 'farmer_seed_stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialsupportCustomerToFarmer',
            fields=[
                ('fid', models.OneToOneField(db_column='FID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app1.farmer')),
                ('amount', models.DecimalField(blank=True, db_column='Amount', decimal_places=2, max_digits=10, null=True)),
                ('donate', models.IntegerField(blank=True, db_column='Donate', null=True)),
                ('loan', models.IntegerField(blank=True, db_column='Loan', null=True)),
            ],
            options={
                'db_table': 'financialsupport_customer_to_farmer',
                'managed': False,
            },
        ),
    ]
