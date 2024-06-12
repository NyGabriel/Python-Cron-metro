import tkinter as tk
import time

# Passo 2: Criando a Classe do Cronômetro
class Stopwatch:
    def __init__(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.start_time = None
        self.elapsed_time = 0

        # Passo 3: Configurando a Interface Gráfica
        self.root = tk.Tk()
        self.root.title("Cronômetro")

        self.display = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.display.pack()

        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.root, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.root, text="Resetar", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

    # Passo 4: Criando as Funções do Cronômetro
    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.hours, remainder = divmod(self.elapsed_time, 3600)
            self.minutes, self.seconds = divmod(remainder, 60)
            self.display.config(text=f"{int(self.hours):02}:{int(self.minutes):02}:{int(self.seconds):02}")
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        if not self.running:
            self.start_time = None
            self.elapsed_time = 0
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.display.config(text="00:00:00")

# Passo 5: Executando o Programa Principal
if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()
