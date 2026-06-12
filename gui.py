import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ShotCalculatorGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FRC Aimbot")
        self.geometry("1400x800")
        ctk.set_appearance_mode("dark")

        self.sidebar = ctk.CTkFrame(self, width=350)
        self.sidebar.pack(side = "left", fill = "y", padx = 10, pady = 10)

        self.tabs = ctk.CTkTabview(self.sidebar)
        self.tabs.pack(fill = "both", expand = True)

        self.tabs.add("Robot")
        self.tabs.add("Game Piece")
        self.tabs.add("Environment")
        self.tabs.add("Targets")
        self.tabs.add("Sandbox")


        self.plot_frame = ctk.CTkFrame(self)
        self.plot_frame.pack(side = "right", fill = "both", expand = True, padx = 10, pady = 10)
        self.fig = plt.Figure(figsize = (8,8), facecolor = "#2b2b2b")
        self.ax = self.fig.add_subplot(111, projection = '3d')
        self.ax.set_facecolor('#2b2b2b')
        self.ax.tick_params(colors = 'white')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill = "both", expand = True)



if __name__ == "__main__":
    app = ShotCalculatorGUI()
    app.mainloop()
