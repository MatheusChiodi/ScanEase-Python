import cv2
import numpy as np
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import Label, Button, Frame
import threading
import winsound  # Para alerta sonoro ao detectar código

# Função para iniciar a leitura da câmera
def start_scanner():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Converter para escala de cinza (melhora a detecção)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        barcodes = decode(gray)

        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # Desenha um retângulo no código detectado
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Exibir o código na tela
            text = f"{barcode_type}: {barcode_data}"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Atualiza a interface gráfica com o código detectado
            barcode_label.config(text=f"📦 Código: {barcode_data} ({barcode_type})", fg="#28a745")

            # Emitir um som ao detectar um código
            winsound.Beep(1000, 200)

        cv2.imshow("📡 Leitor de Código de Barras", frame)

        # Pressionar "Q" para sair do scanner
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Função para rodar o scanner em uma thread separada
def start_scanner_thread():
    threading.Thread(target=start_scanner, daemon=True).start()

# Criando a interface gráfica profissional
root = tk.Tk()
root.title("📡 Leitor de Código de Barras")
root.geometry("500x400")
root.configure(bg="#f8f9fa")

# Estilo de Título
Label(root, text="📡 Leitor de Código de Barras", font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#333").pack(pady=10)

# Área de exibição do código detectado
barcode_frame = Frame(root, bg="black", width=400, height=80)
barcode_frame.pack(pady=10)
barcode_label = Label(barcode_frame, text="📦 Código: ---", font=("Arial", 14), bg="black", fg="white", width=40, height=2)
barcode_label.pack()

# Botão estilizado
def neon_effect(widget):
    widget.config(bg="#0f0", fg="black")
    root.after(200, lambda: widget.config(bg="#00ff00", fg="black"))
    root.after(400, lambda: widget.config(bg="#0f0", fg="black"))

# Botão de iniciar scanner
start_button = Button(
    root, 
    text="🔍 Iniciar Leitura", 
    font=("Arial", 14, "bold"), 
    bg="#007bff", 
    fg="white", 
    width=18, 
    height=2, 
    relief="flat",
    command=lambda: [neon_effect(start_button), start_scanner_thread()]
)
start_button.pack(pady=15)

# Botão de fechar
exit_button = Button(
    root, 
    text="❌ Fechar", 
    font=("Arial", 12, "bold"), 
    bg="red", 
    fg="white", 
    width=12, 
    height=2, 
    relief="flat", 
    command=root.quit
)
exit_button.pack(pady=5)

root.mainloop()
