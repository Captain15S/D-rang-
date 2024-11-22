from tkinter import Tk, Canvas, Button
from avatar import DérangéAvatar
from matrix_bg import MatrixBackground

def main():
    # Fenêtre principale
    root = Tk()
    root.title("Dérangé - Assistant IA")
    canvas = Canvas(root, width=300, height=300, bg="black")
    canvas.pack()

    # Initialisation des composants
    avatar = DérangéAvatar(canvas)
    matrix = MatrixBackground(canvas)

    # Animation de fond
    def animate():
        matrix.update()
        root.after(100, animate)

    # Commandes pour l'avatar
    def simulate_talk():
        avatar.talk()

    def simulate_blink():
        avatar.blink()

    # Boutons pour interactions
    Button(root, text="Parler", command=simulate_talk).pack()
    Button(root, text="Cligner", command=simulate_blink).pack()

    animate()
    root.mainloop()

if __name__ == "__main__":
    main()