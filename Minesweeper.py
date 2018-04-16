from Buttons import Button
from Text import Text
import pygame
import random
import time

pygame.mixer.pre_init(22050,-16, 2, 1024)
pygame.init()

WIDTH = 400
HEIGHT = 400
SIZES = [200,400,600]

WHITE = (255,255,255)
GREY = (225,225,225)
GREY2 = (200,200,200)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255,165,0)
GREEN = (0,200,0)
DARK_GREEN = (0,200,0)
BLUE = (0,0,255)
YELLOW = (225,225,0)
TURQUOISE = (0,255,255)
PINK = (255,0,255)

DEV = 0

lost = []
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)

TITLE = pygame.font.SysFont("AgencyFB", 50)
TEXT = pygame.font.SysFont("AgencyFB", 25)
click = pygame.mixer.Sound("click.wav")
defeat = pygame.mixer.Sound("lost.wav")

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Minsweeper - JB 2018")
ICON = pygame.image.load('flag_sprite.png')
pygame.display.set_icon(ICON)

mine_numbers = {
    0: pygame.image.load("tile_sprite0.png").convert(),
    1: pygame.image.load("tile_sprite1.png").convert(),
    2: pygame.image.load("tile_sprite2.png").convert(),
    3: pygame.image.load("tile_sprite3.png").convert(),
    4: pygame.image.load("tile_sprite4.png").convert(),
    5: pygame.image.load("tile_sprite5.png").convert(),
    6: pygame.image.load("tile_sprite6.png").convert(),
    7: pygame.image.load("tile_sprite7.png").convert(),
    8: pygame.image.load("tile_sprite8.png").convert(),
    }
