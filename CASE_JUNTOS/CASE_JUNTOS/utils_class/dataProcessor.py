from pyspark.sql import SparkSession
import pandas as pd
import os

# Objeto para processar os arquivos brutos
class DataProcessor():
    def __init__(self):
        self.spark = (SparkSession.builder
            .appName("RealTimeSalesProcessing")
            .config("spark.jars.packages", "io.delta:delta-core_2.12:2.3.0")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate())
    
    def save_as_stream(self, df, storage_temporary, schema):
        # Converter o DataFrame Pandas para PySpark DataFrame
        spark_df = self.spark.createDataFrame(df)
        
        # Salvar os dados em partes para simular o stream de dados
        num_parts = 5
        rows_per_part = spark_df.count() // num_parts
        
        for i in range(num_parts):
            if i == num_parts - 1:
                # Para a última parte, incluir todas as linhas restantes
                part_df = spark_df.limit(rows_per_part).offset(i * rows_per_part)
            else:
                part_df = spark_df.limit(rows_per_part).offset(i * rows_per_part + (rows_per_part - 1))
            
            part_file_path = os.path.join(storage_temporary, f'part_{i}.json')
            part_df.write.json(part_file_path, mode='overwrite')
        
        # Leitura do stream de dados em memória
        streaming_df = (self.spark.readStream
                        .schema(schema)
                        .json(storage_temporary))
        
        return streaming_df
