import pygame
import sys
import random

# Initialize Pygame and set up the main display surface
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Pygame from Santosh! ^_^")

# Load background music and start playing it in a loop
bg_music = pygame.mixer.Sound('NarutoRunnerPygame-main/audio/music.wav')
bg_music.play(loops=-1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and scale images for player walking animation
        walk_image1 = pygame.image.load('NarutoRunnerPygame-main/graphics/NR3.png').convert_alpha()
        walk_image1 = pygame.transform.rotozoom(walk_image1, 0, 0.75)
        walk_image2 = pygame.image.load('NarutoRunnerPygame-main/graphics/NR2.png').convert_alpha()
        walk_image2 = pygame.transform.rotozoom(walk_image2, 0, 0.75)
        
        # Create a list of walking images
        self.walk_images = [walk_image1, walk_image2]
        
        # Load and scale the image for jumping
        self.jump_image = pygame.image.load('NarutoRunnerPygame-main/graphics/NR4.png').convert_alpha()
        self.jump_image = pygame.transform.rotozoom(self.jump_image, 0, 0.75)

        self.animation_index = 0
        self.image = self.walk_images[0]
        self.rect = self.image.get_rect(midbottom=(200, 300))
        self.gravity = 0

        # Load and set the volume for the jump sound
        self.jump_sound = pygame.mixer.Sound('NarutoRunnerPygame-main/audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def update_animation(self):
        # Change the player's image based on whether they are jumping or walking
        if self.rect.bottom < 300:
            self.image = self.jump_image
        else:
            self.animation_index += 0.1
            if self.animation_index >= len(self.walk_images):
                self.animation_index = 0
            self.image = self.walk_images[int(self.animation_index)]

    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # Check if the space key is pressed for jumping
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20
        
        # Check if the mouse is clicked while over the player to jump
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.rect.bottom == 300:
                self.jump_sound.play()
                self.gravity = -20

    def apply_gravity(self):
        # Update gravity and move the player
        self.gravity += 1
        self.rect.y += self.gravity
        
        # Ensure the player doesn't fall below the ground level
        if self.rect.bottom > 300:
            self.rect.bottom = 300

    def update(self):
        # Update player's state including animation, input handling, and gravity
        self.handle_input()
        self.apply_gravity()
        self.update_animation()

# Create a group to manage the player sprite
player = pygame.sprite.GroupSingle()
player.add(Player())

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            # Load images for flying obstacles
            fly_image1 = pygame.image.load('NarutoRunnerPygame-main/graphics/shur.png').convert_alpha()
            fly_image2 = pygame.image.load('NarutoRunnerPygame-main/graphics/s2.png').convert_alpha()
            self.images = [fly_image1, fly_image2]
            self.y_pos = 200
        else:
            # Load images for snail obstacles
            snail_image1 = pygame.image.load('NarutoRunnerPygame-main/graphics/SL3.png').convert_alpha()
            snail_image1 = pygame.transform.rotozoom(snail_image1, 0, 0.75)
            snail_image2 = pygame.image.load('NarutoRunnerPygame-main/graphics/SL2.png').convert_alpha()
            snail_image2 = pygame.transform.rotozoom(snail_image2, 0, 0.75)
            self.images = [snail_image1, snail_image2]
            self.y_pos = 300
        
        self.animation_index = 0
        self.image = self.images[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1200), self.y_pos))

    def update_animation(self):
        # Cycle through obstacle images for animation
        self.animation_index += 0.1
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.image = self.images[int(self.animation_index)]
    
    def update(self):
        # Move the obstacle and remove it if it goes off-screen
        self.update_animation()
        self.rect.x -= 10
        self.check_off_screen()

    def check_off_screen(self):
        # Remove the obstacle if it is off the screen
        if self.rect.x <= -100:
            self.kill()

# Create a group to manage all obstacle sprites
obstacle_group = pygame.sprite.Group()

def display_score():
    # Calculate and display the current score based on elapsed time
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surface = score_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(800 / 2, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def check_player_collision(player_rect, obstacle_rects):
    # Check if the player has collided with any obstacles
    if obstacle_rects:
        for obstacle_rect in obstacle_rects:
            if player_rect.colliderect(obstacle_rect):
                return False
    return True

def check_sprite_collision():
    # Check if the player collides with any obstacles in the group
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        player.sprite.rect.bottom = 300
        return False
    return True

clock = pygame.time.Clock()
score_font = pygame.font.Font('NarutoRunnerPygame-main/font/Pixeltype.ttf', 50)

# Load and scale background and ground images
sky_surface = pygame.image.load('NarutoRunnerPygame-main/graphics/bg.png').convert()
sky_surface = pygame.transform.rotozoom(sky_surface, 0, 1.5)
ground_surface = pygame.image.load('NarutoRunnerPygame-main/graphics/ground.png').convert()

# Load and set up the introductory screen images
player_stand = pygame.image.load('NarutoRunnerPygame-main/graphics/NL1.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

intro_title_surface = score_font.render("Pixel Runner!", False, (64, 64, 64))
intro_title_rect = intro_title_surface.get_rect(center=(400, 50))

intro_instructions_surface = score_font.render("Press Space to Start!", False, (64, 64, 64))
intro_instructions_rect = intro_instructions_surface.get_rect(center=(400, 350))

player_gravity = 0
start_time = 0
game_active = False
score = 0

# Set a timer to create obstacles periodically
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['fly', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        # Clear the screen and draw all game elements
        screen.blit(sky_surface, (-100, 0))
        screen.blit(ground_surface, (0, 285))
        score = display_score()
        
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = check_sprite_collision()

    else:
        # Display the introductory screen
        screen.fill((94, 129, 162))
        screen.blit(intro_title_surface, intro_title_rect)
        screen.blit(player_stand, player_stand_rect)

        final_score_surface = score_font.render(f'Your Score: {score}', False, (64, 64, 64))
        final_score_rect = final_score_surface.get_rect(center=(400, 350))

        if score == 0:
            screen.blit(intro_instructions_surface, intro_instructions_rect)
        else:
            screen.blit(final_score_surface, final_score_rect)

    pygame.display.update()
    clock.tick(60)
