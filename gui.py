import customtkinter as ctk

app = ctk.CTk()

app.geometry("1000x800")

left_frame = ctk.CTkFrame(app)

slider_vrad = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
slider_vtan = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
slider_vrad = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
slider_vrad = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
