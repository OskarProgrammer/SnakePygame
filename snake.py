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
            
            try:
                self.point()
                self.check_point()
            except:
                pass

            if self.check_lose():
                print(f"You lost, your score: {self.__score}")

                self.end()

                self.__score = 0

                self.__RUNNING = False

            pygame.display.flip()
            self.fps()

        self.exit()


    def end(self):
        self.background()

        #ustawienie obrazu koncowego
        self.__font = pygame.font.SysFont('comicsans', 50)
        self.__label = self.__font.render(f'You lost... Your score: {self.__score}', 1, "black", "white")
        self.__screen.blit(self.__label, (100,200))
        
        pygame.display.flip() # odswiezenie ekranu

        # while True:
        #     self.__key = pygame.key.get_pressed()

        #     if self.__key[pygame.K_LEFT]:
        #         break
        #     else:
        #         print("nothing")
        pygame.event.wait(timeout=2)


    def check_lose(self):
        if self.__position_play.x >= self.__screen.get_width() or self.__position_play.y >= self.__screen.get_height() or self.__position_play.x <= 0 or self.__position_play.y <= 0:
            return True
        return False


    def check_point(self):
        if self.__player_rect.colliderect(self.__point_rect):
            self.__score += self.__add
            self.__GAINED = True
        else:
            pass

    def score_tab(self):

        self.__font = pygame.font.SysFont('comicsans', 40)
        self.__label = self.__font.render(f'Score: {self.__score-1}         ', 1, "black", "white")
        self.__screen.blit(self.__label, (0,0))
        
        # self.__font = pygame.font.SysFont('comicsans',40)
        # self.__label = self.__font.render(f'Red = 1          ', 1, "red", "white")
        # self.__screen.blit(self.__label, (0,25))
        
        # self.__font = pygame.font.SysFont('comicsans',40)
        # self.__label = self.__font.render(f'Purple = 2     ', 1, "purple", "white")
        # self.__screen.blit(self.__label, (0,52))
        
        # self.__font = pygame.font.SysFont('comicsans',40)
        # self.__label = self.__font.render(f'Orange = 3    ', 1, "orange", "white")
        # self.__screen.blit(self.__label, (0,78))


    def background(self):
        self.__screen.fill("#95BF50")
        pass


    def player(self):
        self.__player_rect = pygame.Rect(self.__position_play.x, self.__position_play.y, 40, 40)

        pygame.draw.rect(self.__screen, "#1E8234", self.__player_rect)


    def point(self):
        self.__point_rect = pygame.Rect(self.__position_point.x, self.__position_point.y, 40, 40)

        pygame.draw.rect(self.__screen , self.__color, self.__point_rect) #draw the point circle on the choosen coordinates
        

    def movement(self,direction):

        if direction == "left":         
            self.__position_play.x -= 10 #move to the left by 10 pixels
        elif direction == "right":
            self.__position_play.x += 10 #move to the right by 10 pixels
        elif direction == "up":
            self.__position_play.y -= 10 #move to the up by 10 pixels
        elif direction == "down":
            self.__position_play.y += 10 #move to the down by 10 pixels


    def event_handling(self,event): #handling events 
        if event[pygame.K_LEFT] or event[pygame.K_a]: #change direction to left
            self.__direction = "left"
        elif event[pygame.K_RIGHT] or event[pygame.K_d]:#change direction to right
            self.__direction = "right"
        elif event[pygame.K_UP] or event[pygame.K_w]:#change direction to up
            self.__direction = "up"
        elif event[pygame.K_DOWN] or event[pygame.K_s]:#change direction to down
            self.__direction = "down"
        elif event[pygame.K_ESCAPE] or event[pygame.K_e]:#exit the application
            self.__RUNNING = False


    def fps(self):
        self.__dt = self.__clock.tick(45)/1000 + self.__score #configurating frame rate


    def run(self):
        pygame.init() #initialize application
        self.__screen = pygame.display.set_mode((800, 600)) #setting resolution
        self.__clock = pygame.time.Clock() #starting clock
        # pygame.display.toggle_fullscreen() # turning on the fullscreen
        pygame.display.set_caption("Better Snake") #setting the title of app
        pygame.display.set_icon(pygame.image.load("snake.jpg")) #changing the icon


    def exit(self):
        pygame.quit()


Snake = App()