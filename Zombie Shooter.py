import pygame
import time
import math
import random
import os

# global variables
global combined_ammo_message
global all_ammo

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1100,800))

# Title and Icon
pygame.display.set_caption("Arena Survival - Rafat and Shaheed")

icon = pygame.image.load('pixelGun.png')
pygame.display.set_icon(icon)

# Background
backgroundImg = pygame.image.load('grass_better.png')
backgroundImg = pygame.transform.scale(backgroundImg, (800, 800))

# Crosshair
crosshairImg = pygame.image.load('Crosshair.png')

# Title Screen
titleImg = pygame.image.load('Game Title.png')

# Empty
emptyImg = pygame.image.load('empty.png')

# Heart
heart_left_1 = pygame.image.load('heart_left.png')
heart_left_1 = pygame.transform.scale(heart_left_1, (128, 128))
heart_right_1 = pygame.image.load('heart_right.png')
heart_right_1 = pygame.transform.scale(heart_right_1, (128, 128))

heart_left_2 = pygame.image.load('heart_left.png')
heart_left_2 = pygame.transform.scale(heart_left_2, (128, 128))
heart_right_2 = pygame.image.load('heart_right.png')
heart_right_2 = pygame.transform.scale(heart_right_2, (128, 128))

heart_left_3 = pygame.image.load('heart_left.png')
heart_left_3 = pygame.transform.scale(heart_left_3, (128, 128))
heart_right_3 = pygame.image.load('heart_right.png')
heart_right_3 = pygame.transform.scale(heart_right_3, (128, 128))

# Panel
panelImg = pygame.image.load('Panel.png')
panelImg = pygame.transform.scale(panelImg, (300, 800))

# Player
playerImg = pygame.image.load('muscle_guy_AR.png')
playerFaceImg = pygame.image.load('Face.png')
playerX_change = 0
playerY_change = 0
fire_rate = 5

# Enemy
enemyImg = []
enemyX = []
enemyY = []
placed = []
enemy_speed = []

# Ammo
ammoImg = []
ammoX = []
ammoY = []

file_array = []

# Level and ammo message initialization
current_mag = "30"
all_ammo = "90"
combined_ammo_message = current_mag +  "/" + all_ammo 

def placeImage(image, x, y):
    screen.blit(image, (x, y))

def sequence(directory):
    del file_array[0:]
    
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"): 
            file = (os.path.join(directory, filename))
            image = pygame.image.load(file)
            file_array.append(image)

    return file_array
    
def rotateImage(image, x, y, direction):
    character = pygame.transform.rotate(image, direction)
    screen.blit(rotate_center(image, direction), (x, y))    

def collision(firstObject_X, firstObject_Y, secondObject_X, secondObject_Y):
    distance = math.sqrt(math.pow((firstObject_X - secondObject_X), 2) + math.pow((firstObject_Y - secondObject_Y), 2))

    return distance

def enemyMovement(x, y, direction, x_distance, y_distance, speed):
    if x_distance < 0:
        x = -speed
    if x_distance > 0:
        x = speed
    if x_distance == 0:
        x = 0
        
    if y_distance < 0:
        y = -speed
    if y_distance > 0:
        y = speed
    if y_distance == 0:
        y = 0
        

    return x, y

def cursor(x, y):
    if x < 800:
        screen.blit(crosshairImg, (x - 17.5, y - 17.5))

def getVectorDirection(x, y, imageX, imageY):
    rel_x = x - imageX
    rel_y = y - imageY

    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    return angle, rel_x, rel_y

def rotate_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def move_image(x_change, y_change, x, y):
        x += x_change
        y += y_change

        if x <= 32:
            x = 32
        if x >= 735:
            x = 735
        if y <= 32:
            y = 32
        if y >= 735:
            y = 735
            
        return x, y

def message(msg, colour, x, y, size):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, colour)
    placeImage(screen_text, x, y)
        
