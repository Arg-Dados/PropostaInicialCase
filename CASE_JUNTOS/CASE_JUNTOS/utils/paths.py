import os

# Diretório de downloads padrão do sistema
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Diretório para armazenamento dos dados
storage_project_path = os.path.join(downloads_path, 'STORAGE_JUNTOS')

# Diretório de armazenamento dos dados iniciais (arquivos csv)
storage_initial = os.path.join(storage_project_path, 'INITIAL_FILES')
storage_raw = os.path.join(storage_initial, 'RAW')

# Diretório de armazenamento dos dados finais
storage_final = os.path.join(storage_project_path, 'FINAL_FILES')
storage_trusted = os.path.join(storage_final, 'TRUSTED')

# Diretório de armazenamento de dados temporário
storage_manager_files = os.path.join(storage_project_path, 'MANAGER')
storage_temporary = os.path.join(storage_manager_files, 'TEMPORARY')

# Diretório de armazenamento de checkpoints
storage_checkpoint = os.path.join(storage_manager_files, 'CHECKPOINT')