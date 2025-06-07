# S11-Implementacion-Grafos-Amigos-Sugerencias
# Social Network Graph Visualization

## Desarrollado por: MayroGamerosXZ
## Fecha: 2025-04-27

## Descripción
Este proyecto implementa una aplicación de visualización de redes sociales utilizando Python y Tkinter. Permite crear y visualizar conexiones entre usuarios en un grafo interactivo, con características adicionales como reproducción de música y animaciones GIF.

## Características Principales

### 1. Visualización de Grafo Social
- Representación visual de usuarios como nodos
- Conexiones entre usuarios mostradas como líneas
- Disposición automática de nodos en el espacio
- Colores personalizados para nodos (#FF69B4) y conexiones

### 2. Gestión de Usuarios
- Agregar nuevos usuarios
- Crear conexiones entre usuarios existentes
- Búsqueda de usuarios
- Visualización de amigos y sugerencias de amistad

### 3. Características Multimedia
- Reproducción de música de fondo
- Control de reproducción (Play/Pause)
- Control deslizante de volumen
- Animación GIF en la parte inferior

## Requisitos del Sistema
```python
# Librerías necesarias
pip install tkinter
pip install pillow
pip install pygame
```

## Estructura del Proyecto

### Clases Principales

1. **Graph**
   - Manejo de la estructura de datos del grafo
   - Implementación de relaciones entre usuarios
   - Algoritmos de búsqueda para sugerencias

2. **SocialNetworkGUI**
   - Interfaz gráfica principal
   - Gestión de visualización
   - Control de multimedia

## Funcionalidades

### Gestión de Usuarios
```python
def add_user(self):
    # Agregar un nuevo usuario al grafo
    # Validación de usuarios existentes
```

### Gestión de Amistades
```python
def add_friendship(self):
    # Crear conexiones entre usuarios
    # Validación de relaciones
```

### Visualización
```python
def update_graph_visualization(self):
    # Actualización del grafo visual
    # Disposición de nodos y conexiones
```

## Configuración de Multimedia

### Música
- Formato: MP3
- Ubicación por defecto: `C:\Users\Usuario\Downloads\Adoロックスター.mp3`
- Controles: Play/Pause y volumen ajustable

### Animación
- Formato: GIF
- Ubicación por defecto: `C:\Users\Usuario\Downloads\robin.gif`
- Tamaño ajustable automáticamente

## Personalización

### Colores y Estilos
- Nodos: Rosa (#FF69B4)
- Conexiones: Gris oscuro (#333333)
- Fuente: Arial 9 Bold

### Dimensiones
- Ventana principal: 900x700 píxeles
- Nodos: 40 píxeles de diámetro
- Animación GIF: 1220x200 píxeles

## Uso del Sistema

1. **Iniciar la Aplicación**
   ```python
   python social_network.py
   ```

2. **Agregar Usuarios**
   - Ingresar nombre en el campo "Nombre de usuario"
   - Hacer clic en "Agregar Usuario"

3. **Crear Conexiones**
   - Ingresar dos usuarios existentes
   - Hacer clic en "Crear Amistad"

4. **Buscar Usuarios**
   - Ingresar nombre en campo de búsqueda
   - Ver amigos y sugerencias en el panel de resultados

## Control de Multimedia

1. **Música**
   - Botón Play/Pause para control de reproducción
   - Deslizador para ajuste de volumen

2. **Animación**
   - GIF automático en panel inferior
   - Velocidad de reproducción: 20ms por frame

## Notas de Implementación

### Mejores Prácticas
- Manejo de errores para carga de archivos multimedia
- Limpieza de recursos al cerrar
- Validación de entradas de usuario

### Consideraciones Técnicas
- Uso de pygame para reproducción de audio
- PIL para manejo de imágenes GIF
- Tkinter para interfaz gráfica

## Futuras Mejoras Posibles
1. Exportación de grafos
2. Temas visuales personalizables
3. Más opciones de multimedia
4. Persistencia de datos
5. Algoritmos adicionales de sugerencias


#Descargar siguientes archivos y tenerlo en carpeta descarga
https://drive.google.com/drive/folders/17OpalCYsHFPoROtWA2UZqQGenHxQr5Xb?usp=sharing 

## Contacto
Desarrollador: MayroGamerosXZ
Fecha de última actualización: 2025-04-27
