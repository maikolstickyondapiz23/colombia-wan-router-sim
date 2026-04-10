# 🛰️ Colombia WAN Router Simulator

Este proyecto es un automatizador de **Networking** diseñado para calcular el direccionamiento IP de una red de área amplia (WAN) que conecta las principales ciudades de Colombia.

## 🚀 Características
* **Subneteo VLSM:** Cálculo automático de subredes optimizando el espacio de direcciones IP.
* **Enrutamiento Estático:** Generación de tablas de rutas para interconectar los nodos de las ciudades.
* **Topología Nacional:** Simulación basada en nodos reales (Bogotá, Medellín, Cali, Barranquilla).

## 🗺️ Topología de Red
La red está diseñada en una estructura de estrella/malla conectando:
* **Nodo Central:** Bogotá (Data Center Principal)
* **Nodos Regionales:** * Medellín (Nodo Occidente)
    * Cali (Nodo Suroccidente)
    * Barranquilla (Nodo Norte)

## 🛠️ Tecnologías
* **Lenguaje:** Python 3.x
* **Librerías:** `ipaddress` para lógica de red.

## 📝 Ejemplo de Direccionamiento (Planificación)
| Ciudad | Hosts Requeridos | Prefijo Sugerido |
| :--- | :--- | :--- |
| Bogotá | 5000 | /19 |
| Medellín | 3000 | /20 |
| Cali | 2000 | /21 |
| Barranquilla | 1500 | /21 |

---
Desarrollado con fines educativos para la gestión de infraestructura de red en Colombia. 🇨🇴
