# Libraries
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from ultralytics import YOLO
import math

def clean_lbl():
    # Clean
    lblimg.config(image='')
    lblimgtxt.config(image='')

def images(img, imgtxt):
    img = img
    imgtxt = imgtxt

    # Img Detect
    img = np.array(img, dtype="uint8")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = Image.fromarray(img)

    img_ = ImageTk.PhotoImage(image=img)
    lblimg.configure(image=img_)
    lblimg.image = img_

    # Img Text
    imgtxt = np.array(imgtxt, dtype="uint8")
    imgtxt = cv2.cvtColor(imgtxt, cv2.COLOR_BGR2RGB)
    imgtxt = Image.fromarray(imgtxt)

    img_txt = ImageTk.PhotoImage(image=imgtxt)
    lblimgtxt.configure(image=img_txt)
    lblimgtxt.image = img_txt

# Scanning Function
def Scanning():
    global img_metal, img_glass, img_plastic, img_carton, img_medical
    global img_metaltxt, img_glasstxt, img_plastictxt, img_cartontxt, img_medicaltxt, pantalla
    global lblimg, lblimgtxt

    # Interfaz
    lblimg = Label(pantalla, bg='#1a1a1a')  # Fondo negro
    lblimg.place(x=75, y=260)

    lblimgtxt = Label(pantalla, bg='#1a1a1a')  # Fondo negro
    lblimgtxt.place(x=995, y=310)
    detect = False

    # Read VideoCapture
    if cap is not None:
        ret, frame = cap.read()
        frame_show =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # True
        if ret == True:
            # Yolo detection
            results = model(frame, stream=True, verbose=False)
            for res in results:
                # Box
                boxes = res.boxes
                for box in boxes:
                    detect = True
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
                    if conf > 0.6:  # Aumentado el umbral de confianza
                        class_name = clsName[cls]
                        
                        # Verificar si es reciclable
                        if class_name in reciclables:
                            tipo_reciclaje = reciclables[class_name]
                            # COLORES MEJORADOS: VERDE OSCURO para reciclables
                            color_rectangulo = (0, 100, 0)  # VERDE OSCURO
                            color_texto = (255, 255, 255)   # BLANCO
                            texto = f'{tipo_reciclaje} - {int(conf * 100)}%'
                            
                            # Mostrar imagen correspondiente
                            if 'PLÁSTICO' in tipo_reciclaje:
                                images(img_plastic, img_plastictxt)
                            elif 'VIDRIO' in tipo_reciclaje:
                                images(img_glass, img_glasstxt)
                            elif 'PAPEL' in tipo_reciclaje:
                                images(img_carton, img_cartontxt)
                            elif 'METALES' in tipo_reciclaje:
                                images(img_metal, img_metaltxt)
                            elif 'ELECTRÓNICOS' in tipo_reciclaje:
                                images(img_medical, img_medicaltxt)
                        else:
                            # COLORES MEJORADOS: ROJO para otros objetos
                            color_rectangulo = (255, 0, 0)  # ROJO
                            color_texto = (255, 255, 255)   # BLANCO
                            texto = f'{class_name} - {int(conf * 100)}%'
                        
                        # Fondo NEGRO para el texto
                        (text_width, text_height), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_COMPLEX, 0.8, 2)
                        cv2.rectangle(frame_show, (x1, y1 - 35), (x1 + text_width + 10, y1), (0, 0, 0), -1)
                        
                        # Draw rectangle con grosor 3
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), color_rectangulo, 3)
                        
                        # Draw text con mejor visibilidad
                        cv2.putText(frame_show, texto, (x1 + 5, y1 - 10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.8, color_texto, 2)

            if detect == False:
                # Clean
                clean_lbl()

            # Resize
            frame_show = imutils.resize(frame_show, width=640)

            # Convertimos el video
            im = Image.fromarray(frame_show)
            img = ImageTk.PhotoImage(image=im)

            # Mostramos en el GUI
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, Scanning)

        else:
            cap.release()

