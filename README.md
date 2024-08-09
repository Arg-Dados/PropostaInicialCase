# Processamento em tempo real com Spark e Delta Lake

Este projeto oferece uma solução de processamento de dados em tempo real utilizando Apache Spark e Delta Lake. Ele foi projetado para lidar com arquivos CSV contendo dados de vendas, processando-os e armazenando-os em um Data Lake. Além disso, o projeto gerencia automaticamente a estrutura de diretórios necessária para o fluxo contínuo de dados.

No que diz respeito ao streaming de dados, assim que o script __init__.py é iniciado, ele monitora constantemente um diretório específico, criado automaticamente pelo próprio script. A cada 5 segundos, o sistema verifica se novos arquivos CSV foram adicionados a esse diretório. Quando um novo arquivo é detectado, ele é imediatamente processado e carregado em tempo real no Data Lake, garantindo que os dados estejam sempre atualizados e prontos para uso. 

*Vale ressaltar que o intervalo de 5 segundos pode ser modificado para intervalos menores, incluindo até mesmo uma verificação contínua sem nenhum tipo de interrupção ou espera, porém isso consequentemente consumiria mais poder computacional e talvez não fosse necessário a depender da velocidade de adição de dados na pasta RAW.*

O Arquivo PropostaPreliminar.pdf possui outros detalhes e possibilidades de implementação, incluindo a arquitetura sugerida utilizando diversas tecnologias e ferramentas fornecidas pela Azure.

## Estrutura do Projeto

A parte do código do projeto é estruturada da seguinte forma:

- CASE_JUNTOS
    |
    - **`__init__.py`**: O ponto de entrada principal do projeto. Ele configura o ambiente, inicializa os diretórios necessários e processa os arquivos CSV encontrados na pasta `RAW`;
    - requirements
        |
        - **requirements.txt**: Arquivo contendo todas as bibliotecas e frameworks necessários para execução do projeto;
    - utils_class
        |
        - **dataProcessor.py**: Objeto responsável por processar os dados simulando streming utilizando spark;
        - **dataLakeWriter.py**: Objeto responsável pela escrita dos dados no data lake;
        - **directoryManager**: Objeto responsável por toda a gerência dos diretórios de armazenamento de dados;
    - utils
        |
        - **functions.py**: Arquivo contendo todas as funções utilizadas no processo;
        - **paths.py***: Arquivo responsável por gerar todas as variáveis contendo os diretórios de armazenamentos locais;
        - **data_schemas.py**: Arquivo contendo o schema dos dados utilizados;

## Configuração e Instalação

OBS: O objeto DirectoryManager no método setup_directories cria automaticamente uma pasta no diretório de downloads chamada  STORAGE_JUNTOS, então caso exista outra pasta com o mesmo nome, a mesma será sobreescrita. Além disso, caso a máquina de execução não possua o diretório padrão Downloads, ocorrerá uma pequena inconsistência.

### 1. Pré-requisitos

- Python 3.8 ou superior
- Apache Spark com suporte a Delta Lake
- Java (para execução do Apache Spark)

### 2. Instalação das Dependências

Crie um ambiente virtual e instale as dependências necessárias:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
