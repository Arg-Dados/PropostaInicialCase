from utils.functions import read_and_show_delta_data
from pyspark.sql import SparkSession

# Objeto para escrever os dados no data lake simulado
class DataLakeWriter():
    def __init__(self, streaming_df):
        self.streaming_df = streaming_df
        self.spark = (SparkSession.builder
            .appName("RealTimeSalesProcessing")
            .config("spark.jars.packages", "io.delta:delta-core_2.12:2.3.0")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate())
    
    def write_data_lake(self, storage_checkpoint, storage_trusted):
        # Processamento dos dados em tempo real
        streaming_df = self.streaming_df.select("*")

        # Escrita dos dados no Delta Lake
        query = (streaming_df.writeStream
            .format("delta")
            .outputMode("append")
            .option("checkpointLocation", storage_checkpoint)
            .start(storage_trusted))
    
        # Aguardar a terminação da query e mostrar os dados
        try:
            query.awaitTermination(timeout=60)  # Timeout de 60 segundos para o streaming
        except Exception as e:
            print(f"Erro durante a execução do streaming: {e}")
        finally:
            read_and_show_delta_data(spark=self.spark)