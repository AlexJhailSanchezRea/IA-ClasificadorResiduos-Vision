import os
import requests
import zipfile
from tqdm import tqdm

def download_file(url, filename):
    """Descarga un archivo con barra de progreso"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

def download_model_manual():
    """Descarga el modelo manualmente"""
    print("📥 Descargando modelo de reciclaje...")
    
    # Crear carpeta Modelos si no existe
    if not os.path.exists("Modelos"):
        os.makedirs("Modelos")
        print("✅ Carpeta 'Modelos' creada")
    
    # URLs alternativas para el modelo
    model_urls = [
        "https://github.com/AprendeIngenia/recyclingAI/raw/main/best.pt",
        "https://huggingface.co/AprendeIngenia/recyclingAI/resolve/main/best.pt"
    ]
    
    model_path = "Modelos/best.pt"
    
    for url in model_urls:
        try:
            print(f"🔄 Intentando descargar desde: {url}")
            download_file(url, model_path)
            print(f"✅ Modelo descargado exitosamente en: {model_path}")
            return True
        except Exception as e:
            print(f"❌ Error con {url}: {e}")
            continue
    
    print("❌ No se pudo descargar el modelo automáticamente")
    print("\n💡 Por favor descarga manualmente:")
    print("1. Ve a: https://huggingface.co/AprendeIngenia/recyclingAI")
    print("2. Descarga el archivo 'best.pt'")
    print("3. Colócalo en la carpeta 'Modelos/'")
    return False

if __name__ == "__main__":
    download_model_manual() 