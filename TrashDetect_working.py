# Importamos librerias
from ultralytics import YOLO
import cv2
import math

# Modelo YOLO pre-entrenado (funciona inmediatamente)
print("🔄 Cargando modelo YOLO...")
model = YOLO('yolov8n.pt')  # Modelo general de YOLO

# Cap
print("📹 Iniciando cámara...")
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Clases generales de YOLO (incluyen objetos que podrían ser reciclables)
clsName = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',
    'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat',
    'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
    'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop',
    'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink',
    'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier',
    'toothbrush'
]

# Objetos reciclables con clasificación mejorada
reciclables = {
    'bottle': 'PLÁSTICO',
    'cup': 'PLÁSTICO',
    'wine glass': 'VIDRIO',
    'bowl': 'VIDRIO',
    'book': 'PAPEL',
    'cell phone': 'ELECTRÓNICOS',
    'laptop': 'ELECTRÓNICOS',
    'tv': 'ELECTRÓNICOS',
    'remote': 'ELECTRÓNICOS',
    'keyboard': 'ELECTRÓNICOS',
    'mouse': 'ELECTRÓNICOS',
    'refrigerator': 'METALES',
    'microwave': 'METALES',
    'oven': 'METALES',
    'toaster': 'METALES',
    'fork': 'METALES',
    'knife': 'METALES',
    'spoon': 'METALES',
    'clock': 'ELECTRÓNICOS',
    'vase': 'VIDRIO',
    'scissors': 'METALES',
    'hair drier': 'ELECTRÓNICOS',
    'toothbrush': 'PLÁSTICO'
}

# Colores personalizados (BGR format)
COLOR_VERDE = (0, 255, 0)      # Verde para reciclables
COLOR_BLANCO = (255, 255, 255) # Blanco para texto
COLOR_NEGRO = (0, 0, 0)        # Negro para fondo

print("🎯 Sistema de detección iniciado!")
print("💡 Detectando objetos reciclables...")
print("🔴 Presiona 'ESC' para salir")

# Inference
while True:
    # Frames
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Error al leer la cámara")
        break

    # Yolo detection
    results = model(frame, stream=True, verbose=False)
    for res in results:
        # Box
        boxes = res.boxes
        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Error < 0
            if x1 < 0: x1 = 0
            if y1 < 0: y1 = 0
            if x2 < 0: x2 = 0
            if y2 < 0: y2 = 0

            # Class
            cls = int(box.cls[0])

            # Confidence
            conf = float(box.conf[0])
            
            # Solo mostrar objetos con alta confianza
            if conf > 0.5:
                class_name = clsName[cls]
                
                # Verificar si es reciclable
                if class_name in reciclables:
                    tipo_reciclaje = reciclables[class_name]
                    color_rectangulo = COLOR_VERDE
                    color_texto = COLOR_BLANCO
                    texto = f'{tipo_reciclaje} - {int(conf * 100)}%'
                    
                    # Agregar fondo negro al texto para mejor visibilidad
                    (text_width, text_height), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_COMPLEX, 0.7, 2)
                    cv2.rectangle(frame, (x1, y1 - 30), (x1 + text_width, y1), COLOR_NEGRO, -1)
                    
                else:
                    color_rectangulo = COLOR_NEGRO
                    color_texto = COLOR_BLANCO
                    texto = f'{class_name} - {int(conf * 100)}%'
                    
                    # Agregar fondo negro al texto para mejor visibilidad
                    (text_width, text_height), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_COMPLEX, 0.7, 2)
                    cv2.rectangle(frame, (x1, y1 - 30), (x1 + text_width, y1), COLOR_NEGRO, -1)
                
                # Draw rectangle
                cv2.rectangle(frame, (x1, y1), (x2, y2), color_rectangulo, 3)
                
                # Draw text
                cv2.putText(frame, texto, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, color_texto, 2)

    # Show
    cv2.imshow("Sistema de Reciclaje Inteligente", frame)

    # Close
    t = cv2.waitKey(5)
    if t == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Sistema cerrado") 