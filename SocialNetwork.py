import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pygame  # Para la música 🎵

# ----- Clase que maneja el "cerebro" de la red social -----
class Graph:

    def __init__(self):
        # Diccionario que guarda la lista de amigos de cada usuario
        self.adjacency_list = {}

    def add_user(self, user):
        # Añade un nuevo usuario a la red si no existe ya
        if user not in self.adjacency_list:
            self.adjacency_list[user] = set()
            return True
        return False

    def add_friendship(self, user1, user2):
        # Crea una amistad entre dos usuarios (bidireccional)
        if user1 in self.adjacency_list and user2 in self.adjacency_list:
            self.adjacency_list[user1].add(user2)
            self.adjacency_list[user2].add(user1)
            return True
        return False

    def get_friends(self, user):
        # Devuelve la lista de amigos directos de un usuario
        if user in self.adjacency_list:
            return list(self.adjacency_list[user])
        return []

    def bfs_level_2(self, start_user):
        """
        Algoritmo BFS para sugerencias de amigos:
        Devuelve los amigos de amigos (nivel 2), que no son amigos directos
        """
        if start_user not in self.adjacency_list:
            return set()

        visited = {start_user}  # Usuarios ya revisados
        level_1 = set(self.adjacency_list[start_user])  # Amigos directos
        suggestions = set()  # Donde se guardan las sugerencias

        # Explora los amigos de los amigos
        for friend in level_1:
            for friend_of_friend in self.adjacency_list[friend]:
                if friend_of_friend not in visited and friend_of_friend not in level_1:
                    suggestions.add(friend_of_friend)

        return suggestions

