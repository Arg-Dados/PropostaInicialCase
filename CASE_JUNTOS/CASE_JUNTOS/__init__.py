from utils.paths import storage_project_path, storage_trusted, storage_raw, storage_temporary, storage_checkpoint
from utils_class.directoryManager import DirectoryManager
from utils_class.dataLakeWriter import DataLakeWriter
from utils_class.dataProcessor import DataProcessor
from utils.data_schemas import schema
from time import sleep
import pandas as pd
import sys
import os

# Configurando ambiente
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
sys.path.append(script_dir)

# Criando pasta de armazenamento caso ainda não exista
directory_manager = DirectoryManager(
    storage_raw=storage_raw,
    storage_trusted=storage_trusted,
    storage_temporary=storage_temporary,
    storage_checkpoint=storage_checkpoint,
    storage_project_path=storage_project_path
)
directory_manager.setup_directories()

# Limpando o terminal
os.system('cls' if os.name == 'nt' else 'clear')
print("Sessão Spark iniciada")

# Lendo todos os arquivos encontrados na pasta de input inicial
# O loop continuará sendo executado indefinidamente até que seja parado de forma manual
while True:

    # Verificando se há novos arquivos na pasta RAW, se não houver, espera 5 segundos e verifica novamente.
    # Se houver arquivos, processa os arquivos e os exclui após o processamento
    while True:
        csv_files = os.listdir(directory_manager.get_storage_raw())
        if len(csv_files) > 0:
            break
        sleep(5)
    
    for file in csv_files:
        file_path = os.path.join(directory_manager.get_storage_raw(), file)
        
        # Verificar se é um arquivo CSV
        if file.endswith('.csv'):
            df = pd.read_csv(file_path)
            
            # Processamento dos dados
            data_processor = DataProcessor()
            streaming_df = data_processor.save_as_stream(
                df=df, 
                schema=schema,
                storage_temporary=directory_manager.get_storage_temporary()
                )
            
            # Escrita dos dados no Data Lake
            data_lake_writer = DataLakeWriter(streaming_df=streaming_df)
            data_lake_writer.write_data_lake(
                storage_checkpoint=directory_manager.get_storage_checkpoint(),
                storage_trusted=directory_manager.get_storage_trusted()
            )
            
            print(f"Streaming query finalizado para o arquivo: {file}")
            
        os.remove(file_path)
        csv_files.pop(0)