flag = pygame.image.load("flag_sprite.png").convert()
face = pygame.image.load("face_sprite.png").convert()
bar = pygame.image.load("bar.png").convert()
tiles = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    """Tile Class"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tile_sprite.png").convert()
        self.action = False
        self.flagged = False
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if DEV == 1:
            if self.state == 3:
                self.image = pygame.image.load("mine_sprite.png").convert()
        self.rect.center = (self.x, self.y)
        

    def clicked(self):
        if pygame.mouse.get_pressed()[0]:
            if self.state == 3:
                self.image = pygame.image.load("mine_sprite.png").convert()
                lost.append(1)
            else:
                nearby_mines = 0
                c_x = self.x
                c_y = self.y
                # N
                for tile in tiles:
                    if tile.rect.collidepoint(c_x,c_y-20):
                        if tile.state == 3:
                            nearby_mines += 1
                    # NE
                    if tile.rect.collidepoint(c_x+20,c_y-20):
                        if tile.state == 3:
                            nearby_mines += 1
                    # E
                    if tile.rect.collidepoint(c_x+20,c_y):
                        if tile.state == 3:
                            nearby_mines += 1
                    # SE
                    if tile.rect.collidepoint(c_x+20,c_y+20):
                        if tile.state == 3:
                            nearby_mines += 1
                    # S
                    if tile.rect.collidepoint(c_x,c_y+20):
                        if tile.state == 3:
                            nearby_mines += 1
                    # SW
                    if tile.rect.collidepoint(c_x-20,c_y+20):
                        if tile.state == 3:
                            nearby_mines += 1
                    # W
                    if tile.rect.collidepoint(c_x-20,c_y):
                        if tile.state == 3:
                            nearby_mines += 1
                    # NW
                    if tile.rect.collidepoint(c_x-20,c_y-20):
                        if tile.state == 3:
                            nearby_mines += 1
                            
                self.image = mine_numbers[nearby_mines]
                self.action = True

        elif pygame.mouse.get_pressed()[2]:
            if self.flagged == False:
                self.image = flag
                self.flagged = True
            else:
                self.image = pygame.image.load("tile_sprite.png").convert()
                self.flagged = False


def generate_grid(SIZE):
    display = pygame.display.set_mode((400,400))
    display.fill(GREY)
    title = Text(display,200,100,"Generating...",TITLE,BLACK)
    pygame.display.update()
    if SIZE == 200:
        RATIO = 6.4
    elif SIZE == 400:
        RATIO = 5
    else:
        RATIO = 3
    number_of_mines = int((SIZE/2)/RATIO)
    temp = []
    
    
    X_TIMES = int(SIZE/20)
    Y_TIMES = int(SIZE/20)
    x = 100
    y = 100
    for _ in range(Y_TIMES):
        for _ in range(X_TIMES):
            t = Tile(x,y)
            t.state = 0
            temp.append(t)
            x += 20
        legacy_x = x
        x = 100
        y += 20

    for _ in range(number_of_mines):
        tile = random.choice(temp)
        tile.state = 3

    for t in temp:
        tiles.add(t)
                    
    for t in tiles:
        if t.state != 3:
            nearby_mines = 0
            c_x = t.x
            c_y = t.y        
            for tile in tiles:
                if tile.rect.collidepoint(c_x,c_y-20):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x+20,c_y-20):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x+20,c_y):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x+20,c_y+20):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x,c_y+20):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x-20,c_y+20):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x-20,c_y):
                    if tile.state == 3:
                        nearby_mines += 1
                if tile.rect.collidepoint(c_x-20,c_y-20):
                    if tile.state == 3:
                        nearby_mines += 1

            if nearby_mines == 0:
                tiles.remove(t)

    display = pygame.display.set_mode((legacy_x+100,y+100))

def lose():
    clear()
    menu()

def win(score):
    clear()
    display = pygame.display.set_mode((400,400))
    display.fill(GREY)
    menu_button = Button(display,150,200,75,50,"Menu",TEXT,BLACK,GREY2)
    score_text = Text(display,200,125,"Score: "+str(score),TITLE,BLACK)
    title = Text(display,200,50,"Victory!",TITLE,BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.clicked():
                    channel1.play(click)
                    menu()

        pygame.display.update()


def clear():
    for tile in tiles:
        tiles.remove(tile)
    for item in lost:
        lost.remove(item)
    
def play(difficulty):
    clock = 0
    generate_grid(SIZES[difficulty])
    menu_button = Button(display,0,0,100,0,"Menu",TEXT,BLACK,GREY2)
    time_text = Text(display,101,0,"Your Time: "+str(clock),TEXT,BLACK)
    org_time = time.time()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.clicked():
                    channel1.play(click)
                    lose()
                pos = pygame.mouse.get_pos()
                for tile in tiles:
                    if tile.rect.collidepoint(pos):
                        channel1.play(click)
                        tile.clicked()

        won = True
        for tile in tiles:
            if tile.state != 3 and tile.action == False:
                won = False
        if won == True:
            score = 0
            for _ in tiles:
                score += 1
            score  = (score*2) - clock
            win(score)
        
        display.fill(GREY)
        tiles.update()
        tiles.draw(display)

        # blit here
        display.blit(bar, (0,0))
        menu_button = Button(display,0,0,100,25,"Menu",TEXT,BLACK,GREY2)
        time_text = Text(display,160,12,"Your Time: "+str(clock),TEXT,BLACK)
        
        if len(lost) != 0:
            display.fill(GREY)
            tiles.update()
            tiles.draw(display)
            pygame.display.flip()
            channel2.play(defeat)
            time.sleep(1)
            lose()

        if (time.time() - org_time) > 1:
            clock += 1
            org_time = time.time()
        
        pygame.display.flip()

def menu():
    display = pygame.display.set_mode((WIDTH,HEIGHT))
    display.fill(GREY)
    display.blit(face, (180,150))
    title_text = "Minesweeper"
    title = Text(display,int(WIDTH/2),int((HEIGHT/2))-100,title_text,TITLE,(0,0,0))
    quit_button = Button(display,int(WIDTH/2)-50,300,100,50,"QUIT",TITLE,RED,BLACK)

    easy = Button(display,60,200,75,50,"Easy",TEXT,GREEN,BLACK)
    medium = Button(display,160,200,75,50,"Medium",TEXT,ORANGE,BLACK)
    hard = Button(display,260,200,75,50,"Hard",TEXT,RED,BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy.clicked():
                    channel1.play(click)
                    play(0)
                elif medium.clicked():
                    channel1.play(click)
                    play(1)
                elif hard.clicked():
                    channel1.play(click)
                    play(2)
                elif quit_button.clicked():
                    channel1.play(click)
                    pygame.quit()
                    quit()

        pygame.display.flip()

menu()

