import tkinter as tk
from PIL import Image, ImageTk
import random
import math
inning_number = 1

#Fireworks Window
def end_of_game():
   window3 = tk.Tk()
   window3.title("Game Over")
   canvas = tk.Canvas(window3, width=600, height=400, bg="black")
   canvas.pack()
   winner_logo_frame = tk.Frame(window3, width=169, height=100, bg="white", relief="solid", bd=1)
   winner_logo_frame.place(x=215.5, y=65)
   def show_team_logo(team, frame):
       team_image_path = team_images.get(team)
       if team_image_path:
           try:
               original_image = Image.open(team_image_path)
               resized_image = original_image.resize((169, 100))
               tk_image = ImageTk.PhotoImage(resized_image)
               frame.image = tk_image
               display_label = tk.Label(frame, image=tk_image, bg="white")
               display_label.pack(anchor=tk.CENTER)
           except Exception as e:
               print(f"Error loading image for {team}: {e}")
       else:
           print(f"Team image not found for {team}")
  
   def place_logos_on_scoreboard():
       if home_total > guest_total:
           show_team_logo(home_team, winner_logo_frame)
       elif home_total < guest_total:
           show_team_logo(away_team, winner_logo_frame)
       elif home_total == guest_total:
           tie_label = tk.Label(
               window3,
               text=("It's a tie!"),
               bg= "black",
               fg="white",
               font=("Helvetica", 30, "bold"),
           )
           tie_label.place(x=235, y=80)
           winner_logo_frame.after(0, lambda: (winner_logo_frame.destroy()))

   place_logos_on_scoreboard()
  
   def create_firework(canvas, x, y, color):
       particles = []
       for _ in range(80):
           angle = random.uniform(0, 2 * math.pi)
           speed = random.uniform(1, 5)
           x_vel = speed * math.cos(angle)
           y_vel = speed * math.sin(angle)
           particle = canvas.create_oval(x, y, x + 4, y + 4, fill=color)
           particles.append((particle, x_vel, y_vel))
       return particles

   def animate_firework(canvas, particles):
       for particle, dx, dy in particles:
           canvas.move(particle, dx, dy)
           coords = canvas.coords(particle)
           if coords[0] < 0 or coords[1] < 0 or coords[2] > 600 or coords[3] > 400:
               canvas.delete(particle)
               particles.remove((particle, dx, dy))
       if particles:
           canvas.after(50, lambda: animate_firework(canvas, particles))

   def launch_firework(event):
       x, y = event.x, event.y
       color = random.choice(["red", "blue", "yellow", "green", "orange"])
       particles = create_firework(canvas, x, y, color)
       animate_firework(canvas, particles)

   canvas.bind("<Button-1>", launch_firework)

   final_score_label = tk.Label(
       window3,
       text=f"Final Score: {guest_total} - {home_total}",
       bg="black",
       fg="red",
       font=("Helvetica", 30, "bold"),
   )
   instructions_label = tk.Label(
       window3,
       text=("Click for FIREWORKS!!"),
       bg= "black",
       fg="white",
       font=("Helvetica", 20, "bold"),
   )
   def winning_label():
       if home_total > guest_total:
           winning_team_label = tk.Label(
               window3,
               text=f"The {home_title} win!",
               bg= "black",
               fg="red",
               font=("Helvetica", 30, "bold"),
           )
           winning_team_label.place(x=175, y=215)
       if home_total < guest_total:
           winner_label = tk.Label(
               window3,
               text=f"The {away_title} win!",
               bg= "black",
               fg="red",
               font=("Helvetica", 30, "bold"),
           )
           winner_label.place(x=175, y=215)
   winning_label()
   final_score_label.place(x=175, y=180)
   instructions_label.place(x=185, y=370)
   window3.mainloop()

color1 = "white"
color2 = "black"
guest_total = 0
home_total = 0

#Dictionary of team images
team_images = {
   "angels": "./Images/Angels.png",
   "astros": "./Images/Astros.png",
   "athletics": "./Images/Athletics.png",
   "bluejays": "./Images/Blue Jays.png",
   "braves": "./Images/Braves.png",
   "brewers": "./Images/Brewers.png",
   "cardinals": "./Images/Cardinals.png",
   "cubs": "./Images/Cubs.png",
   "diamondbacks": "./Images/Diamondbacks.png",
   "dodgers": "./Images/Dodgers.png",
   "giants": "./Images/Giants.png",
   "guardians": "./Images/Guardians.png",
   "mariners": "./Images/Mariners.png",
   "marlins": "./Images/Marlins.png",
   "mets": "./Images/Mets.png",
   "nationals": "./Images/Nationals.png",
   "orioles": "./Images/Orioles.png",
   "padres": "./Images/Padres.png",
   "phillies": "./Images/Phillies.png",
   "pirates": "./Images/Pirates.png",
   "rangers": "./Images/Rangers.png",
   "rays": "./Images/Rays.png",
   "redsox": "./Images/Red Sox.png",
   "reds": "./Images/Reds.png",
   "rockies": "./Images/Rockies.png",
   "royals": "./Images/Royals.png",
   "tigers": "./Images/Tigers.png",
   "twins": "./Images/Twins.png",
   "whitesox": "./Images/White Sox.png",
   "yankees": "./Images/Yankees.png"
}

