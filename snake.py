import pygame
import random 

class App(object):
    def __init__(self):
        self.run()
        self.__direction = "right"
        self.__score = 0
        self.__dt = 0
        self.__position_play = pygame.Vector2(self.__screen.get_height()/3,self.__screen.get_width()/3)#position of player

        self.__RUNNING = True
        self.__FLAG = False


        while self.__RUNNING:
            self.score_tab()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__RUNNING = False

            self.background()
            self.player()
            self.movement(self.__direction)

            self.__key = pygame.key.get_pressed()
            self.event_handling(self.__key)

            self.score_tab()

            if self.__FLAG == False:
                self.point()
                self.__FLAG = True
                
            pygame.display.flip()
            self.fps()

        self.exit()

    def score_tab(self):

        self.__font = pygame.font.SysFont('comicsans', 30)
        self.__label = self.__font.render(f'WYNIK: {self.__score}', 1, (255, 255, 255))
        self.__screen.blit(self.__label, (25,25))


    def background(self):
        self.__screen.fill("#95BF50")
        pass

    def player(self):
        self.__player = pygame.draw.circle(self.__screen, "#1E8234", self.__position_play, 25)


    def point(self):
        self.__point = pygame.Vector2(100,100)
        
        if random.randint(0,5) == 0:
            pygame.draw.circle(self.__screen , "blue" , self.__point , 20)
        else:
            pygame.draw.circle(self.__screen , "red" , self.__point , 20)

        pygame.display.update()


    def movement(self,direction):

        if direction == "left":
            self.__position_play.x -= 10
        elif direction == "right":
            self.__position_play.x += 10
        elif direction == "up":
            self.__position_play.y -= 10
        elif direction == "down":
            self.__position_play.y += 10


    def event_handling(self,event):
        if event[pygame.K_LEFT] or event[pygame.K_a]:
            self.__direction = "left"
        elif event[pygame.K_RIGHT] or event[pygame.K_d]:
            self.__direction = "right"
        elif event[pygame.K_UP] or event[pygame.K_w]:
            self.__direction = "up"
        elif event[pygame.K_DOWN] or event[pygame.K_s]:
            self.__direction = "down"
        elif event[pygame.K_ESCAPE] or event[pygame.K_e]:
            self.__RUNNING = False


    def fps(self):
        self.__dt = self.__clock.tick(45)/1000 + self.__score


    def run(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = pygame.time.Clock()
        # pygame.display.toggle_fullscreen() # turning on the fullscreen
        pygame.display.set_caption("Better Snake")
        pygame.display.set_icon(pygame.image.load("snake.jpg"))


    def exit(self):
        pygame.quit()


Snake = App()