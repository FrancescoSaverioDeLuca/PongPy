import turtle


def main():
	wn= turtle.Screen()
	wn.title("Pong by Francesco")
	wn.bgcolor("black")
	wn.setup(width=800,height=600)
	wn.tracer(0)

	#Def paddle A 
	paddle_a = turtle.Turtle()
	paddle_a.speed(0)
	paddle_a.shape("square")
	paddle_a.color("white")
	paddle_a.penup()
	paddle_a.goto(-350,0)
	
	#Main Loop
	while True: 
		wn.update() 


	
main()