def display_error(message):
   error_label.config(text=message)
   error_label.pack(pady=5)
   window.after(3000, lambda: error_label.config(text=""))
   save_team()
def display_message(message):
   message_label.config(text=message)
   message_label.pack(pady=5)
def clear_frames():
   for widget in home_frame.winfo_children():
       widget.destroy()
   for widget in away_frame.winfo_children():
       widget.destroy()
def show_team_logo(team, frame):
   team_image_path = team_images.get(team)
   if team_image_path:
       try:
           original_image = Image.open(team_image_path)
           resized_image = original_image.resize((169, 100))
           tk_image = ImageTk.PhotoImage(resized_image)
           frame.image = tk_image
           display_label = tk.Label(frame, image=tk_image, bg="white")
           display_label.pack(anchor=tk.CENTER)
       except Exception as e:
           print(f"Error loading image for {team}: {e}")
   else:
       print(f"Team image not found for {team}")
def save_team():
   clear_frames()
   global home_team
   home_team = home_team_entry.get().strip().lower().replace(" ", "")
   global away_team
   away_team = away_team_entry.get().strip().lower().replace(" ", "")
   if not home_team or not away_team:
       display_error("Error: both teams required!")
       return
   if home_team == away_team:
       display_error("Error: must be different teams!")
       return
   if home_team not in team_images:
       display_error("Invalid home team name!")
       return
   if away_team not in team_images:
       display_error("Invalid away team name!")
       return
   global home_title
   home_title = home_team.capitalize()
   global away_title
   away_title = away_team.capitalize()
   show_team_logo(home_team, home_frame)
   show_team_logo(away_team, away_frame)
   display_message("Let's play ball! Batter up!")
   window.after(3000, lambda: (window.destroy(), scoreboard()))

#Open window
window = tk.Tk()
window.title("Select Your Teams")
window.configure(bg="#00693e")
window.geometry('507x350')
greeting = tk.Label(window, text="Welcome to the game!\nPlease input your teams to begin...",
                   bg="#00693e", fg="white", font=('Arial', 18, 'bold'), pady=10)
greeting.pack()

#Team Input Section
input_frame = tk.Frame(window, bg="#00693e")
input_frame.pack(pady=10)
home_label = tk.Label(input_frame, text="Home Team:", bg="#00693e", fg='white', font=('Arial', 12, 'bold'))
home_label.grid(row=0, column=0, padx=5, sticky="w")
home_team_entry = tk.Entry(input_frame, bg="#ffffff", font=('Arial', 12), width=30)
home_team_entry.grid(row=0, column=1, padx=5)
away_label = tk.Label(input_frame, text="Away Team:", bg="#00693e", fg='white', font=('Arial', 12, 'bold'))
away_label.grid(row=1, column=0, padx=5, sticky="w")
away_team_entry = tk.Entry(input_frame, bg="#ffffff", font=('Arial', 12), width=30)
away_team_entry.grid(row=1, column=1)

#Error Label
error_label = tk.Label(window, text="", bg="#00693e", fg="white", font=('Arial', 12, 'bold'))
error_label.pack() 

#Message Label
message_label = tk.Label(window, text="", bg="#00693e", fg="white", font=('Arial', 12, 'bold'))
message_label.pack()

#Submit Button
submit_button = tk.Button(window, text="Submit", command=save_team, bg="#00693e")
submit_button.pack()

#Logo Frames
logo_frame = tk.Frame(window, bg="#00693e")
logo_frame.pack(fill="x", pady=10)
home_frame = tk.Frame(logo_frame, width=169, height=100, bg="white", relief="solid", bd=1)
home_frame.pack(side="right", padx=10)
away_frame = tk.Frame(logo_frame, width=169, height=100, bg="white", relief="solid", bd=1)
away_frame.pack(side="left", padx=10)

