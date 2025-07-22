import os
import requests
import zipfile
from tqdm import tqdm

def download_file(url, filename):
    """Descarga un archivo con barra de progreso"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()  # Verificar si hay errores HTTP
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filename, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=8192):
                size = file.write(data)
                pbar.update(size)
        return True
    except Exception as e:
        print(f"Error descargando {url}: {e}")
        return False

def download_model_fixed():
    """Descarga el modelo desde fuentes alternativas"""
    print("📥 Descargando modelo de reciclaje...")
    
    # Crear carpeta Modelos si no existe
    if not os.path.exists("Modelos"):
        os.makedirs("Modelos")
        print("✅ Carpeta 'Modelos' creada")
    
    # URLs alternativas para el modelo
    model_urls = [
        "https://github.com/AprendeIngenia/recyclingAI/raw/main/best.pt",
        "https://huggingface.co/AprendeIngenia/recyclingAI/resolve/main/best.pt",
        "https://raw.githubusercontent.com/AprendeIngenia/recyclingAI/main/best.pt"
    ]
    
    model_path = "Modelos/best.pt"
    
    for i, url in enumerate(model_urls, 1):
        print(f"\n🔄 Intento {i}: Descargando desde {url}")
        if download_file(url, model_path):
            # Verificar que el archivo se descargó correctamente
            if os.path.exists(model_path) and os.path.getsize(model_path) > 100000:  # Más de 100KB
                print(f"✅ Modelo descargado exitosamente en: {model_path}")
                print(f"📊 Tamaño del archivo: {os.path.getsize(model_path)} bytes")
                return True
            else:
                print("❌ Archivo descargado pero parece estar corrupto")
                if os.path.exists(model_path):
                    os.remove(model_path)
        else:
            print(f"❌ Falló la descarga desde {url}")
    
    print("\n❌ No se pudo descargar el modelo automáticamente")
    print("\n💡 Solución alternativa:")
    print("1. Ve a: https://huggingface.co/AprendeIngenia/recyclingAI")
    print("2. Haz clic en 'Files and versions'")
    print("3. Descarga el archivo 'best.pt'")
    print("4. Colócalo en la carpeta 'Modelos/'")
    print("\n🔧 O usa un modelo YOLO pre-entrenado como alternativa:")
    print("   model = YOLO('yolov8n.pt')  # Modelo general")
    return False

if __name__ == "__main__":
    download_model_fixed() 