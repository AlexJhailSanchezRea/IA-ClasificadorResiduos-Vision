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
    lblimg = Label(pantalla)
    lblimg.place(x=75, y=260)

    lblimgtxt = Label(pantalla)
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
                    if conf > 0.5:
                        class_name = clsName[cls]
                        
                        # Verificar si es reciclable
                        if class_name in reciclables:
                            tipo_reciclaje = reciclables[class_name]
                            color_rectangulo = (0, 255, 0)  # Verde para reciclables
                            color_texto = (255, 255, 255)   # Blanco para texto
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
                            color_rectangulo = (0, 0, 255)  # Rojo para otros objetos
                            color_texto = (255, 255, 255)   # Blanco para texto
                            texto = f'{class_name} - {int(conf * 100)}%'
                        
                        # Agregar fondo negro al texto para mejor visibilidad
                        (text_width, text_height), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_COMPLEX, 0.7, 2)
                        cv2.rectangle(frame_show, (x1, y1 - 30), (x1 + text_width, y1), (0, 0, 0), -1)
                        
                        # Draw rectangle
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), color_rectangulo, 3)
                        
                        # Draw text
                        cv2.putText(frame_show, texto, (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.7, color_texto, 2)

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
    pantalla.title("RECICLAJE INTELIGENTE - Versión Funcional")
    pantalla.geometry("1280x720")

    # Background
    imagenF = PhotoImage(file="setUp/Canva.png")
    background = Label(image=imagenF, text="Inicio")
    background.place(x=0, y=0, relwidth=1, relheight=1)

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

    # Video
    lblVideo = Label(pantalla)
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