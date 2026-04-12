import tkinter as tk
from tkinter import ttk
import ipaddress

class RedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Red WAN Colombia - Proyecto QA")
        self.root.geometry("900x500")
        self.root.configure(bg="#f0f0f0")

        # Título estilo Neo-brutalista (Bordes gruesos)
        title_label = tk.Label(
            root, text="MATRIZ DE DIRECCIONAMIENTO WAN", 
            font=("Arial", 18, "bold"), bg="#000", fg="#fff", pady=10
        )
        title_label.pack(fill=tk.X, padx=10, pady=10)

        # Definición de datos (Basado en tu imagen de Packet Tracer)
        self.datos = [
            ["BOGOTÁ", "Bog", "192.160.100.0/24"],
            ["IBAGUÉ", "1ra", "192.171.0.0/29"],
            ["PEREIRA", "2da", "192.168.28.0/23"],
            ["MEDELLÍN", "3ra", "192.169.50.0/22"],
            ["NEIVA", "5ta", "192.170.28.0/27"],
            ["CALI", "Últ.", "192.172.40.0/26"]
        ]

        self.crear_tabla()

    def crear_tabla(self):
        # Frame para la tabla
        frame = tk.Frame(self.root, bd=2, relief="solid")
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Configuración de estilo de la tabla
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", rowheight=30, font=("Arial", 10))

        # Columnas según tu dibujo
        columns = ("router", "subred", "dir_red", "dir_ip", "mask_red")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")

        self.tree.heading("router", text="ROUTER")
        self.tree.heading("subred", text="SUBRED")
        self.tree.heading("dir_red", text="DIR RED")
        self.tree.heading("dir_ip", text="DIR IP (Gateway)")
        self.tree.heading("mask_red", text="MASK RED")

        # Ajuste de ancho de columnas
        for col in columns:
            self.tree.column(col, anchor="center", width=150)

        # Insertar datos calculados
        for item in self.datos:
            net = ipaddress.IPv4Network(item[2])
            dir_red = str(net.network_address)
            dir_ip = str(list(net.hosts())[0]) # Gateway
            mask_red = str(net.netmask)
            
            self.tree.insert("", tk.END, values=(item[0], item[1], dir_red, dir_ip, mask_red))

        self.tree.pack(expand=True, fill="both")

        # Botón de salida
        btn_salir = tk.Button(
            self.root, text="CERRAR", command=self.root.quit,
            bg="#ff4d4d", fg="white", font=("Arial", 10, "bold"), 
            bd=3, relief="raised", padx=20
        )
        btn_salir.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RedApp(root)
    root.mainloop()
