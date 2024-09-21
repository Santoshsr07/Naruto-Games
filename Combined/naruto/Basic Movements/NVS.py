import pygame
pygame.init()
pygame.mixer.init()

win = pygame.display.set_mode((700,500))
pygame.display.set_caption("Naruto vs Sasuke")

walkRight = [pygame.image.load('naruto/Basic Movements/pics/NR2.png'), pygame.image.load('naruto/Basic Movements/pics/NR3.png'), pygame.image.load('naruto/Basic Movements/pics/NR4.png')]

walkLeft = [pygame.image.load('naruto/Basic Movements/pics\\NL2.png'), pygame.image.load('naruto/Basic Movements/pics\\NL3.png'), pygame.image.load('naruto/Basic Movements/pics\\NL4.png')]

shurikens = []
throwSpeed = 0

bg = pygame.image.load('naruto/Basic Movements/pics\\bg.png')
stan = pygame.image.load('naruto/Basic Movements/pics\\Nstanding.png')
j = pygame.image.load('naruto/Basic Movements/pics\\NR4.png')

Nh = pygame.image.load('naruto/Basic Movements/pics\\Nh.png')
Sh = pygame.image.load('naruto/Basic Movements/pics\\Sh.png')

try:
    hitSound = pygame.mixer.Sound('naruto/Basic Movements/pics\\hit.wav')
    pygame.mixer.music.play(-1)
    
except pygame.error as e:
    print(f"Error loading hit sound: {e}")
    
try:
    shurikenSound = pygame.mixer.Sound('naruto/Basic Movements/pics\\shuriken.wav')
    pygame.mixer.music.play(-1)
    
except pygame.error as e:
    print(f"Error loading shuriken sound: {e}")

