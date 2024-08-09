import os

# Objeto para manipulação dos diretórios de armazenamento
class DirectoryManager:
    def __init__(self, storage_project_path, storage_trusted, storage_raw, storage_temporary, storage_checkpoint):
        self.storage_project_path = storage_project_path
        self.storage_trusted = storage_trusted
        self.storage_raw = storage_raw
        self.storage_temporary = storage_temporary
        self.storage_checkpoint = storage_checkpoint

    def setup_directories(self):
        # Cria os ciretórios de armazenamento caso ainda não existam
        if not os.path.exists(self.storage_project_path):
            os.makedirs(self.storage_project_path)
            os.makedirs(self.storage_trusted)
            os.makedirs(self.storage_raw)
            os.makedirs(self.storage_temporary)
            os.makedirs(self.storage_checkpoint)
            print(f"Diretórios de armazenamento gerados automaticamente na pasta de downloads")
        else:
            print(f"Diretórios de armazenamento já existem na pasta de downloads")

    def get_storage_project_path(self):
        # Retorna o diretório principal de armazenamento
        return self.storage_project_path
    
    def get_storage_trusted(self):
        # Retorna o diretório de dados final
        return self.storage_trusted
    
    def get_storage_raw(self):
        # Retorna o diretório de dados brutos
        return self.storage_raw
    
    def get_storage_temporary(self):
        # Retorna o diretório de dados temporários
        return self.storage_temporary
    
    def get_storage_checkpoint(self):
        # Retorna o diretório de checkpoints
        return self.storage_checkpoint
    