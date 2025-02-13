# Conversor CSV para KML

Este projeto tem como objetivo converter coordenadas geográficas armazenadas em um arquivo CSV para o formato KML, que pode ser visualizado no Google Earth. A aplicação é desenvolvida com Python, utilizando as bibliotecas `pandas`, `streamlit` e `simplekml`.

## Funcionalidades

- Carregamento de arquivos CSV com coordenadas de latitude e longitude.
- Conversão de coordenadas no formato personalizado para o formato decimal.
- Geração de um arquivo KML com pontos correspondentes às coordenadas extraídas.
- Interface simples e interativa utilizando Streamlit para facilitar o uso.

## Como usar

1. **Pré-requisitos**:
   - Instale as dependências do projeto:
     ```bash
     pip install pandas streamlit simplekml
     ```

2. **Executando a aplicação**:
   - Execute o arquivo Python que contém o código:
     ```bash
     streamlit run nome_do_arquivo.py
     ```
   - Acesse a aplicação no seu navegador, geralmente em `http://localhost:8501`.

3. **Utilização**:
   - Faça o upload de um arquivo CSV contendo as colunas `Latitude` e `Longitude`.
   - O formato das coordenadas pode ser personalizado, mas o código já inclui funções para corrigir e converter os dados.
   - Após o upload, o sistema irá extrair as coordenadas e gerar um arquivo KML que poderá ser baixado.

4. **Formato esperado do CSV**:
   O arquivo CSV deve ter, pelo menos, as seguintes colunas:
   - `Latitude` (coordenadas de latitude)
   - `Longitude` (coordenadas de longitude)

   Exemplo de CSV:
   ```csv
   Latitude,Longitude
   123456789,987654321
   123456780,987654310
   ```

5. **Resultado**:
   Após o processamento, será gerado um arquivo `output.kml` contendo os pontos extraídos do CSV. Você poderá visualizar esses pontos em plataformas como o Google Earth.

## Como funciona o código

- **Funções de conversão**:
  - `corrigir_coordenada`: Remove pontos extras e corrige a vírgula para o formato correto.
  - `converter_coordenada`: Converte as coordenadas no formato personalizado para o formato decimal.

- **Extração de coordenadas**:
  - O código lê as coordenadas de latitude e longitude do CSV e as converte para o formato adequado.

- **Criação do arquivo KML**:
  - O KML é gerado com a ajuda da biblioteca `simplekml`, onde cada coordenada é representada como um ponto no arquivo.
