import tkinter as tk
import random


class SnakeGame:
    def __init__(self,master):
        self.master=master
        self.master.title("Snake Game")
        self.master.geometry("400x400")

        self.canvas=tk.Canvas(self.master,bg="black",width=400,height=400)
        self.canvas.pack()

        self.snake=[(100,100),(90,100),(80,100)]
        self.direction="Right"
        self.food=self.create_food()

        self.master.bind("<KeyPress>",self.change_direction)

        self.update()

    def create_food(self):
        x=random.randint(0,39)*10
        y=random.randint(0,39)*10
        self.canvas.create_rectangle(x,y,x+10,y+10,fill="red",tags="food")
        return x,y

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"


    def move(self):
        head=list(self.snake[0])
        if self.direction=="Up":
            head[1]-=10
        elif self.direction=="Down":
            head[1]+=10
        elif self.direction=="Left":
            head[0]-=10
        elif self.direction=="Right":
            head[0]+=10
        self.snake=[tuple(head)]+self.snake[:-1]

    def check_collision(self):
        head=self.snake[0]
        if (
                head[0]<0
                or head[0]>=400
                or head[1]<0
                or head[1]>=400
                or head in self.snake[1:]
        ):
            return True
        return False

    def check_food_collision(self):
        head=self.snake[0]
        if head==self.food:
            self.snake.append(self.snake[-1])
            self.canvas.delete("food")
            self.food=self.create_food()

    def update(self):
        if self.check_collision():
            self.canvas.create_text(
                200,200,text="Game Over",font=("Helvetica",16),fill="white"
            )
        else:
            self.move()
            self.check_food_collision()
            self.canvas.delete("snake")
            for segment in self.snake:
                self.canvas.create_rectangle(
                    segment[0],
                    segment[1],
                    segment[0]+10,
                    segment[1]+10,
                    fill="green",
                    tags="snake",
                )
            self.master.after(100,self.update)


if __name__=="__main__":
    root=tk.Tk()
    game=SnakeGame(root)
    root.mainloop()
