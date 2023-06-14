import pygame
import random 

class App(object):
    def __init__(self):
        self.run()
        self.__direction = "right"
        self.__score = 1
        self.__dt = 0
        self.__position_play = pygame.Vector2(self.__screen.get_height()/3,self.__screen.get_width()/3)#position of player

        self.__RUNNING = True
        self.__GAINED = True


        while self.__RUNNING:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__RUNNING = False


            self.background()
            self.player()
            self.movement(self.__direction)

            self.__key = pygame.key.get_pressed()
            self.event_handling(self.__key)

            self.score_tab()

            if self.__GAINED:
                self.__position_point = pygame.Vector2(random.randint(50,self.__screen.get_height()-20),random.randint(50,self.__screen.get_height()-20))

                if random.randint(0,2)==0:
                    self.__color = "red"
                    self.__add = 1
                elif random.randint(0,2)==1:
                    self.__color = "purple"
                    self.__add = 2
                else:
                    self.__color = "orange"
                    self.__add = 3

                self.__GAINED = False

            self.check_point()

            self.point()

            pygame.display.flip()
            self.fps()

        self.exit()


    def check_point(self):
        for x in range(0,10):
            if self.__position_point.x+x == self.__position_play.x:
                self.__score += self.__add
                self.__GAINED = True
                return

        for x in range(0,10):
            if self.__position_point.y+x == self.__position_play.y:
                self.__score += self.__add
                self.__GAINED = True
                return


    def score_tab(self):

        self.__font = pygame.font.SysFont('comicsans', 40)
        self.__label = self.__font.render(f'Score: {self.__score-1}         ', 1, "black", "white")
        self.__screen.blit(self.__label, (0,0))
        
        self.__font = pygame.font.SysFont('comicsans',40)
        self.__label = self.__font.render(f'Red = 1          ', 1, "red", "white")
        self.__screen.blit(self.__label, (0,25))
        
        self.__font = pygame.font.SysFont('comicsans',40)
        self.__label = self.__font.render(f'Purple = 2     ', 1, "purple", "white")
        self.__screen.blit(self.__label, (0,52))
        
        self.__font = pygame.font.SysFont('comicsans',40)
        self.__label = self.__font.render(f'Orange = 3    ', 1, "orange", "white")
        self.__screen.blit(self.__label, (0,78))


    def background(self):
        self.__screen.fill("#95BF50")
        pass


    def player(self):
        self.__player = pygame.draw.circle(self.__screen, "#1E8234", self.__position_play, 25)


    def point(self):
        self.__point = pygame.draw.circle(self.__screen , self.__color , self.__position_point , 20)
        

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
        pygame.display.toggle_fullscreen() # turning on the fullscreen
        pygame.display.set_caption("Better Snake")
        pygame.display.set_icon(pygame.image.load("snake.jpg"))


    def exit(self):
        pygame.quit()


Snake = App()