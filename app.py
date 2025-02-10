import pandas as pd
import streamlit as st
import simplekml

# Função para corrigir o formato das coordenadas
def corrigir_coordenada(coord):
    # Remove pontos extras e substitui a vírgula por ponto
    coord = str(coord).replace(".", "").replace(",", ".")
    return float(coord)

# Função para converter coordenadas no formato personalizado para decimal
def converter_coordenada(coord):
    # Remove pontos extras
    coord = str(coord).replace(".", "")
    # Converte para float
    return float(coord) / 1000000  # Ajuste conforme necessário

# Função para extrair coordenadas do CSV
def extract_coordinates_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    coordinates = []
    
    # Verifica se as colunas de latitude e longitude existem
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        for index, row in df.iterrows():
            try:
                lat = converter_coordenada(row['Latitude'])
                lon = converter_coordenada(row['Longitude'])
                coordinates.append((lat, lon))
            except ValueError:
                continue  # Ignorar linhas com valores inválidos
    return coordinates

# Função para criar arquivo KML
def create_kml(coordinates):
    kml = simplekml.Kml()
    for lat, lon in coordinates:
        kml.newpoint(coords=[(lon, lat)])
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