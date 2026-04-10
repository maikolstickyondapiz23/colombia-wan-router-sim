import ipaddress

class CiudadNodo:
    def __init__(self, nombre, hosts_requeridos):
        self.nombre = nombre
        self.hosts_requeridos = hosts_requeridos
        self.subred = None
        self.gateway = None

def generador_red_colombia():
    print("="*50)
    print("SISTEMA DE CONFIGURACIÓN WAN - NODOS COLOMBIA")
    print("="*50)

    # 1. Definición de la Red Base (Clase A privada para grandes redes)
    try:
        red_maestra = ipaddress.IPv4Network("10.0.0.0/8")
    except ValueError:
        print("Error en la IP base.")
        return

    # 2. Configuración de Ciudades (Nodos)
    # Se ordenan de mayor a menor número de hosts (Regla de VLSM)
    nodos = [
        CiudadNodo("Bogotá", 5000),
        CiudadNodo("Medellín", 2500),
        CiudadNodo("Cali", 1200),
        CiudadNodo("Barranquilla", 800),
        CiudadNodo("Bucaramanga", 500)
    ]
    nodos.sort(key=lambda x: x.hosts_requeridos, reverse=True)

    # 3. Proceso de Subneteo
    print(f"\n[+] Iniciando Subneteo VLSM sobre la red: {red_maestra}")
    current_addr = red_maestra.network_address

    for nodo in nodos:
        # Calculamos el prefijo necesario para los hosts
        # Agregamos +2 para la IP de Red y el Broadcast
        prefix = 32 - (nodo.hosts_requeridos + 2).bit_length()
        
        # Crear la subred
        subred = ipaddress.IPv4Network((current_addr, prefix))
        nodo.subred = subred
        nodo.gateway = list(subred.hosts())[0] # Primera IP utilizable

        print(f"📍 {nodo.nombre:12} | Subred: {str(subred):15} | Gateway: {nodo.gateway}")
        
        # Movemos el puntero a la siguiente dirección disponible
        current_addr = subred.broadcast_address + 1

    # 4. Generación de Enrutamiento Estático (Mapeado lógico)
    print("\n" + "="*50)
    print("TABLA DE ENRUTAMIENTO ESTÁTICO (IP ROUTE)")
    print("="*50)
    
    for nodo_local in nodos:
        print(f"\n--- Configuración para Router {nodo_local.nombre} ---")
        print(f"! Interfaz LAN: ip address {nodo_local.gateway} {nodo_local.subred.netmask}")
        
        for nodo_destino in nodos:
            if nodo_local != nodo_destino:
                # Simulamos que el 'Next Hop' es la IP .2 de la subred del vecino
                next_hop = list(nodo_destino.subred.hosts())[1]
                print(f"ip route {nodo_destino.subred.network_address} {nodo_destino.subred.netmask} {next_hop}")

if __name__ == "__main__":
    generador_red_colombia()