#"Vs" Emblem
vs_emblem = tk.Label(logo_frame, text="Vs.", bg="#00693e", font=('Arial', 30, 'bold'), fg="#ffffff")
vs_emblem.pack(side="bottom")

#Code for scoreboard window
def scoreboard():
   global home_logo_frame, away_logo_frame
   window2 = tk.Tk()
   window2.title("Scoreboard")
   window2.geometry("960x510")
   window2.configure(bg="#00693e")
  
   #Main Rectangle Border
   main_frame = tk.Canvas(window2, width=950, height=300, background="#00693e")
   main_frame.pack(padx=5, pady=5)
  
   #Score Rectangle Border
   main_frame.create_rectangle(230, 0, 710, 130, outline="white", width=5)
  
   #Logo frames
   away_logo_frame = tk.Frame(window2, width=169, height=100, bg="white", relief="solid", bd=1)
   away_logo_frame.place(x=35, y=30)
   home_logo_frame = tk.Frame(window2, width=169, height=100, bg="white", relief="solid", bd=1)
   home_logo_frame.place(x=750, y=30)
  
   #Funcion to show logos
   def place_logos_on_scoreboard():
       show_team_logo(home_team, home_logo_frame)
       show_team_logo(away_team, away_logo_frame)
   place_logos_on_scoreboard()

   #Home and Away Score Labels
   guest_text = main_frame.create_text(145, 200, text="GUEST", fill=f"{color1}", font=("Helvetica", 38, "bold", "italic"))
   home_text = main_frame.create_text(150, 260, text="HOME", fill=f"{color2}", font=("Helvetica", 38, "bold", "italic"))
  
   #Inning Numbers
   for x, inning in enumerate(range(1, 11)):
       main_frame.create_text(246 + x * 48, 155, text=str(inning), fill="white", font=("Helvetica", 30, "bold", "italic"))
  
   #Guest Score Boxes and Labels
   guest_scores = []
   for x in range(10):
       main_frame.create_rectangle(233 + x * 48, 178, 263 + x * 48, 221, fill="black")
       lbl = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 30, "bold"))
       lbl.place(x=240 + x * 48, y=188, width=28, height=30)
       guest_scores.append(lbl)
  
   #Total Runs Label
   main_frame.create_text(755, 155, text="R", fill="white", font=("Helvetica", 30, "bold", "italic"))
  
   #Guest Total Box and Label
   main_frame.create_rectangle(728, 178, 783, 221, fill="black")
   guest_total_label = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 30, "bold"))
   guest_total_label.place(x=737, y=188, width=50, height=30)
  
   #Home Score Boxes and Labels
   home_scores = []
   for x in range(10):
       main_frame.create_rectangle(233 + x * 48, 235, 263 + x * 48, 278, fill="black")
       lbl = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 30, "bold"))
       lbl.place(x=240 + x * 48, y=245, width=28, height=30)
       home_scores.append(lbl)
  
   #Home Total Box and Label
   main_frame.create_rectangle(728, 235, 783, 278, fill="black")
   home_total_label = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 30, "bold"))
   home_total_label.place(x=737, y=245, width=50, height=30)
  
   #Ball Strike and Out Labels
   main_frame.create_text(305, 25, text="BALL", fill="white", font=("Helvetica", 34, "bold", "italic"))
   main_frame.create_text(475, 25, text="STRIKE", fill="white", font=("Helvetica", 34, "bold", "italic"))
   main_frame.create_text(635, 25, text="OUT", fill="white", font=("Helvetica", 34, "bold", "italic"))
  
   #Ball Strike and Out Boxes
   main_frame.create_rectangle(285.5, 50, 327.5, 115, fill="black")
   main_frame.create_rectangle(455, 50, 497, 115, fill="black")
   main_frame.create_rectangle(613.5, 50, 655.5, 115, fill="black")
  
   #Starting numbers for counts
   ball_count = [0]
   strike_count = [0]
   out_count = [0]
   current_inning = [0]
   team_turn = ["guest"]
  
   #Labels
   ball_label = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 44, "bold"))
   strike_label = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 44, "bold"))
   out_label = tk.Label(window2, text="0", bg="black", fg="red", font=("Helvetica", 44, "bold"))
  
   #Label placements
   ball_label.place(x=297, y=58)
   strike_label.place(x=467, y=58)
   out_label.place(x=626, y=58)

   #Reset ball and strike counts
   def reset_ball_strike():
       ball_count[0] = 0
       strike_count[0] = 0
       ball_label.config(text="0")
       strike_label.config(text="0")
  
   #Switch  between home and guest
   def switch_turns():
       out_count[0] = 0
       out_label.config(text="0")
       switch_colors()
       if team_turn[0] == "guest":
           team_turn[0] = "home"
       else:
           team_turn[0] = "guest"
           current_inning[0] += 1
       main_frame.itemconfig(guest_text, fill=color1)
       main_frame.itemconfig(home_text, fill=color2)
       if current_inning[0] >= 8:
           if current_inning[0] == 8 and team_turn[0] == "home" and home_total > guest_total:
               window2.after(2000, (window2.destroy(), end_of_game()))
           elif current_inning[0] > 8: 
               if team_turn[0] == "guest" and guest_total > home_total:
                   window2.after(2000, (window2.destroy(), end_of_game()))
               elif team_turn[0] == "home" and home_total > guest_total:
                   window2.after(2000, (window2.destroy(), end_of_game()))

   def switch_colors():  
       if team_turn[0] == "home":
           global color1, color2
           color1 = "white"
           color2 = "black"
           next_inning()
       else:
           color1 = "black"
           color2 = "white"

   #Add out after three strikes
   def add_out():
       update_count(out_label, out_count, 3, switch_turns)
       reset_ball_strike()
  
   #Function to update total score
   def update_total():
       global guest_total, home_total
       guest_total = sum(int(lbl.cget("text")) for lbl in guest_scores)
       home_total = sum(int(lbl.cget("text")) for lbl in home_scores)
       guest_total_label.config(text=str(guest_total))
       home_total_label.config(text=str(home_total))
       if current_inning[0] >= 8:
           if current_inning[0] == 8 and team_turn[0] == "home" and home_total > guest_total:
               window2.after(2000, (window2.destroy(), end_of_game()))
           elif current_inning[0] > 8: 
               if team_turn[0] == "guest" and guest_total > home_total:
                   window2.after(2000, (window2.destroy(), end_of_game()))
               elif team_turn[0] == "home" and home_total > guest_total:
                   window2.after(2000, (window2.destroy(), end_of_game()))
 
   #Function to update count
   def update_count(label, count, limit, callback=None):
       count[0] += 1
       if count[0] == limit:
           reset_ball_strike()
           if callback:
               callback()
       else:
           label.config(text=str(count[0]))
   
   #Function to add score for the current team
   def increment_score():
       inning = current_inning[0]
       if inning <= 9:
           if team_turn[0] == "home":
               current_score = int(home_scores[inning].cget("text"))
               home_scores[inning].config(text=str(current_score + 1))
           else:
               current_score = int(guest_scores[inning].cget("text"))
               guest_scores[inning].config(text=str(current_score + 1))
       if current_inning[0] >= 8:
           if current_inning[0] == 8 and team_turn[0] == "home" and home_total > guest_total:
               window2.after(2000, (window2.destroy(), end_of_game()))
           elif current_inning[0] > 8: 
               if team_turn[0] == "guest" and guest_total > home_total:
                   window2.after(2000, (window2.destroy(), end_of_game()))
               elif team_turn[0] == "home" and home_total > guest_total:
                   window2.after(2000, (window2.destroy(), end_of_game()))
       reset_ball_strike()
       update_total()
      
   #Buttons
   ball_button = tk.Button(window2, height=5, text="Ball", font=("Helvetica", 22),
                          command=lambda: update_count(ball_label, ball_count, 4))
   strike_button = tk.Button(window2, height=5, text="Strike", font=("Helvetica", 22),
                            command=lambda: update_count(strike_label, strike_count, 3, add_out))
   run_button = tk.Button(window2, height=5, text="Run", font=("Helvetica", 22),
                            command=increment_score)
   out_button = tk.Button(window2, height=5, text="Out", font=("Helvetica", 22),
                            command=add_out)
  
   #Place buttons
   ball_button.place(x=130, y=335)
   strike_button.place(x=200, y=335)
   run_button.place(x=580, y=335)
   out_button.place(x=290, y=335)

   #Inning Box
   main_frame.create_rectangle(820, 178, 900, 278, fill="black")
   main_frame.create_text(860, 158, text="INN", fill="white", font=("Helvetica", 30, "bold", "italic"))
   inning_label = main_frame.create_text(860, 227, text=(inning_number), fill="red", font=("Helvetica", 60, "bold"))

   def next_inning():
       global inning_number
       if inning_number <= 9:
           inning_number
           inning_number += 1
           main_frame.itemconfig(inning_label, text=str(inning_number))
           reset_ball_strike()
       else:
           window2.after(1000, (window2.destroy(), end_of_game()))

def main():
   window.mainloop()
main()
