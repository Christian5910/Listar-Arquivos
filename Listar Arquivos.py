import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def list_folder_contents():
    # Cria uma janela root oculta
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Abre a caixa de diálogo para selecionar a pasta
    folder_path = filedialog.askdirectory(title="Selecione a pasta")
    
    if not folder_path:
        print("Nenhuma pasta selecionada.")
        return

    # Nome do arquivo de saída com data e hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"folder_contents_{timestamp}.txt"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Conteúdo da pasta: {folder_path}\n")
            f.write("=" * 50 + "\n\n")
            
            # Percorre a pasta e lista arquivos e subpastas
            for root, dirs, files in os.walk(folder_path):
                # Escreve o caminho relativo da subpasta
                relative_path = os.path.relpath(root, folder_path)
                if relative_path == ".":
                    relative_path = "Raiz"
                f.write(f"Pasta: {relative_path}\n")
                
                # Lista as subpastas
                for dir_name in dirs:
                    f.write(f"  [Pasta] {dir_name}\n")
                
                # Lista os arquivos
                for file_name in files:
                    f.write(f"  [Arquivo] {file_name}\n")
                
                f.write("\n")
            
            f.write("=" * 50 + "\n")
            f.write(f"Arquivo gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"Arquivo '{output_file}' gerado com sucesso!")
    
    except Exception as e:
        print(f"Erro ao gerar o arquivo: {e}")

if __name__ == "__main__":
    list_folder_contents()