# ----- Clase que maneja la interfaz gráfica -----
class SocialNetworkGUI:
    """
    Clase que diseña la interfaz gráfica para el usuario.
    Permite crear usuarios, crear amistades, buscar amigos y ver sugerencias.
    También muestra el grafo y reproduce música/GIF.
    """

    def __init__(self, root):
        # Configura la ventana principal
        self.root = root
        self.root.title("Social Network Graph Mayro Gameros")
        self.root.geometry("900x700")

        # Inicializa la música de fondo 🎵
        pygame.mixer.init()
        self.play_music()

        # Crea el grafo de la red social
        self.graph = Graph()
        self.node_positions = {}  # Guarda posiciones de los nodos para el dibujo
        self.gif_frames = []  # Guarda los fotogramas del GIF

        # Crea el marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Construye la interfaz
        self.create_control_panel()  # Panel con botones y entradas
        self.create_canvas()  # Área para visualizar el grafo
        self.create_gif_canvas()  # Área para la animación GIF
        self.load_background()  # Carga el GIF animado

    # ----- Música -----
    def play_music(self):
        """ Carga y reproduce la música en bucle """
        try:
            pygame.mixer.music.load("C:\\Users\\DELL\\Downloads\\Adoロックスター.mp3")
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error al cargar la música: {e}")

    def toggle_music(self):
        """ Permite pausar/reanudar la música """
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    # ----- Panel de control -----
    def create_control_panel(self):
        """ Crea los botones y entradas para controlar la red social """
        self.control_frame = ttk.LabelFrame(self.main_frame, text="Controles")
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Control de música
        music_frame = ttk.LabelFrame(self.control_frame, text="Control de Música")
        music_frame.pack(fill=tk.X, pady=5, padx=5)

        ttk.Button(music_frame, text="Play/Pause", command=self.toggle_music).pack(side=tk.LEFT, padx=5)

        self.volume_var = tk.DoubleVar(value=0.5)
        volume_scale = ttk.Scale(music_frame, from_=0, to=1, orient=tk.HORIZONTAL,
                                 variable=self.volume_var, command=self.change_volume)
        volume_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Entrada para agregar usuario
        ttk.Label(self.control_frame, text="Nombre de usuario:").pack(pady=5)
        self.user_entry = ttk.Entry(self.control_frame)
        self.user_entry.pack(pady=5)
        ttk.Button(self.control_frame, text="Agregar Usuario", command=self.add_user).pack(pady=5)

        # Entradas para crear amistad
        ttk.Label(self.control_frame, text="Usuario 1:").pack(pady=5)
        self.user1_entry = ttk.Entry(self.control_frame)
        self.user1_entry.pack(pady=5)

        ttk.Label(self.control_frame, text="Usuario 2:").pack(pady=5)
        self.user2_entry = ttk.Entry(self.control_frame)
        self.user2_entry.pack(pady=5)

        ttk.Button(self.control_frame, text="Crear Amistad", command=self.add_friendship).pack(pady=5)

        # Entrada para buscar usuario
        ttk.Label(self.control_frame, text="Buscar usuario:").pack(pady=5)
        self.search_entry = ttk.Entry(self.control_frame)
        self.search_entry.pack(pady=5)
        ttk.Button(self.control_frame, text="Buscar", command=self.search_user).pack(pady=5)

        # Área de resultados
        self.result_frame = ttk.LabelFrame(self.control_frame, text="Resultados")
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.result_text = tk.Text(self.result_frame, height=10, width=30)
        self.result_text.pack(pady=5, padx=5)

    def change_volume(self, *args):
        """ Ajusta el volumen de la música """
        pygame.mixer.music.set_volume(self.volume_var.get())

    # ----- Visualización del grafo -----
    def create_canvas(self):
        """ Crea el área donde se dibuja el grafo """
        self.canvas_frame = ttk.LabelFrame(self.main_frame, text="Visualización del Grafo")
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.canvas = tk.Canvas(self.canvas_frame, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

    # ----- Área para el GIF -----
    def create_gif_canvas(self):
        """ Crea el área donde se muestra la animación GIF """
        self.gif_frame = ttk.LabelFrame(self.main_frame, text="Animación")
        self.gif_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=5, pady=5)

        self.gif_canvas = tk.Canvas(self.gif_frame, bg='white', height=100)
        self.gif_canvas.pack(fill=tk.BOTH, expand=False)

    def load_background(self):
        """ Carga los fotogramas del GIF animado """
        try:
            gif_path = "C:\\Users\\DELL\\Downloads\\robin.gif"
            self.current_frame = 0

            gif = Image.open(gif_path)
            for frame in range(0, gif.n_frames):
                gif.seek(frame)
                frame_resized = gif.resize((1235, 135), Image.Resampling.LANCZOS)
                frame_image = ImageTk.PhotoImage(frame_resized)
                self.gif_frames.append(frame_image)

            if self.gif_frames:
                self.background_item = self.gif_canvas.create_image(0, 0, anchor='nw',
                                                                    image=self.gif_frames[0])
                self.animate_gif()
        except Exception as e:
            print(f"Error al cargar el GIF: {e}")
            self.gif_frames = []

    def animate_gif(self):
        """ Anima el GIF (cambia de fotograma automáticamente) """
        if self.gif_frames:
            self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
            self.gif_canvas.itemconfig(self.background_item, image=self.gif_frames[self.current_frame])
            self.root.after(20, self.animate_gif)

    # ----- Actualiza el dibujo del grafo -----
    def update_graph_visualization(self):
        """ Dibuja el grafo actualizado con nodos y conexiones """
        self.canvas.delete("graph")
        num_nodes = len(self.graph.adjacency_list)
        if num_nodes == 0:
            return

        circle_size = 40
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        margin_x = canvas_width * 0.2
        margin_y = canvas_height * 0.15

        effective_width = canvas_width - (2 * margin_x)
        effective_height = canvas_height - (2 * margin_y)

        self.node_positions = {}
        nodes = list(self.graph.adjacency_list.keys())

        # Posicionamiento tipo "cuadrícula"
        for i, node in enumerate(nodes):
            row = i // 4
            col = i % 4
            x = margin_x + (effective_width * (col + 1)) / 5
            y = margin_y + (effective_height * (row + 1)) / 3

            self.node_positions[node] = (x, y)

            # Dibuja el nodo
            self.canvas.create_oval(
                x - circle_size / 2, y - circle_size / 2,
                x + circle_size / 2, y + circle_size / 2,
                fill="#FF69B4",
                width=1,
                tags="graph"
            )

            # Dibuja el nombre del nodo
            self.canvas.create_text(
                x, y,
                text=node,
                font=("Arial", 9, "bold"),
                tags="graph"
            )

        # Dibuja las conexiones
        for user, friends in self.graph.adjacency_list.items():
            x1, y1 = self.node_positions[user]
            for friend in friends:
                if friend in self.node_positions:
                    x2, y2 = self.node_positions[friend]
                    self.canvas.create_line(
                        x1, y1, x2, y2,
                        tags="graph",
                        width=1,
                        fill="#333333"
                    )

    # ----- Funcionalidad para el usuario -----
    def add_user(self):
        """ Agrega un nuevo usuario a la red """
        username = self.user_entry.get().strip()
        if username:
            if self.graph.add_user(username):
                self.update_graph_visualization()
                self.user_entry.delete(0, tk.END)
                messagebox.showinfo("Éxito", f"Usuario {username} agregado correctamente")
            else:
                messagebox.showerror("Error", "El usuario ya existe")
        else:
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario")

    def add_friendship(self):
        """ Crea una amistad entre dos usuarios """
        user1 = self.user1_entry.get().strip()
        user2 = self.user2_entry.get().strip()

        if user1 and user2:
            if self.graph.add_friendship(user1, user2):
                self.update_graph_visualization()
                self.user1_entry.delete(0, tk.END)
                self.user2_entry.delete(0, tk.END)
                messagebox.showinfo("Éxito", f"Amistad creada entre {user1} y {user2}")
            else:
                messagebox.showerror("Error", "Uno o ambos usuarios no existen")
        else:
            messagebox.showerror("Error", "Por favor ingrese ambos usuarios")

    def search_user(self):
        """ Muestra los amigos y sugerencias de un usuario """
        username = self.search_entry.get().strip()
        if username in self.graph.adjacency_list:
            friends = self.graph.get_friends(username)
            suggestions = self.graph.bfs_level_2(username)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Amigos de {username}:\n")
            for friend in friends:
                self.result_text.insert(tk.END, f"- {friend}\n")

            self.result_text.insert(tk.END, "\nSugerencias de amistad:\n")
            for suggestion in suggestions:
                self.result_text.insert(tk.END, f"- {suggestion}\n")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    # ----- Al cerrar -----
    def __del__(self):
        """ Detiene la música al cerrar la aplicación """
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass

# ----- Main -----
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialNetworkGUI(root)
    root.mainloop()
