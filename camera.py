#camera working
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class KameraUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera")

        self.kamera = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        self.btn_kapat = ttk.Button(root, text="Close", command=self.kapat)
        self.btn_kapat.pack()

        self.goruntu_goster()

    def goruntu_goster(self):
        ret, frame = self.kamera.read()
        if ret:
            frame = cv2.flip(frame, 1)
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img_tk = ImageTk.PhotoImage(image=img)
            self.canvas.img_tk = img_tk
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.root.after(10, self.goruntu_goster)
        else:
            self.kapat()

    def kapat(self):
        self.kamera.release()
        self.root.destroy()

root = tk.Tk()
app = KameraUygulamasi(root)
root.mainloop()
