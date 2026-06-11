import customtkinter as ctk

app = ctk.CTk()

app.geometry("1000x800")

left_frame = ctk.CTkFrame(app)

slider_dist = ctk.CTkSlider(left_frame, from_=2.0, to=10.0, command=update_plot)
slider_vrad = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
slider_vtan = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
slider_pitch = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)
slider_roll = ctk.CTkSlider(left_frame, from_=-5.0, to=5.0, command=update_plot)


def update_plot(event):
    v_rad = slider_vrad.get()
    v_tan = slider_vtan.get()
    pitch = slider_pitch.get()
    roll = slider_roll.get()

    inputs = np.array([[dist, height, v_rad, v_tan, pitch, roll]])

