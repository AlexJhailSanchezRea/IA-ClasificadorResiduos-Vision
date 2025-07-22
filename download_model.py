import os
import requests
from huggingface_hub import hf_hub_download

def download_model():
    """Descarga el modelo YOLO desde Hugging Face"""
    print("�� Descargando modelo YOLO...")
    
    try:
        # Crear carpeta Modelos si no existe
        if not os.path.exists("Modelos"):
            os.makedirs("Modelos")
            print("✅ Carpeta 'Modelos' creada")
        
        # Descargar modelo desde Hugging Face
        model_path = hf_hub_download(
            repo_id="AprendeIngenia/recyclingAI",
            filename="best.pt",
            local_dir="Modelos"
        )
        
        print(f"✅ Modelo descargado exitosamente en: {model_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error al descargar el modelo: {e}")
        print("💡 Alternativa: Descarga manual desde https://huggingface.co/AprendeIngenia/recyclingAI")
        return False

if __name__ == "__main__":
    download_model()