def game():
    # speed
    player_speed = 3
    
    # initialize ammo variables
    shooting = False
    bullets_shot = 0

    # initialize health
    health = 6
    zombie_health = []
    
    # Initialize time
    timer = 0
    shoot_timer = 0
    spawn_timer = 0

    zombies = 0
    total_zombies = 0
    bullet_speed = 7
    zombie_collide_time = 0
    wave = 0
    
    # Player picture
    playerX_change = 0
    playerY_change = 0
    
    playerX = 400
    playerY = 400

    #Settings
    FPS = 75
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    ammo_spwn_time = random.randrange(FPS*12, FPS*20)
    zombie_spwn_time = FPS*3

    player_fire_rate = FPS/fire_rate

    game_over = False
    has_played = False
    controls_played = True

    intro = True
    while intro:
        placeImage(titleImg, 0, 0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                intro = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        intro = False
                        running = True

        pygame.display.update()
        
    while running:
        pygame.time.delay(10)
        
        timer += 1
        clock.tick(FPS)
        
        backgroundX = 0
        backgroundY = 0
        placeImage(backgroundImg, backgroundX, backgroundY)

        panelX = 800
        panelY = 0
        placeImage(panelImg, panelX, panelY)

        # Level panel
        message("Level", (255, 255, 255), 880, 50, 60)
        message("1", (255, 0, 0), 1000, 50, 60)
        
        # Heart panel
        if zombie_collide_time <= 25:
            placeImage(heart_right_3, 984, 170)
        if zombie_collide_time <= 50:
            placeImage(heart_left_3, 984, 170)
        if zombie_collide_time <= 75:
            placeImage(heart_right_2, 887, 170)
        if zombie_collide_time <= 100:
            placeImage(heart_left_2, 887, 170)
        if zombie_collide_time <= 125:
            placeImage(heart_right_1,790, 170)
        if zombie_collide_time <= 150:
            placeImage(heart_left_1,790, 170)

        # Ammo panel
        message("Ammo", (255, 255, 255), 915, 370, 30)

        # Upgrade panel
        message("Upgrades", (0, 255, 0), 900, 590, 30)
        message("Damage", (255, 0, 0), 815, 640, 35)
        message("Fire Rate", (0, 255, 0), 980, 640, 35)
        message("Ammo", (0, 0, 255), 815, 710, 35)
        message("Accuracy", (0, 255, 255), 980, 710, 35)
        
        mousePos = pygame.mouse.get_pos()
        
        cursor(mousePos[0], mousePos[1])

        # Ammo
        if timer % 100 == 0:
            ammoImg.append(pygame.image.load('Ammo.png'))
            ammoX.append(random.randrange(32, 735))
            ammoY.append(random.randrange(32, 735))

        for i in range(len(ammoImg)):
            
            placeImage(ammoImg[i] ,ammoX[i], ammoY[i])
                                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                return
            if mousePos[0] < 800:
                # if mouse down
                if event.type == pygame.MOUSEBUTTONDOWN:
                    global current_mag
                    current_mag = int(current_mag)
                    
                    if current_mag == 0:
                        shooting = False

                    if current_mag > 0:
                        shooting = True

                    current_mag = str(current_mag)

                if event.type == pygame.MOUSEBUTTONUP:
                    shooting = False

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_a:
                        playerX_change = -player_speed
                    if event.key == pygame.K_d:
                        playerX_change = player_speed
                    if event.key == pygame.K_w:
                        playerY_change = -player_speed
                    if event.key == pygame.K_s:
                        playerY_change = player_speed

                if event.type == pygame.KEYUP:
                    global all_ammo
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        playerX_change = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        playerY_change = 0

                    if event.key == pygame.K_1:
                        player_speed += 0.2
                    if event.key == pygame.K_2:
                        all_ammo = int(all_ammo)
                        all_ammo += 5
                        all_ammo = str(all_ammo)

                    if event.key == pygame.K_r:
                        int_current_mag = int(current_mag)
                        all_ammo = int(all_ammo)

                        int_current_mag += all_ammo
                        all_ammo -= bullets_shot

                        if all_ammo  < 0:
                            all_ammo = 0

                        if int_current_mag > 30:
                            int_current_mag = 30

                        bullets_shot = 0
                        
                        all_ammo = str(all_ammo)
                        current_mag = str(int_current_mag)


        if shooting == True:
            current_mag = int(current_mag)

            current_mag -= 1
            bullets_shot += 1
            
            if current_mag < 0:
                current_mag = 0
                bullets_shot = 30
                shooting = False
                
            current_mag = str(current_mag)

        combined_ammo_message = current_mag + "/" + all_ammo
         
        message(combined_ammo_message, (0, 255, 0), 900, 440, 55)

        playerPos = move_image(playerX_change, playerY_change, playerX, playerY)

        playerX = playerPos[0]
        playerY = playerPos[1]

        # Zombies
        if spawn_timer % zombie_spwn_time == 0 and spawn_timer != 0 and zombies < 6:
            enemyImg.append(pygame.image.load('zombie_model.png'))
            enemyX.append(random.randrange(32, 735))
            enemyY.append(random.randrange(32, 735))
            enemy_speed.append(1)
            zombie_health.append(20)
            placed.append(False)
            total_zombies += 1
            zombies += 1
           
            spawn_timer = 0

        for i in range(zombies):
            
            if placed[i] == False:
                print(i)
                placeImage(enemyImg[i] ,enemyX[i], enemyY[i])
                placed[i] = True
                print("placed")
                
            else:
                enemy_direction = int(getVectorDirection(playerX, playerY, enemyX[i], enemyY[i])[0] - 90)

                x_distance = int(getVectorDirection(playerX, playerY, enemyX[i], enemyY[i])[1])
                y_distance = int(getVectorDirection(playerX, playerY, enemyX[i], enemyY[i])[2])
                
                enemy_x_change = int(enemyMovement(enemyX[i], enemyY[i], enemy_direction, x_distance, y_distance, enemy_speed[i])[0])
                enemy_y_change = int(enemyMovement(enemyX[i], enemyY[i], enemy_direction, x_distance, y_distance, enemy_speed[i])[1])
                
                enemyPos = move_image(enemy_x_change, enemy_y_change, enemyX[i], enemyY[i])

                enemyX[i] = enemyPos[0]
                enemyY[i]  = enemyPos[1]
                
                if total_zombies % 5 == 0:
                    wave += 1
                    enemy_speed[i] += 0.2

                if shooting == True:
                    if mousePos[0] > (enemyX[i] + 3) and mousePos[0] < (enemyX[i] + 30):
                        if mousePos[1] > (enemyX[i] + 2) and mousePos[1] < (enemyY[i] + 27):
                            zombie_health[i] -= 1
                            if zombie_health[i] == 0:
                                zombie_health[i] = 0
                                print("dead")
                                enemyImg[i] = emptyImg
                                zombie_health[i] = 0
                                enemyX[i] = 0
                                enemyY[i] = 0
                                enemy_speed[i] = 0
                                zombies -= 1

                    
                if collision(playerX, playerY, enemyX[i], enemyY[i]) <= 20 and zombie_health[i] > 0:
                    zombie_collide_time += 1

                    if wave <= 5:
                        if zombie_collide_time >= 25:
                            placeImage(heart_right_3, 1200, 1200)
                        if zombie_collide_time >= 50:
                            placeImage(heart_left_3, 1200, 1200)
                        if zombie_collide_time >= 75:
                            placeImage(heart_right_2, 1200, 1200)
                        if zombie_collide_time >= 100:
                            placeImage(heart_left_2, 1200, 1200)
                        if zombie_collide_time >= 125:
                            placeImage(heart_right_1, 1200, 1200)
                        if zombie_collide_time >= 150:
                            placeImage(heart_left_1, 1200, 1200)
                            running = False
                            game_over = True

                    else:
                        if zombie_collide_time >= 50:
                            placeImage(heart_right_3, 1200, 1200)
                            placeImage(heart_left_3, 1200, 1200)
                            placeImage(heart_right_2, 1200, 1200)
                        if zombie_collide_time >= 100:
                            placeImage(heart_right_2, 1200, 1200)
                            placeImage(heart_left_2, 1200, 1200)
                        if zombie_collide_time >= 150:
                            placeImage(heart_right_1, 1200, 1200)
                            placeImage(heart_left_1, 1200, 1200)
                            running = False
                            game_over = True
                        

                else:
                    rotateImage(enemyImg[i], enemyX[i], enemyY[i], enemy_direction)

        player_direction = int(getVectorDirection(mousePos[0], mousePos[1], playerX, playerY)[0] - 90)
        rotateImage(playerImg, playerPos[0], playerPos[1], player_direction)
        
        pygame.display.update()
        pygame.display.flip()

        timer += 1
        spawn_timer += 1

        
        while game_over:
            if has_played == False:
                for image in sequence("Game Over Screen"):
                    pygame.time.delay(50)
                    image = pygame.transform.scale(image, (1100, 800))
                    placeImage(image, 0, 0)
                    pygame.display.update()
                has_played = True
                pygame.time.delay(500)
                controls_played = False

            if controls_played == False:
                for image in sequence("Game Over Controls"):
                    pygame.time.delay(50)
                    image = pygame.transform.scale(image, (500, 150))
                    placeImage(image, 300, 650)
                    pygame.display.update()
                controls_played = True
                
                    
        
            pygame.draw.rect(screen, (0,0,0), [490, 590, 120, 47])
            message("Start over", (255,255,255), 500, 600, 40)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    intro = False
                    pygame.display.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mousePos[0] > 490 and mousePos[0] < 610:
                        if mousePos[1] > 590 and mousePos[1] < 637:
                            game_over = False
                            intro = True

            pygame.display.update()

game()
