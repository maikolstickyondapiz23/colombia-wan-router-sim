import ipaddress

class RedInfo:
    def __init__(self, nombre, red_cidr, id_subred="-"):
        self.nombre = nombre
        self.id_subred = str(id_subred)
        self.red_obj = ipaddress.IPv4Network(red_cidr)
        
        # Extraer los datos para la tabla en formato de texto
        self.dir_red = str(self.red_obj.network_address)
        self.mascara = str(self.red_obj.netmask)
        # La IP Gateway (normalmente la primera utilizable)
        self.ip_lan = str(list(self.red_obj.hosts())[0])

def generar_tabla_final():
    # Usando los datos de la topología compleja de tu imagen anterior
    # (Ciudad, Red CIDR, ID de subred anotado en la imagen)
    datos_lan = [
        RedInfo("IBAGUÉ", "192.171.0.0/29", "1ra"),
        RedInfo("PEREIRA", "192.168.28.0/23", "2da"),
        RedInfo("MEDELLÍN", "192.169.50.0/22", "3ra"),
        RedInfo("NEIVA", "192.170.28.0/27", "5ta"),
        RedInfo("CALI", "192.172.40.0/26", "Últ."),
        RedInfo("BOGOTÁ", "192.160.100.0/24", "Bog")
    ]

    # Enlaces WAN (las líneas rojas del Router central)
    # Aquí la 'DIR IP' es la IP que le pones al router central (R0) en ese enlace
    datos_wan = [
        RedInfo("R0 -> BOG", "190.0.0.0/30", "W0"),
        RedInfo("R0 -> CALI", "190.0.0.4/30", "W1"),
        RedInfo("R0 -> IBA", "190.0.0.8/30", "W2"),
        RedInfo("R0 -> NEI", "190.0.0.12/30", "W3"),
        RedInfo("R0 -> MED", "190.0.0.16/30", "W4"),
        RedInfo("R0 -> PER", "190.0.0.20/30", "W5")
    ]

    # Encabezados de tabla EXACTOS a tu imagen de referencia (en mayúsculas)
    header = f"{'ROUTER':<15} {'SUBRED':<8} {'DIR RED':<15} {'DIR IP':<15} {'MASK RED'}"
    
    # ------------------------------------------------------------------
    # TABLA 1: REDES LAN (Ciudades)
    # ------------------------------------------------------------------
    print("-" * 75)
    print(f"{'MATRIZ DE DIRECCIONAMIENTO LAN (CIUDADES COLOMBIA)':^75}")
    print("-" * 75)
    print(header)
    print("-" * 75)
    
    for c in datos_lan:
        # Se formatea para que la IP del router LAN (Gateway) se vea corta (ej. '1.1')
        # Pero como son redes de clase C/A, pondré la IP completa para QA.
        print(f"{c.nombre:<15} {c.id_subred:<8} {c.dir_red:<15} {c.ip_lan:<15} {c.mascara}")
    
    print("\n" + "="*75 + "\n")

    # ------------------------------------------------------------------
    # TABLA 2: ENLACES WAN (Conexiones de Router0)
    # ------------------------------------------------------------------
    print("-" * 75)
    print(f"{'MATRIZ DE ENLACES WAN (CONEXIONES CENTRALES R0)':^75}")
    print("-" * 75)
    print(header)
    print("-" * 75)
    
    for w in datos_wan:
        # En la columna 'DIR IP' de WAN, mostramos la IP que le toca al Router0 (R0)
        # La IP remota sería la siguiente utilizable.
        print(f"{w.nombre:<15} {w.id_subred:<8} {w.dir_red:<15} {w.ip_lan:<15} {w.mascara}")
        
    print("-" * 75)
    print("Nota: En la tabla WAN, 'DIR IP' es la IP de la interfaz Serial/Gigabit del Router0 (central).")

if __name__ == "__main__":
    generar_tabla_final()
