import subprocess
import sys
import os

def install_requirements():
    """Instala las dependencias del proyecto"""
    print("📦 Instalando dependencias...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False

def check_model():
    """Verifica si el modelo existe"""
    model_path = "Modelos/best.pt"
    if os.path.exists(model_path):
        print("✅ Modelo encontrado")
        return True
    else:
        print("❌ Modelo no encontrado")
        return False

def main():
    print("🚀 Configurando Sistema de Reciclaje Inteligente")
    print("=" * 50)
    
    # Instalar dependencias
    if not install_requirements():
        print("❌ No se pudieron instalar las dependencias")
        return
    
    # Verificar modelo
    if not check_model():
        print("📥 Descargando modelo...")
        try:
            subprocess.check_call([sys.executable, "download_model.py"])
        except:
            print("💡 Por favor descarga manualmente el modelo desde:")
            print("   https://huggingface.co/AprendeIngenia/recyclingAI")
            print("   Y colócalo en la carpeta 'Modelos/'")
    
    print("\n🎉 Configuración completada!")
    print("\n📋 Para ejecutar el proyecto:")
    print("   python main.py          # Versión con interfaz gráfica")
    print("   python TrashDetect.py   # Versión simple")

if __name__ == "__main__":
    main()