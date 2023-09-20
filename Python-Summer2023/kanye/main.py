import tkinter as tk
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text,text= quote)

window = tk.Tk()
window.title("Kanye says....")
window.config(padx=50,pady=50)


canvas = tk.Canvas(width=300,height=414)
background_img = tk.PhotoImage(file="background.png")
canvas.create_image(150,207,image= background_img)
quote_text = canvas.create_text(150,207,text= f"Kanye quote",width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
emoji = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(image= emoji,highlightthickness=0,command= get_quote)
kanye_button.grid(row=1,column=0)




window.mainloop()