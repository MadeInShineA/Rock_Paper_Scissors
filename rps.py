import sys
import random
import pygame


def play ():

    #Here we set all the constants we are going to use
    WIDTH=500
    LENGHT=500
    FONT_SIZE=20

    MIN_X_PLAY_BUTTON=225
    MAX_X_PLAY_BUTTON=275
    MIN_Y_PLAY_BUTTON=390
    MAX_Y_PLAY_BUTTON=410

    MIN_X_ROCK_BUTTON=100
    MAX_X_ROCK_BUTTON=150
    MIN_Y_ROCK_BUTTON=390
    MAX_Y_ROCK_BUTTON=405

    MIN_X_PAPER_BUTTON = 220
    MAX_X_PAPER_BUTTON = 280
    MIN_Y_PAPER_BUTTON = 390
    MAX_Y_PAPER_BUTTON = 410

    MIN_X_SCISSORS_BUTTON=330
    MAX_X_SCISSORS_BUTTON=420
    MIN_Y_SCISSORS_BUTTON=390
    MAX_Y_SCISSORS_BUTTON=410

    MIN_X_YES_BUTTON=145
    MAX_X_YES_BUTTON=180
    MIN_Y_YES_BUTTON=290
    MAX_Y_YES_BUTTON=310

    MIN_X_NO_BUTTON=320
    MAX_X_NO_BUTTON=345
    MIN_Y_NO_BUTTON=290
    MAX_Y_NO_BUTTON=310

    WHITE_RESULTS_RECTANGLE_X_POSITION=0
    WHITE_RESULTS_RECTANGLE_Y_POSITIONS=200
    WHITE_RESULTS_RECTANGLE_X_SIZE=WIDTH
    WHITE_RESULTS_RECTANGLE_Y_SIZE=80

    WHITE_SCORE_RECTANGLE_X_POSITION=0
    WHITE_SCORE_RECTANGLE_Y_POSITION=90
    WHITE_SCORE_RECTANGLE_X_SIZE=WIDTH
    WHITE_SCORE_RECTANGLE_Y_SIZE=25

    #The list of the different options the player or CPU can pick
    OPTION_LIST = ["rock", "paper", "scissors"]

    window =pygame.display.set_mode((WIDTH,LENGHT))
    window.fill("white")
    pygame.display.flip()
    pygame.display.set_caption("Rock Paper Scissors")



    def draw_text(text,font_size,color,background_color,position):
        font=pygame.font.Font("melee_font.otf", font_size)
        text=font.render(text,True,color,background_color)
        text_rectangle=text.get_rect(center=position)
        window.blit(text,text_rectangle)
        pygame.display.flip()

    def change_background_hovered(text,text_color,min_x,max_x,min_y,max_y,hover_color,normal_color,position_x,position_y):
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] > min_x and mouse_position[0] < max_x and mouse_position[1] > min_y and mouse_position[1] < max_y:
            draw_text(text, FONT_SIZE, text_color, hover_color, (position_x, position_y))
        else:
            draw_text(text, FONT_SIZE, text_color, normal_color, (position_x, position_y))

    draw_text("Welcome to the RPS game",FONT_SIZE,"black","white",(WIDTH/2,80))
    draw_text("Play",FONT_SIZE,"black","green",(WIDTH/2,400))
    running=True


    image=pygame.image.load("rock-paper-scissors.png")
    image_rectangle=image.get_rect(center=(WIDTH/2,LENGHT/2))
    window.blit(image,image_rectangle)
    pygame.display.flip()

    list_score=[0,0]


    def option_pick(option_picked):
        pygame.draw.rect(window,"white",rect=(WHITE_RESULTS_RECTANGLE_X_POSITION,WHITE_RESULTS_RECTANGLE_Y_POSITIONS,WHITE_RESULTS_RECTANGLE_X_SIZE,WHITE_RESULTS_RECTANGLE_Y_SIZE))
        pygame.display.flip()
        option_picked_by_cpu=OPTION_LIST[random.randint(0,2)]
        player_score=list_score[0]
        cpu_score=list_score[1]
        if option_picked_by_cpu==option_picked:
            draw_text(f"You both picked {option_picked}",FONT_SIZE,"black","white",(WIDTH/2,LENGHT/2))
        if option_picked=="rock" :
            if option_picked_by_cpu=="paper":
                draw_text(f"You lost, your opponent picked {option_picked_by_cpu}", FONT_SIZE, "black", "white", (WIDTH / 2, LENGHT / 2))
                cpu_score+=1
            if option_picked_by_cpu=="scissors":
                draw_text(f"You won, your opponent picked {option_picked_by_cpu}", FONT_SIZE, "black", "white",(WIDTH / 2, LENGHT / 2))
                player_score+=1
        if option_picked=="paper":
            if option_picked_by_cpu=="scissors":
                draw_text(f"You lost, your opponent picked {option_picked_by_cpu}", FONT_SIZE, "black", "white", (WIDTH / 2, LENGHT / 2))
                cpu_score +=1
            if option_picked_by_cpu=="rock":
                draw_text(f"You won, your opponent picked {option_picked_by_cpu}", FONT_SIZE, "black", "white",(WIDTH / 2, LENGHT / 2))
                player_score+=1
        if option_picked == "scissors":
            if option_picked_by_cpu == "rock":
                draw_text(f"You lost, your opponent picked {option_picked_by_cpu}", FONT_SIZE, "black", "white",(WIDTH / 2, LENGHT / 2))
                cpu_score+=1
            if option_picked_by_cpu == "paper":
                draw_text(f"You won, your opponent picked {option_picked_by_cpu}", FONT_SIZE, "black", "white",(WIDTH / 2, LENGHT / 2))
                player_score+=1
        pygame.draw.rect(window,"white",rect=(WHITE_SCORE_RECTANGLE_X_POSITION,WHITE_SCORE_RECTANGLE_Y_POSITION,WHITE_SCORE_RECTANGLE_X_SIZE,WHITE_SCORE_RECTANGLE_Y_SIZE))
        draw_text(f"You {player_score} | {cpu_score} CPU", FONT_SIZE, "black", "white", (WIDTH / 2, 100))
        list_score[0]=player_score
        list_score[1]=cpu_score



    def game_run():
        window.fill("white")
        pygame.display.flip()
        draw_text("Score",FONT_SIZE,"black","white",(WIDTH/2,80))
        draw_text("Please chose your next move!",FONT_SIZE,"Black","White",(WIDTH/2,50))
        draw_text("Rock",FONT_SIZE,"#4ed95a","#D9514EFF",(WIDTH/4,400))
        draw_text("Paper",FONT_SIZE,"white","#2A2B2DFF",(2*WIDTH/4,400))
        draw_text("Scissors",FONT_SIZE,"#d8632d","#2DA8D8FF",(3*WIDTH/4,400))
        game_running=True
        while game_running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    print("Goodbye")
                    game_running = False
                if event.type == pygame.MOUSEMOTION:
                    change_background_hovered("Rock","#4ed95a",MIN_X_ROCK_BUTTON, MAX_X_ROCK_BUTTON, MIN_Y_ROCK_BUTTON, MAX_Y_ROCK_BUTTON, "Black", "#D9514EFF",WIDTH / 4, 400)
                    change_background_hovered("Paper","white",MIN_X_PAPER_BUTTON,MAX_X_PAPER_BUTTON,MIN_Y_PAPER_BUTTON,MAX_Y_PAPER_BUTTON,"red","#2A2B2DFF",WIDTH/2,400)
                    change_background_hovered("Scissors","#d8632d",MIN_X_SCISSORS_BUTTON,MAX_X_SCISSORS_BUTTON,MIN_Y_SCISSORS_BUTTON,MAX_Y_SCISSORS_BUTTON,"yellow","#2DA8D8FF",3*WIDTH/4,400)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position=pygame.mouse.get_pos()
                    if mouse_position[0] > MIN_X_ROCK_BUTTON and mouse_position[0] < MAX_X_ROCK_BUTTON and mouse_position[1] > MIN_Y_ROCK_BUTTON and mouse_position[1] < MAX_Y_ROCK_BUTTON:
                        option_pick("rock")
                    if mouse_position[0] > MIN_X_PAPER_BUTTON and mouse_position[0] < MAX_X_PAPER_BUTTON and mouse_position[1] > MIN_Y_PAPER_BUTTON and mouse_position[1] < MAX_Y_PAPER_BUTTON:
                        option_pick("paper")
                    if mouse_position[0] > MIN_X_SCISSORS_BUTTON and mouse_position[0] < MAX_X_SCISSORS_BUTTON and mouse_position[1] > MIN_Y_SCISSORS_BUTTON and mouse_position[1] < MAX_Y_SCISSORS_BUTTON:
                        option_pick("scissors")
            if list_score[0]==3:
                end()
                sys.exit()
            if list_score[1]==3:
                end()
                sys.exit()

    def end():
        end = True
        window.fill("white")
        if list_score[0]==3:
            draw_text("You won !",FONT_SIZE,"black","white",(WIDTH/2,100))
        else:
            draw_text("You lost...", FONT_SIZE, "black", "white", (WIDTH / 2, 100))
        draw_text("Play again?",FONT_SIZE,"black","white",(WIDTH/2,200))
        draw_text("Yes",FONT_SIZE,"black","green",(2*WIDTH/6,300))
        draw_text("No", FONT_SIZE, "black", "red", (4 * WIDTH / 6, 300))
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Goodbye")
                    end = False
                if event.type == pygame.MOUSEMOTION:
                    change_background_hovered("Yes","black",MIN_X_YES_BUTTON, MAX_X_YES_BUTTON, MIN_Y_YES_BUTTON, MAX_Y_YES_BUTTON, "#09FFCC", "green",2*WIDTH / 6, 300)
                    change_background_hovered("No","black",MIN_X_NO_BUTTON,MAX_X_NO_BUTTON,MIN_Y_NO_BUTTON,MAX_Y_NO_BUTTON,"#09FFCC","red",4*WIDTH/6,300)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()
                    if mouse_position[0] > MIN_X_YES_BUTTON and mouse_position[0] < MAX_X_YES_BUTTON and mouse_position[1] > MIN_Y_YES_BUTTON and mouse_position[1] < MAX_Y_YES_BUTTON:
                        end = False
                        play()
                    if mouse_position[0] > MIN_X_NO_BUTTON and mouse_position[0] < MAX_X_NO_BUTTON and mouse_position[1] > MIN_Y_NO_BUTTON and mouse_position[1] < MAX_Y_NO_BUTTON:
                        print("Goodbye")
                        sys.exit()





    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print("Goodbye")
                running=False
            if event.type==pygame.MOUSEMOTION:
                change_background_hovered("Play","black",MIN_X_PLAY_BUTTON,MAX_X_PLAY_BUTTON,MIN_Y_PLAY_BUTTON,MAX_Y_PLAY_BUTTON,"red","green",WIDTH/2,400)
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_position=pygame.mouse.get_pos()
                if mouse_position[0] >210 and mouse_position[0]<290 and mouse_position[1]>370 and mouse_position[1]<430:
                    game_run()
                    sys.exit()

pygame.init()
play()