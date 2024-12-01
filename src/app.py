import os
import pandas as pd
import rarfile
import streamlit as st
import shutil

# Configuração de caminhos
data_path = "./data"
advbox_path = os.path.join(data_path, "AdvBox")
temp_path = "./temp"
extracao_backup_path = os.path.join(data_path, "extracao_backup")  # Caminho para extração
output_path = "./output"

# Criação dos diretórios necessários
os.makedirs(temp_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)
os.makedirs(extracao_backup_path, exist_ok=True)

# Função para processar os dados
def process_data(input_file, modelo_file, output_file):
    # Leitura das planilhas
    input_df = pd.read_excel(input_file, engine="openpyxl")
    modelo_df = pd.read_excel(modelo_file, engine="openpyxl")

    # Padronizar os dados conforme o modelo
    colunas_necessarias = modelo_df.columns
    output_df = input_df.reindex(columns=colunas_necessarias, fill_value="")

    # Formatar datas no formato DD/MM/AAAA
    for col in output_df.select_dtypes(include=["datetime"]):
        output_df[col] = output_df[col].dt.strftime("%d/%m/%Y")

    # Salvar o arquivo processado
    output_df.to_excel(output_file, index=False)

# Função para extrair arquivos do RAR
def extract_rar(rar_path, extract_to):
    try:
        with rarfile.RarFile(rar_path, "r") as rf:
            st.info(f"Extraindo arquivos para: {extract_to}")
            rf.extractall(extract_to)  # Extração
            extracted_files = rf.namelist()  # Lista de arquivos extraídos
            return extracted_files
    except Exception as e:
        st.error(f"Erro ao extrair arquivos: {e}")
        return []

# Interface com Streamlit
st.set_page_config(page_title="Migração AdvBox", layout="wide")
st.title("Sistema de Migração AdvBox")

st.markdown("""  
**Regras de negócio:**  
1. Faça o upload do arquivo compactado `.rar` (Backup de Dados).  
2. Os arquivos CLIENTES.xlsx e PROCESSOS.xlsx serão carregados automaticamente do diretório `data/AdvBox`.  
3. O modelo padrão AdvBox será carregado automaticamente do diretório `data/AdvBox`.  
""")

# Upload do arquivo RAR
uploaded_rar = st.file_uploader("Upload do arquivo RAR (Backup de Dados)", type=["rar"])

if st.button("Processar Dados"):
    try:
        # Verificar os arquivos CLIENTES, PROCESSOS e o modelo
        clientes_path = os.path.join(advbox_path, "CLIENTES.xlsx")
        processos_path = os.path.join(advbox_path, "PROCESSOS.xlsx")
        modelo_path = os.path.join(advbox_path, "MIGRAÇÃO PADRÕES NOVO.xlsx")

        # Validar existência dos arquivos locais
        if not os.path.exists(clientes_path):
            st.error(f"Arquivo CLIENTES.xlsx não encontrado em {advbox_path}.")
        elif not os.path.exists(processos_path):
            st.error(f"Arquivo PROCESSOS.xlsx não encontrado em {advbox_path}.")
        elif not os.path.exists(modelo_path):
            st.error(f"Modelo MIGRAÇÃO PADRÕES NOVO.xlsx não encontrado em {advbox_path}.")
        else:
            # Salvar o arquivo RAR carregado
            rar_path = os.path.join(temp_path, "Backup_de_dados.rar")
            with open(rar_path, "wb") as f:
                f.write(uploaded_rar.read())
            
            # Extrair os arquivos do RAR
            st.info("Extraindo arquivos do backup...")
            staged_files = extract_rar(rar_path, extracao_backup_path)  # Alteração no caminho de extração
           
            # Caminhos de saída
            clientes_output_path = os.path.join(output_path, "CLIENTES_TRATADOS.xlsx")
            processos_output_path = os.path.join(output_path, "PROCESSOS_TRATADOS.xlsx")

            # Processar os arquivos
            st.info("Processando CLIENTES...")
            process_data(clientes_path, modelo_path, clientes_output_path)
            st.info("Processando PROCESSOS...")
            process_data(processos_path, modelo_path, processos_output_path)

            # Disponibilizar os arquivos processados para download
            st.success("Processamento concluído! Faça o download dos arquivos abaixo:")
            
            with open(clientes_output_path, "rb") as f:
                st.download_button(
                    label="Baixar CLIENTES_TRATADOS.xlsx",
                    data=f,
                    file_name="CLIENTES_TRATADOS.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

            with open(processos_output_path, "rb") as f:
                st.download_button(
                    label="Baixar PROCESSOS_TRATADOS.xlsx",
                    data=f,
                    file_name="PROCESSOS_TRATADOS.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

    except Exception as e:
        st.error(f"Erro durante o processamento: {e}")
    finally:
        # Limpar a pasta temporária
        shutil.rmtree(temp_path)
