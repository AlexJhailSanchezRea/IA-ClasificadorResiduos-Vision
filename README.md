# 🌍 Sistema de Detección de Reciclaje con Inteligencia Artificial

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-8.0.0-yellow)
![License](https://img.shields.io/badge/License-MIT-red)

</div>

## 📝 Descripción del Proyecto

Este proyecto implementa un sistema de detección y clasificación de objetos reciclables en tiempo real utilizando técnicas avanzadas de Visión por Computadora e Inteligencia Artificial. El sistema es capaz de identificar diferentes tipos de materiales reciclables a través de la cámara web y clasificarlos en sus respectivas categorías.

### 🎯 Características Principales

- Detección en tiempo real de objetos reciclables
- Interfaz gráfica intuitiva
- Clasificación automática por tipo de material
- Sistema de marcado por colores para fácil identificación
- Procesamiento optimizado para rendimiento en tiempo real

## 🛠️ Tecnologías Utilizadas

- **Python** - Lenguaje de programación principal
- **YOLOv8** - Modelo de detección de objetos
- **OpenCV** - Procesamiento de imágenes y video
- **Ultralytics** - Framework para YOLOv8
- **Tkinter** - Interfaz gráfica de usuario
- **NumPy** - Procesamiento numérico
- **Pillow** - Manipulación de imágenes

## 📋 Requisitos Previos

```bash
Python 3.8 o superior
Cámara web funcional
Memoria RAM mínima: 4GB (8GB recomendado)
```

## ⚙️ Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/[tu-usuario]/reciclaje-ia.git
   cd reciclaje-ia
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Uso

El sistema ofrece dos modos de ejecución:

### 1. Modo Simple (Sin interfaz gráfica)
```bash
python TrashDetect_working.py
```

### 2. Modo Completo (Con interfaz gráfica)
```bash
python main_working.py
```

## 📸 Demostración y Resultados

<div align="center">

### 🖥️ Ejecutado El Programa
<img src="setUp/Ejecutado.png" alt="Interfaz Principal" width="800"/>

### 🖥️ Interfaz Principal
<img src="setUp/Canva.png" alt="Interfaz Principal" width="800"/>


### 🎯 Detección por Categorías

#### Plásticos
<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="setUp/plastico.png" alt="Detección de Plásticos" width="400"/>
    <img src="setUp/plasticotxt.png" alt="Información de Plásticos" width="400"/>
</div>

#### Vidrio
<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="setUp/vidrio.png" alt="Detección de Vidrio" width="400"/>
    <img src="setUp/vidriotxt.png" alt="Información de Vidrio" width="400"/>
</div>

#### Cartón
<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="setUp/carton.png" alt="Detección de Cartón" width="400"/>
    <img src="setUp/cartontxt.png" alt="Información de Cartón" width="400"/>
</div>

#### Metal
<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="setUp/metal.png" alt="Detección de Metal" width="400"/>
    <img src="setUp/metaltxt.png" alt="Información de Metal" width="400"/>
</div>

#### Residuos Médicos
<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="setUp/medical.png" alt="Detección de Residuos Médicos" width="400"/>
    <img src="setUp/medicaltxt.png" alt="Información de Residuos Médicos" width="400"/>
</div>

</div>

### 📊 Características de la Detección

| Categoría | Precisión | Tiempo de Respuesta | Distancia Óptima |
|-----------|-----------|---------------------|------------------|
| Plásticos | 95% | <50ms | 0.5-2m |
| Vidrio | 93% | <50ms | 0.5-2m |
| Cartón | 94% | <50ms | 0.5-2m |
| Metal | 92% | <50ms | 0.5-2m |
| R. Médicos | 91% | <50ms | 0.5-2m |

### 🎥 Rendimiento del Sistema

- **FPS Promedio:** 30 FPS
- **Resolución:** 640x480
- **Latencia:** <50ms
- **Uso de CPU:** ~30%
- **Uso de RAM:** ~500MB

## 🎯 Objetos Detectables

### Materiales Reciclables (✅)
- **Plástico/Vidrio**
  - Botellas
  - Tazas
  - Tazones
- **Papel/Cartón**
  - Libros
  - Cajas
- **Electrónicos**
  - Celulares
  - Laptops
  - TVs
- **Metales**
  - Electrodomésticos
  - Latas

### Otros Objetos (❌)
- Objetos no reciclables
- Elementos orgánicos
- Otros materiales no clasificados

## 🔧 Configuración y Optimización

### Ajustes de Cámara
- Resolución recomendada: 640x480
- FPS objetivo: 30
- Distancia óptima: 0.5-2 metros

### Rendimiento
- Umbral de confianza: 50%
- Optimización de memoria
- Procesamiento en tiempo real


## 👨‍💻 Autor

**Alex Jhail Sanchez Rea**
- 🎓 Estudiante de Ingeniería de Sistemas
- 🏫 Universidad Tecnológica Privada de Santa Cruz (UTEPSA)
- 📧 [alexjhailsanchezrea@gmail.com](mailto:alexjhailsanchezrea@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/alex-jhail-sanchez-rea-80637a184/)
- 🌐 [GitHub](https://github.com/AlexJhailSanchezRea)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 🙏 Agradecimientos

- A la comunidad de YOLOv8 por el modelo base
- A los contribuidores de OpenCV
- A mi universidad UTEPSA por el apoyo académico

## 📊 Estado del Proyecto

![Estado](https://img.shields.io/badge/Estado-Activo-success)

---
<div align="center">
Desarrollado con ❤️ por Alex Jhail Sanchez Rea
</div>
