# Layers

dbutils.fs.mount(
    source = 'wasbs://bronze@medalliondbtstorage.blob.core.windows.net',
    mount_point = '/mnt/bronze',
    extra_configs = {'fs.azure.account.key.medalliondbtstorage.blob.core.windows.net': dbutils.secrets.get('databricksScope','storageAccountKey')}
)

dbutils.fs.mount(
    source = 'wasbs://silver@medalliondbtstorage.blob.core.windows.net',
    mount_point = '/mnt/silver',
    extra_configs = {'fs.azure.account.key.medalliondbtstorage.blob.core.windows.net': dbutils.secrets.get('databricksScope','storageAccountKey')}
)

dbutils.fs.mount(
    source = 'wasbs://gold@medalliondbtstorage.blob.core.windows.net',
    mount_point = '/mnt/gold',
    extra_configs = {'fs.azure.account.key.medalliondbtstorage.blob.core.windows.net': dbutils.secrets.get('databricksScope','storageAccountKey')}
)

dbutils.fs.ls('/mnt/bronze')
dbutils.fs.ls('/mnt/silver')
dbutils.fs.ls('/mnt/gold')

fileName = dbutils.widgets.get('fileName')
tableSchema = dbutils.widgets.get('table_schema')
tableName = dbutils.widgets.get('table_name')

spark.sql(f'CREATE DATABASE IF NOT EXISTS {tableSchema}') 

spark.sql
(""" 
        CREATE TABLE IF NOT EXISTS """+tableSchema+"""."""+tableName+"""
        USING PARQUET LOCATION '/mnt/bronze/"""+fileName+"""/"""+tableSchema+"""."""+tableName+""".parquet'
 """)
