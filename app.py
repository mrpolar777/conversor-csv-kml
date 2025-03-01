import pandas as pd
import streamlit as st
import simplekml

# Função para extrair coordenadas do CSV sem modificar os valores
def extract_coordinates_from_csv(csv_file):
    try:
        # Detectar delimitador correto
        df = pd.read_csv(csv_file, encoding="utf-8", delimiter=";", on_bad_lines="skip")

        if df.shape[1] == 1:
            df = pd.read_csv(csv_file, encoding="utf-8", delimiter=",", on_bad_lines="skip")
        if df.shape[1] == 1:
            df = pd.read_csv(csv_file, encoding="utf-8", delimiter="\t", on_bad_lines="skip")

    except Exception as e:
        st.error(f"Erro ao ler o CSV: {e}")
        return []

    st.write("Colunas encontradas:", df.columns.tolist())  # Exibe as colunas para debug

    coordinates = []
    
    # Verifica se as colunas existem (independente de maiúsculas/minúsculas)
    col_lat = next((col for col in df.columns if "lat" in col.lower()), None)
    col_lon = next((col for col in df.columns if "long" in col.lower()), None)

    if col_lat and col_lon:
        for index, row in df.iterrows():
            try:
                lat = float(str(row[col_lat]).replace(",", "."))  # Garante formato decimal
                lon = float(str(row[col_lon]).replace(",", "."))
                coordinates.append((lat, lon))
            except ValueError:
                continue  # Ignora linhas inválidas
    else:
        st.error("Colunas de latitude e longitude não foram encontradas no CSV.")
    
    return coordinates

# Função para criar arquivo KML
def create_kml(coordinates):
    kml = simplekml.Kml()
    for lat, lon in coordinates:
        kml.newpoint(coords=[(lon, lat)])  # Mantém a ordem correta (lon, lat)
    return kml

# Interface com Streamlit
st.title("Conversor CSV para KML")
uploaded_file = st.file_uploader("Faça upload de um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    st.write("Arquivo carregado com sucesso!")
    
    # Extrair coordenadas do CSV
    coordinates = extract_coordinates_from_csv(uploaded_file)
    if coordinates:
        st.write(f"Coordenadas encontradas: {coordinates}")
        
        # Criar arquivo KML
        kml = create_kml(coordinates)
        kml_file = "output.kml"
        kml.save(kml_file)
        
        # Oferecer download do KML
        with open(kml_file, "rb") as f:
            st.download_button("Baixar KML", f, file_name="rota_convertida.kml")
    else:
        st.write("Nenhuma coordenada encontrada no CSV.")
