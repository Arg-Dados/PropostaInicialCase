from utils.paths import storage_trusted

# Função para ler e mostrar os dados após a escrita
def read_and_show_delta_data(spark):
    delta_df = spark.read.format("delta").load(storage_trusted)
    delta_df.show(10)  # Mostrar as primeiras 10 linhas
    print(f"Total de linhas no Delta Lake: {delta_df.count()}")
