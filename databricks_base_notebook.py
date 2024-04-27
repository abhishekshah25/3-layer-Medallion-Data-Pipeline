# Bronze Layer
dbutils.fs.mount(
    source = 'wasbs://bronze@medalliondbtstorage.blob.core.windows.net',
    mount_point = '/mnt/bronze',
    extra_configs = {'fs.azure.account.key.medalliondbtstorage.blob.core.windows.net': dbutils.secrets.get('databricksScope','storageAccountKey')}
)

# Silver Layer
dbutils.fs.mount(
    source = 'wasbs://silver@medalliondbtstorage.blob.core.windows.net',
    mount_point = '/mnt/silver',
    extra_configs = {'fs.azure.account.key.medalliondbtstorage.blob.core.windows.net': dbutils.secrets.get('databricksScope','storageAccountKey')}
)

# Gold Layer
dbutils.fs.mount(
    source = 'wasbs://gold@medalliondbtstorage.blob.core.windows.net',
    mount_point = '/mnt/gold',
    extra_configs = {'fs.azure.account.key.medalliondbtstorage.blob.core.windows.net': dbutils.secrets.get('databricksScope','storageAccountKey')}
)

# List of Files in Layers
dbutils.fs.ls('/mnt/bronze')
dbutils.fs.ls('/mnt/silver')
dbutils.fs.ls('/mnt/gold')


fileName = dbutils.widgets.get('fileName')
tableSchema = dbutils.widgets.get('table_schema')
tableName = dbutils.widgets.get('table_name')


# Create database if not exists
spark.sql(f'CREATE DATABASE IF NOT EXISTS {tableSchema}') 

# Create table if not exists
spark.sql(""" 
        CREATE TABLE IF NOT EXISTS """+tableSchema+"""."""+tableName+"""
        USING PARQUET LOCATION '/mnt/bronze/"""+fileName+"""/"""+tableSchema+"""."""+tableName+""".parquet'
""")