Clock = pygame.time.Clock()

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 7
        self.isjump = False
        self.jumpheight = 10 
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 10, self.y + 5, 80, 80)
        self.health = 200
        
    def draw(self, win):
        
        if self.health > 0:
        
            if self.walkCount + 1 > 6:
                self.walkCount = 0
                
            if not (self.standing):
            
                if self.left and self.isjump == False:
                    win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
                    self.walkCount += 1
                    
                elif self.left and self.isjump:
                    win.blit(walkLeft[2], (self.x,self.y))
                
                elif self.right and self.isjump == False:
                    win.blit(walkRight[self.walkCount//2], (self.x,self.y))
                    self.walkCount += 1
                    
                elif self.right and self.isjump:
                    win.blit(walkRight[2], (self.x,self.y))
                    
            elif stan and self.isjump:
                win.blit(j, (self.x,self.y))
                    
            else:
                if self.left:
                    win.blit(pygame.image.load('naruto/Basic Movements/pics\\NL1.png'), (self.x, self.y))
                    
                else:
                    win.blit(pygame.image.load('naruto/Basic Movements/pics\\NR1.png'), (self.x, self.y))
                    
            self.hitbox = (self.x + 10, self.y + 5, 80, 80)
            Nbar2 = pygame.draw.rect(win, (255, 0, 0), (80, 45, 200, 20))
            health_width = max(0, min(self.health, 200))
            new_x = 80 + (200 - health_width)
            Nbar = pygame.draw.rect(win, (255, 255, 0), (new_x, 45, health_width, 20))

            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            
        else:
            win.blit(pygame.image.load('naruto/Basic Movements/pics\\Nd.png'), (self.x, self.y))
            text = font.render('Sasuke Wins', True, (255, 255, 255), (0, 0, 100))
            win.blit(text, (180, 200))
        
    def hit(self):
        if self.health > 0:
            self.health -= 3
        else:
            print("Sasuke Wins")
            
class weapons():
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (self.x, self.y, 40, 40)
        
    def draw(self, win):
        
        win.blit(pygame.image.load('naruto/Basic Movements/pics\\s2.png'), (self.x, self.y))
        shurikenSound.play()
        self.hitbox = (self.x, self.y, 40, 40)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        
class enemy():
    
    walkRightS = [pygame.image.load('naruto/Basic Movements/pics\\SR2.png'), pygame.image.load('naruto/Basic Movements/pics\\SR3.png'), pygame.image.load('naruto/Basic Movements/pics\\SR1.png')]

    walkLeftS = [pygame.image.load('naruto/Basic Movements/pics\\SL2.png'), pygame.image.load('naruto/Basic Movements/pics\\SL3.png'), pygame.image.load('naruto/Basic Movements/pics\\SL1.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.end, self.x]
        self.speed = 8
        self.walkCount = 0
        self.hitbox = (self.x + 10, self.y + 5, 80, 80)
        self.health = 200
        
    def draw(self, win):
        self.move()
        
        if sasuke.health > 0:
        
            if self.walkCount + 1 >= 6:
                self.walkCount = 0
                
            if self.speed > 0:
                win.blit(self.walkRightS[self.walkCount//2], (self.x, self.y))
                self.walkCount += 1
                
            else:
                win.blit(self.walkLeftS[self.walkCount//2], (self.x, self.y))
                self.walkCount += 1
            
            self.hitbox = (self.x + 10, self.y + 5, 80, 80)
            Sbar2 = pygame.draw.rect(win, (255, 0, 0), (410, 45, 200, 20))
            Sbar = pygame.draw.rect(win, (255, 255, 0), (410, 45, self.health, 20))
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            
        else:
            self.speed = 0
            text = font.render('Naruto Wins', True, (255, 100, 10), (0, 0, 100))
            win.blit(text, (180, 200))
            win.blit(pygame.image.load('naruto/Basic Movements/pics\\Sd.png'), (self.x, self.y))
        
    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            
            else:
                self.speed = self.speed * -1
                self.walkCount = 0
                
        else:
            if self.x + self.speed > self.path[0]:
                self.x += self.speed
                
            else:
                self.speed = self.speed * -1
                self.walkCount = 0
                
    def hit(self):
        if self.health > 0:
            self.health -= 10
            
        else:
            print("Sasuke Died")
    

run = True

def redrawgamewindow():
    win.blit(bg,(0,0))
    naruto.draw(win)
    sasuke.draw(win)
    win.blit(Nh, (10, 10))
    win.blit(Sh, (600, 10))
    for shuriken in shurikens:
        shuriken.draw(win)
    
    pygame.display.update()
    
font = pygame.font.SysFont('comicsans', 50, True)
    
naruto = player(20, 400, 100, 100)
sasuke = enemy(600, 400, 100, 100, 20)

while run:
    Clock.tick(25)
    
    if throwSpeed > 0:
        throwSpeed += 1
        
    if throwSpeed > 3:
        throwSpeed = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if naruto.health > 0 and sasuke.health > 0:
        if naruto.hitbox[1] < sasuke.hitbox[1] + sasuke.hitbox[3] and naruto.hitbox[1] + naruto.hitbox[3] > sasuke.hitbox[1]:
            if naruto.hitbox[0] + naruto.hitbox[2] > sasuke.hitbox[0] and naruto.hitbox[0] < sasuke.hitbox[0] + sasuke.hitbox[2]:
                naruto.hit()
                hitSound.play()
                
    else:
        if naruto.health == 0:
            naruto.speed = 0
            
    for shuriken in shurikens:
        
        if sasuke.health > 0:
        
            if shuriken.hitbox[1] + round(shuriken.hitbox[3]/2) > sasuke.hitbox[1] and shuriken.hitbox[1] + round   (shuriken.hitbox[3]/2) < sasuke.hitbox[1] + sasuke.hitbox[3]:
                if shuriken.hitbox[0] + shuriken.hitbox[2] > sasuke.hitbox[0] and shuriken.hitbox[0] + shuriken.hitbox[2] < sasuke.hitbox[0] + sasuke.hitbox[2]:
                    sasuke.hit()
                    hitSound.play()
                    shurikens.pop(shurikens.index(shuriken))
                    
        else:
            sasuke.speed = 0
            
        if shuriken.x < 700 and shuriken.x > 0:
            shuriken.x += shuriken.vel
            
        else:
            shurikens.pop(shurikens.index(shuriken))
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and throwSpeed == 0:
        if naruto.left == True:
            facing = -1
            
        else:
            facing = 1
            
        if len(shurikens) < 5:
            shurikens.append(weapons(round(naruto.x + naruto.width//2), round(naruto.y + 50//2), 40,40, facing))
            throwSpeed = 1
    
    if keys[pygame.K_LEFT] and naruto.x > naruto.speed:
        naruto.x -= naruto.speed
        naruto.left = True
        naruto.right = False
        naruto.standing = False
        
    elif keys[pygame.K_RIGHT] and naruto.x < 700 - naruto.width - naruto.speed:
        naruto.x += naruto.speed
        naruto.left = False
        naruto.right = True
        naruto.standing = False
    
    else:
        naruto.walkCount = 0
        naruto.standing = True
        
    if naruto.isjump == False:
        if keys[pygame.K_UP]:
            naruto.isjump = True
            naruto.left = False
            naruto.right = False
            naruto.walkCount = 0
            
    else:
        if naruto.jumpheight >= -10:
            neg = 1
            
            if naruto.jumpheight < 0:
                neg = -1
                
            naruto.y -= (naruto.jumpheight ** 2) * 0.5 * neg # type: ignore
            naruto.jumpheight -= 1
            
        else:
            naruto.isjump = False
            naruto.jumpheight = 10
    
    pygame.display.update()
    
    redrawgamewindow()
    
pygame.quit()