# main
def ventana_principal():
    global cap, lblVideo, model, clsName, img_metal, img_glass, img_plastic, img_carton, img_medical
    global img_metaltxt, img_glasstxt, img_plastictxt, img_cartontxt, img_medicaltxt, pantalla, reciclables
    
    # Ventana principal
    pantalla = Tk()
    pantalla.title("RECICLAJE INTELIGENTE - COLORES MEJORADOS")
    pantalla.geometry("1280x720")
    pantalla.configure(bg='#1a1a1a')  # Fondo negro

    # Background personalizado con colores nuevos
    # Crear un canvas con fondo negro y elementos en blanco
    canvas = Canvas(pantalla, width=1280, height=720, bg='#1a1a1a', highlightthickness=0)
    canvas.place(x=0, y=0)
    
    # Título principal en blanco
    canvas.create_text(640, 50, text="SISTEMA DE RECICLAJE INTELIGENTE", 
                      font=("Arial", 24, "bold"), fill="white")
    
    # Subtítulo
    canvas.create_text(640, 90, text="Detector Automático de Materiales Reciclables", 
                      font=("Arial", 14), fill="white")
    
    # Marco para el video
    canvas.create_rectangle(310, 170, 950, 510, outline="white", width=2)
    canvas.create_text(630, 150, text="CÁMARA EN VIVO", 
                      font=("Arial", 16, "bold"), fill="white")
    
    # Marco para información de reciclaje
    canvas.create_rectangle(50, 250, 300, 450, outline="white", width=2)
    canvas.create_text(175, 230, text="TIPO DE MATERIAL", 
                      font=("Arial", 12, "bold"), fill="white")
    
    # Marco para instrucciones
    canvas.create_rectangle(970, 300, 1230, 450, outline="white", width=2)
    canvas.create_text(1100, 280, text="INSTRUCCIONES", 
                      font=("Arial", 12, "bold"), fill="white")
    
    # Texto de instrucciones
    instrucciones = [
        "1. Apunte la cámara al objeto",
        "2. El sistema detectará",
        "   automáticamente",
        "3. Se mostrará el tipo",
        "   de reciclaje",
        "4. Verde = Reciclable",
        "5. Rojo = No reciclable"
    ]
    
    y_pos = 320
    for instruccion in instrucciones:
        canvas.create_text(1100, y_pos, text=instruccion, 
                          font=("Arial", 10), fill="white", anchor="w")
        y_pos += 20

    # Modelo YOLO pre-entrenado
    print("🔄 Cargando modelo YOLO...")
    model = YOLO('yolov8n.pt')

    # Clases generales de YOLO
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

    # Objetos reciclables con clasificación mejorada y más específica
    reciclables = {
        # PLÁSTICOS
        'bottle': 'PLÁSTICO - BOTELLA',
        'cup': 'PLÁSTICO - VASO',
        'toothbrush': 'PLÁSTICO - CEPILLO',
        
        # VIDRIO
        'wine glass': 'VIDRIO - COPA',
        'bowl': 'VIDRIO - TAZÓN',
        'vase': 'VIDRIO - FLORERO',
        
        # PAPEL/CARTÓN
        'book': 'PAPEL - LIBRO',
        'newspaper': 'PAPEL - PERIÓDICO',
        'magazine': 'PAPEL - REVISTA',
        
        # METALES
        'refrigerator': 'METALES - REFRIGERADOR',
        'microwave': 'METALES - MICROONDAS',
        'oven': 'METALES - HORNO',
        'toaster': 'METALES - TOSTADORA',
        'fork': 'METALES - TENEDOR',
        'knife': 'METALES - CUCHILLO',
        'spoon': 'METALES - CUCHARA',
        'scissors': 'METALES - TIJERAS',
        
        # ELECTRÓNICOS
        'cell phone': 'ELECTRÓNICOS - CELULAR',
        'laptop': 'ELECTRÓNICOS - LAPTOP',
        'tv': 'ELECTRÓNICOS - TELEVISOR',
        'remote': 'ELECTRÓNICOS - CONTROL',
        'keyboard': 'ELECTRÓNICOS - TECLADO',
        'mouse': 'ELECTRÓNICOS - MOUSE',
        'clock': 'ELECTRÓNICOS - RELOJ',
        'hair drier': 'ELECTRÓNICOS - SECADOR'
    }

    # Images
    img_metal = cv2.imread("setUp/metal.png")
    img_glass = cv2.imread("setUp/vidrio.png")
    img_plastic = cv2.imread("setUp/plastico.png")
    img_carton = cv2.imread("setUp/carton.png")
    img_medical = cv2.imread("setUp/medical.png")
    img_metaltxt = cv2.imread("setUp/metaltxt.png")
    img_glasstxt = cv2.imread("setUp/vidriotxt.png")
    img_plastictxt = cv2.imread("setUp/plasticotxt.png")
    img_cartontxt = cv2.imread("setUp/cartontxt.png")
    img_medicaltxt = cv2.imread("setUp/medicaltxt.png")

    # Video con fondo negro
    lblVideo = Label(pantalla, bg='#1a1a1a')
    lblVideo.place(x=320, y=180)

    # Elegimos la camara
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 1280)
    cap.set(4, 720)
    Scanning()

    # Eject
    pantalla.mainloop()

if __name__ == "__main__":
    ventana_principal() 