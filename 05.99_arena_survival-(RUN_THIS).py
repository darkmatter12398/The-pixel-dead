# Name: Rafat Kabir and Shaheed Headley
# Date: 11/13/2020
# Program: Arena Survival
# Description:  Welcome to arena survival. The objective of the game is to essentially survive as long as
#               long as you can. A horde of zombies will come after you. But worry not my fellow soldier, as you
#               are equipped with an automatic assault rifle. Click on the zombies to get rid of their health (you can
#               hold since it is automatic). The game ends once you die, so if you would like to play again, just run
#               the program again! Its a very fun tactical shooter for very chill purposes, such as if you want
#               to take a small break or if you just want to have some fun. Have fun!


# import all necessary libraries
import pygame
import time
import math
import random
import os
import sys

# Initialize pygame function
pygame.init()


# display measurements of the window (pixel by pixel)
screen = pygame.display.set_mode((1100,800))

# Title and icon setup
pygame.display.set_caption("Arena Survival - Rafat and Shaheed")

icon = pygame.image.load('pixelGun.png')
pygame.display.set_icon(icon)

# Load in background image
# Transform the background image and scale it to fit the size of the window
backgroundImg = pygame.image.load('grass_better.png')
backgroundImg = pygame.transform.scale(backgroundImg, (800, 800))
backgroundX = 0
backgroundY = 0

# Load in crosshair image (for shooting and aiming)
crosshairImg = pygame.image.load('Crosshair.png')

# Load in title screen + tutorial images image and scale it to fit the size of the window
titleImg = pygame.image.load('Game_Title.png')
titleImg = pygame.transform.scale(titleImg, (1100, 800))

# Load in empty image
# Essentially, the purpose of this image is to make images that are supposed to be disappear, disappear.
# Especially zombies
emptyImg = pygame.image.load('empty.png')

# Loads in all heart images
# They are seperate variables, since they are deleted at certain times
# They are also scaled to fit their respective places on the UI panel
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

# Loads in panel image, and scales it up to screen size
# This displays the players statistics (e.g. their health)
panelImg = pygame.image.load('Panel.png')
panelImg = pygame.transform.scale(panelImg, (300, 800))

panelX = 800
panelY = 0

# Blood splatter
blood = []
bloodX = []
bloodY = []

# Loads in player image
# This is the player your play as.
# We initialize changes that might be needed for the x and y value
# Fire rate is the players speed at which they unload bullets
playerImg = pygame.image.load('muscle_guy_AR.png')
player_flash = pygame.image.load('muscle_guy_AR_flash.png')
playerX_change = 0
playerY_change = 0
fire_rate = 5

# Intitializes empty arrays for the enemy image and other statistics like the X and Y value.
# We use them as arrays since they will spawn in groups and need to be appended
enemyImg = []
enemyX = []
enemyY = []
placed = []
enemy_speed = []


# Initializes empty arrays for the ammo that will spawn at different intervals
# We use them as arrays since they will spawn in groups and need to be appended
ammoImg = []
ammoX = []
ammoY = []

# Array to store images in the image sequence
file_array = []

# Level and ammo message initialization
# This is the string that the panel will display for the players current ammo
current_mag = "30"
all_ammo = "90"
combined_ammo_message = current_mag +  "/" + all_ammo 

# Initialize function
def initialize():
    pygame.init()

    bruh = 0
    # Load in empty image
    # Essentially, the purpose of this image is to make images that are supposed to be disappear, disappear.
    # Especially zombies
    emptyImg = pygame.image.load('empty.png')

    # Loads in all heart images
    # They are seperate variables, since they are deleted at certain times
    # They are also scaled to fit their respective places on the UI panel
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

    # Loads in panel image, and scales it up to screen size
    # This displays the players statistics (e.g. their health)
    panelImg = pygame.image.load('Panel.png')
    panelImg = pygame.transform.scale(panelImg, (300, 800))

    panelX = 800
    panelY = 0

    # Blood splatter
    blood = []
    bloodX = []
    bloodY = []

    # Loads in player image
    # This is the player your play as.
    # We initialize changes that might be needed for the x and y value
    # Fire rate is the players speed at which they unload bullets
    playerImg = pygame.image.load('muscle_guy_AR.png')
    player_flash = pygame.image.load('muscle_guy_AR_flash.png')
    playerX_change = 0
    playerY_change = 0
    fire_rate = 5

    # Intitializes empty arrays for the enemy image and other statistics like the X and Y value.
    # We use them as arrays since they will spawn in groups and need to be appended
    enemyImg = []
    enemyX = []
    enemyY = []
    placed = []
    enemy_speed = []
    zombie_health = []


    # Initializes empty arrays for the ammo that will spawn at different intervals
    # We use them as arrays since they will spawn in groups and need to be appended
    ammoImg = []
    ammoX = []
    ammoY = []
    file_array = []

    # Level and ammo message initialization
    # This is the string that the panel will display for the players current ammo
    current_mag = "30"
    all_ammo = "90"
    combined_ammo_message = current_mag +  "/" + all_ammo

    # Identifiers
    level = "1"
    zombie_collide_time = 0
    
    player_damage = 1            

    max_ammo = 90
    all_ammo = "90"
    player_speed = 3

    current_mag = "30"

    stat = 0

    bullets_shot = 0 

    spawn_timer = 0 
    spawn_timer = 0
        
    zombie_health = []
    
    total_zombies = 0
    zombies = 0

    enemy_speed = []

    zombie_kill = 0

    exp = 25

    zombie_collide_time = 0

    blood_timer = 0
    max_exp = 0
    
    # Function for placing images in the displayed screen
    def place_image(image, x, y):
        screen.blit(image, (x, y))

    # Function for playing an image sequence
    def sequence(directory):
        del file_array[0:]

        # Uses the os library to add images to an array to be played in order later
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"): 
                file = (os.path.join(directory, filename))
                image = pygame.image.load(file)
                file_array.append(image)
        return file_array

    # Function takes in an image and rotates it on the screen using the rotate_center
    # function (also places it there too)
    def rotateImage(image, x, y, direction):
        screen.blit(rotate_center(image, direction), (x, y))    
        
    # Function calculates the distance between 2 objects, and returns that distance
    def collision(firstObject_X, firstObject_Y, secondObject_X, secondObject_Y):
        distance = math.sqrt(math.pow((firstObject_X - secondObject_X), 2) + \
                             math.pow((firstObject_Y - secondObject_Y), 2))

        return distance

    def enemy_evolution(total_zombies, enemy_health):
        if total_zombies % 3 == 0 and total_zombies != 0:
            enemy_health += 1

        return enemy_health


    # Function returns the new x and y coordinates of an enemy using their speed and direction
    # based on their target's destination distance(s)
    def enemy_move(x, y, direction, x_distance, y_distance, speed):
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

    def mouse_check(mouseX, mouseY):
        if mouseX <= 32:
            mouseX = 32
        if mouseX >= 768:
            mouseX = 768
        if mouseY <= 32:
            mouseY = 32
        if mouseY >= 768:
            mouseY = 768
            
        return mouseX, mouseY

    # Function returns the crosshair image
    # Makes it so that the clicks are in the center
    def cursor(x, y):
        if x < 800: 
            screen.blit(crosshairImg, (x - 17.5, y - 17.5))

    # Function returns the angle and distance to a given target based on an image's location
    def get_angle_distance(x, y, imageX, imageY):
        rel_x = x - imageX
        rel_y = y - imageY

        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        return angle, rel_x, rel_y

    # Function takes the image and finds its centre pixel then rotates around that point to make a rotation
    def rotate_center(image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    # Moves an image depending on its x and y coordinat
    # Usually used for player movement or enemy movement
    def move_image(x_change, y_change, x, y):
            x += x_change
            y += y_change

            if x <= 32:
                x = 32
            if x >= 736:
                x = 736
            if y <= 32:
                y = 32
            if y >= 736:
                y = 736
                
            return x, y

    # Function is resposible for creating messages depending on the paramters, such as the font and colour
    # It also places the this message in an x and y coordinate
    def message(msg, colour, x, y, size):
        font = pygame.font.SysFont(None, size)
        screen_text = font.render(msg, True, colour)
        place_image(screen_text, x, y)

    # Takes the text out of a file and returns the message inside of it
    def get_txt(filename):
        text_file = open (filename, "r")
        
        line_read = text_file.readline()

        while line_read != "":
            line_read = text_file.readline()
            print(line_read)

        text_file.close()

        
    # This is basically the game (you could also refer to it as "main()"
    def game():
        # Variable to control game state
        running = False

        #  These variables are to initialized variables that related to leveling
        level = "1"
        exp = 0
        zombie_kill = 0

        # Initialize the stat points of the player (use these to increase player power)
        stat = 0
        
        # Initalizes player speed
        player_speed = 3

        # Initializes player damage
        player_damage = 1
        
        # Initalizes shooting boolean and the amount of bullets shot
        # This is to calculate how much bullets the player has shot and what to do with it
        shooting = False
        bullets_shot = 0

        # Initialize max stuff
        max_exp = 50
        max_ammo = 90

        # Initializes health
        # Zombie health is an array, because zombie health is appended to each and every one of the
        # zombies
        health = 6
        enemy_health = 15

        zombie_health = []
        
        # Initializes timer variables
        timer = 0
        shoot_timer = 0
        spawn_timer = 0
        zombie_collide_time = 0
        blood_timer = []

        # Initializes the amount of zombies in the screen, and the amount of zombies that has spawned in
        # total
        zombies = 0
        total_zombies = 0
        
        # Initializes player X and Y coordinates
        # The X_change and Y_change variables are to detect if a key has been pressed to trigger player
        # movement
        playerX_change = 0
        playerY_change = 0
        playerX = 400
        playerY = 400

        # The FPS value defines a target frame rate for the game to run at
        # The clock is a variable to measure time in pygame relative to the frame rate
        FPS = 75
        clock = pygame.time.Clock()

        # Hides mouse from game
        pygame.mouse.set_visible(False)

        # Ammo drop and zombie spawn cooldowns
        ammo_spwn_time = random.randrange(FPS*12, FPS*20)
        zombie_spwn_time = FPS*0.6

        # Calculation for player fire rate
        player_fire_rate = FPS/fire_rate

        # End of game booleans
        game_over = False
        has_played = False
        controls_put = False

        #Starts game (at the intro screen)
        game = True
        while game:            
            # Scene for the main menu part of the game.
            # Basically an infinite loop to keep the sprites and images present in the screen
            # Tutorial images are put in a sequence
            # Tutorial index is equal to 0
            intro = True
            tutorials = sequence("Tutorial")
            tutorial = 0
            start = False

            # While the game is running the introduction
            while intro:
                if start == False:
                    # Places main menu image on the screen
                    place_image(titleImg, 0, 0)
                    start = True

                # Update the image of the game constantly
                pygame.display.update()
                # Loops through all events that are happening (e.g. what keys are pressed)
                for event in pygame.event.get():

                    # Keydown is for when a key is pressed
                    if event.type == pygame.KEYDOWN:

                        # If the player presses space, the next tutorial image will be put
                        # if the player presses space on the last tutorial image, start the game
                        if event.key == pygame.K_SPACE:
                            if tutorial == 4:
                                intro = False
                                running = True
                            else:    
                                image = tutorials[tutorial]
                                image = pygame.transform.scale(image, (1100, 800))
                                place_image(image, 0, 0)
                                pygame.display.update()

                            tutorial += 1

                            
            # This is the actual game scene. The arena survival game. 
            while running:

                if timer == 0:
                    # Load in empty image
                    # Essentially, the purpose of this image is to make images that are supposed to be disappear, disappear.
                    # Especially zombies
                    emptyImg = pygame.image.load('empty.png')

                    # Loads in all heart images
                    # They are seperate variables, since they are deleted at certain times
                    # They are also scaled to fit their respective places on the UI panel
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

                    # Loads in panel image, and scales it up to screen size
                    # This displays the players statistics (e.g. their health)
                    panelImg = pygame.image.load('Panel.png')
                    panelImg = pygame.transform.scale(panelImg, (300, 800))

                    panelX = 800
                    panelY = 0

                    # Blood splatter
                    blood = []
                    bloodX = []
                    bloodY = []

                    # Loads in player image
                    # This is the player your play as.
                    # We initialize changes that might be needed for the x and y value
                    # Fire rate is the players speed at which they unload bullets
                    playerImg = pygame.image.load('muscle_guy_AR.png')
                    player_flash = pygame.image.load('muscle_guy_AR_flash.png')
                    playerX_change = 0
                    playerY_change = 0

                    # Intitializes empty arrays for the enemy image and other statistics like the X and Y value.
                    # We use them as arrays since they will spawn in groups and need to be appended
                    enemyImg = []
                    enemyX = []
                    enemyY = []
                    placed = []
                    enemy_speed = []
                    zombie_health = []


                    # Initializes empty arrays for the ammo that will spawn at different intervals
                    # We use them as arrays since they will spawn in groups and need to be appended
                    ammoImg = []
                    ammoX = []
                    ammoY = []
                    file_array = []

                    # Level and ammo message initialization
                    # This is the string that the panel will display for the players current ammo
                    current_mag = "30"
                    all_ammo = "90"
                    combined_ammo_message = current_mag +  "/" + all_ammo

                    # Identifiers
                    level = "1"
                    zombie_collide_time = 0
                    
                    player_damage = 1
                                
                    max_ammo = 90
                    player_speed = 3

                    stat = 0

                    bullets_shot = 0 

                    spawn_timer = 7
                    zombie_spwn_time = 45
                    spawn_timer = 7
                        
                    zombie_health = []
                    
                    total_zombies = 0
                    zombies = 0

                    enemy_speed = []

                    zombie_kill = 0

                    exp = 25

                    zombie_collide_time = 0

                    blood_timer = []
                    max_exp = 50
                    
                # Timer variable measures the amount of iterations the while loop has gone through
                timer += 1

                # Uses the clock variable to store and execute frame rate intervals
                clock.tick(FPS)

                # Places  background image
                place_image(backgroundImg, backgroundX, backgroundY)

                # Places panels at the side, to show the statistics and such
                place_image(panelImg, panelX, panelY)

                # Top bar of the panel will display the level of the player
                # This message handles that
                message("Level", (255, 255, 255), 880, 50, 60)
                message(level, (255, 0, 0), 1000, 50, 60)
                
                # Second bar of the panel will display the level of the player
                # if the iteration at which zombile_collide_time is a certain number, the program will show the
                # appropriate hearts or amount of hearts
                if zombie_collide_time <= 50:
                    place_image(heart_right_3, 984, 170)
                if zombie_collide_time <= 100:
                    place_image(heart_left_3, 984, 170)
                if zombie_collide_time <= 150:
                    place_image(heart_right_2, 887, 170)
                if zombie_collide_time <= 200:
                    place_image(heart_left_2, 887, 170)
                if zombie_collide_time <= 250:
                    place_image(heart_right_1,790, 170)
                if zombie_collide_time <= 300:
                    place_image(heart_left_1,790, 170)

                # Third bar displays the amount of ammo the player has
                # We will reference the actual numbers later, since we have hard coded what the message will
                # will contain and because of that, the message has been coded later in this loop
                message("Ammo", (255, 255, 255), 915, 370, 30)

                # Fourth panel handles all the upgrades necessary
                message("Upgrades", (0, 255, 0), 900, 590, 30)

                # Player damage label
                player_damage = str(player_damage)
                message("Damage" + ": " + player_damage, (255, 0, 0), 815, 640, 35)
                player_damage = int(player_damage)

                # Player ammo label
                max_ammo = str(max_ammo) 
                message("Ammo" + ": " + max_ammo, (0, 255, 0), 960, 640, 35)
                max_ammo = int(max_ammo)

                # Player speed label
                player_speed = str(player_speed)
                message("Speed" + ": " + player_speed, (0, 0, 255), 815, 710, 35)
                player_speed = int(player_speed)

                # We will use the pygame.mouse.get_pos() function to get the positition of where the cursor
                # is at
                # And then use the cursor funtion to place a crosshair to where the cursor should be
                # We can also manipulate what happens when we click something, since we have X and Y
                # coordinates
                mousePos = pygame.mouse.get_pos()
                mousePos = mouse_check(mousePos[0], mousePos[1])
                cursor(mousePos[0], mousePos[1])

                # Ammo sprites will spawn randomly around the map between a certain time interval
                # (usually like 4-8 seconds)
                # When it is appropriate, the empty ammo arrays will append values, such as the image
                # Ammo
                if timer % 525 == 0:
                    
                    ammoImg.append(pygame.image.load('Ammo.png'))
                    ammoX.append(random.randrange(32, 735))
                    ammoY.append(random.randrange(32, 735))

                # It will loop through these arrays, and place all ammo sprites in the map according to their
                # appended values
                # Each ammo will disappear if they collide with the player
                # Ammo is increased by 20
                for i in range(len(ammoImg)):
                    # Globalize ammo because we need ammo on outer scopes of the code
                    place_image(ammoImg[i] ,ammoX[i], ammoY[i])

                    if collision(ammoX[i], ammoY[i], playerX, playerY) <= 28:
                        all_ammo = int(all_ammo)
                        ammoImg[i] = emptyImg
                        ammoX[i] = 0
                        ammoY[i] = 0

                        all_ammo += 20

                        if all_ammo > max_ammo:
                            all_ammo = max_ammo

                        all_ammo = str(all_ammo)

                # Loops through all events that happen in the game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.display.quit()
                        return

                    # We will only display a cursor when it inside the game. NOT at the panels
                    if mousePos[0] < 800:
                        
                        # if the mouse is clicked, we will only allow for shooting if the current mag has more than
                        # 0 bullets
                        # If else, no shooting is allowed
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            
                            current_mag = int(current_mag)
                            
                            if current_mag == 0:
                                shooting = False

                            if current_mag > 0:
                                shooting = True

                            current_mag = str(current_mag)

                        # Shooting is not allowed when mouse button is released
                        if event.type == pygame.MOUSEBUTTONUP:
                            shooting = False

                        # When a key is pressed down
                        if event.type == pygame.KEYDOWN:

                            # These are WASD controls. They affect the players x and y coordinates
                            # If you a, the player moves left, if you press w, the player moves up, etc
                            # Coordinate change variables are added to the coordinates to change movement
                            # These coordinate change variables are affected depending on what the speed or number
                            # is
                            if event.key == pygame.K_a:
                                playerX_change = -player_speed
                            if event.key == pygame.K_d:
                                playerX_change = player_speed
                            if event.key == pygame.K_w:
                                playerY_change = -player_speed
                            if event.key == pygame.K_s:
                                playerY_change = player_speed

                        # When the key is released
                        if event.type == pygame.KEYUP:

                            # If movement keys are released
                            # Coordinate change variables are equal to 0, so no movement is allowed
                            if event.key == pygame.K_a or event.key == pygame.K_d:
                                playerX_change = 0
                            if event.key == pygame.K_w or event.key == pygame.K_s:
                                playerY_change = 0

                            # If key 1 is released
                            # Player speed is going to be upgraded
                            # That is if the player has stat points
                            # This goes with key 2 for more ammo, and key 3 for more speed
                            if event.key == pygame.K_1:
                                stat -= 1

                                if stat < 0:
                                    stat = 0

                                else:
                                    player_damage += 1
                            if event.key == pygame.K_2:
                                stat -= 1

                                if stat < 0:
                                    stat = 0

                                else:
                                    all_ammo = int(all_ammo)
                                    max_ammo += 10
                                    all_ammo = max_ammo
                                    all_ammo = str(all_ammo)

                            if event.key == pygame.K_3:
                                stat -= 1

                                if stat < 0:
                                    stat = 0

                                else:
                                    player_speed += 1

                            if event.key == pygame.K_l:
                                timer = 0
                                running = False
                                intro = True

                            # Key r is pressed to reload
                            # Cannot reload if there is no more ammo left in "all_ammo" variable
                            if event.key == pygame.K_r: 
                                int_current_mag = int(current_mag)
                                all_ammo = int(all_ammo)

                                ammo_remainder = 30 - int_current_mag 
                                
                                if all_ammo < ammo_remainder:
                                    ammo_remainder = all_ammo
                                    
                                all_ammo -= ammo_remainder
                                
                                int_current_mag += ammo_remainder
                                
                                if all_ammo < 0:
                                    all_ammo = 0

                                if int_current_mag > 30:
                                    int_current_mag = 30

                                bullets_shot = 0
                                
                                all_ammo = str(all_ammo)
                                current_mag = str(int_current_mag)

                # Message for ammo numbers
                # Use a variable to manipulate ammo message
                combined_ammo_message = current_mag + "/" + all_ammo
                message(combined_ammo_message, (0, 255, 0), 900, 440, 55)

                # Position of the player keeps updating.
                # Uses "move_image" function to update player position
                playerPos = move_image(playerX_change, playerY_change, playerX, playerY)

                # X coordinate of player and Y coordinate of player
                playerX = playerPos[0]
                playerY = playerPos[1]

                # Zombies
                # If a certain amount of time passes, we will append various array that involve zombies
                if spawn_timer % zombie_spwn_time == 0 and spawn_timer != 0:

                    enemyImg.append(pygame.image.load('zombie_model.png'))
                    enemyX.append(random.randrange(32, 735))
                    enemyY.append(random.randrange(32, 735))
                    enemy_speed.append(1)
                    enemy_health = enemy_evolution(total_zombies, enemy_health)
                    zombie_health.append(enemy_health)
                    placed.append(False)
                    blood.append(pygame.image.load('blood.png'))
                    blood_timer.append(0)
                    bloodX.append(0)
                    bloodY.append(0)
                    total_zombies += 1
                    zombies += 1
                   
                    spawn_timer = 0

                # For as many times as a zombie has spawned
                for i in range(total_zombies):

                    #If the enemy hasn't been placed at its spawn point, then do that
                    if placed[i] == False:
                        place_image(enemyImg[i] ,enemyX[i], enemyY[i])
                        placed[i] = True

                    # Apply normal pathfinding route and movement towards player, if already spawned    
                    else:
                        # Gets a direction, distance, movement value and updated position using the player as a destination target
                        enemy_direction = int(get_angle_distance(playerX, playerY, enemyX[i], enemyY[i])[0] - 90)
                        
                        x_distance = int(get_angle_distance(playerX, playerY, enemyX[i], enemyY[i])[1])
                        y_distance = int(get_angle_distance(playerX, playerY, enemyX[i], enemyY[i])[2])
                        
                        enemy_x_change = int(enemy_move(enemyX[i], enemyY[i], enemy_direction, x_distance, y_distance, enemy_speed[i])[0])
                        enemy_y_change = int(enemy_move(enemyX[i], enemyY[i], enemy_direction, x_distance, y_distance, enemy_speed[i])[1])
                        
                        enemy_pos = move_image(enemy_x_change, enemy_y_change, enemyX[i], enemyY[i])

                        enemyX[i] = enemy_pos[0]
                        enemyY[i]  = enemy_pos[1]

                        # If the player is shooting (timer variable involved for fire rate effect)
                        if shooting == True and timer % 1 == 0:
                            # If the mouse position is at any of the zombies, the zombies will lose health (depending on how much damage the player does)
                            # If the zombies reach 0 health, the zombies will disappear, and will be considered "dead".
                            # We will also increment values to calculate different things
                            # Zombies variable will decrease
                            # Zombie kill variable will increase
                            # And experience will increase by 25
                            # The zombies position before they die will also be recorded and appended to the blood x and y arrays
                            if mousePos[0] > (enemyX[i] ) and mousePos[0] < (enemyX[i] + 32):
                                if mousePos[1] > (enemyY[i]) and mousePos[1] < (enemyY[i] + 32):
                                    zombie_health[i] -= player_damage
                                    if zombie_health[i] <= 0:
                                        bloodX[i] = enemyX[i]
                                        bloodY[i] = enemyY[i]
                                        bloodY.append(enemyY[i])
                                        zombie_health[i] = 0
                                        enemyImg[i] = emptyImg
                                        zombie_health[i] = 0
                                        enemyX[i] = 0
                                        enemyY[i] = 0
                                        enemy_speed[i] = 0
                                        
                                        zombies -= 1
                                        zombie_kill += 1
                                        exp += 25

                        # If collision occours between the player and the zombie
                        # The player will essentially lose health after a certain amount of time
                        # The player has 6 health. The player loses half a heart after every appropriately timed collision
                        if collision(playerX, playerY, enemyX[i], enemyY[i]) <= 20 and zombie_health[i] > 0:
                            zombie_collide_time += 1
                            if zombie_collide_time >= 50:
                                place_image(heart_right_3, 1200, 1200)
                            if zombie_collide_time >= 100:
                                place_image(heart_left_3, 1200, 1200)
                            if zombie_collide_time >= 150:
                                place_image(heart_right_2, 1200, 1200)
                            if zombie_collide_time >= 200:
                                place_image(heart_left_2, 1200, 1200)
                            if zombie_collide_time >= 250:
                                place_image(heart_right_1, 1200, 1200)
                            if zombie_collide_time >= 300:
                                place_image(heart_left_1, 1200, 1200)
                                running = False
                                game_over = True

                        # When the certain zombie has no health at all
                        # We will add a blood image to replace them
                        # This blood image will last as long as around 5 seconds
                        # Then it will disappear.
                        elif zombie_health[i] == 0:
                            if blood_timer[i] >= 150:
                                pass

                            else:
                                place_image(blood[i], bloodX[i], bloodY[i])
                                blood_timer[i] += 1

                        # If the zombie is not colliding with the player, we will create an image of the zombie
                        else:
                            rotateImage(enemyImg[i], enemyX[i], enemyY[i], enemy_direction)

                # If the experience gained from the player reaches max_experience, we will allow the player to level up
                # They will gain 1 stat point from each level, as well as the max experience needed to level up incrementing
                # by 50 when this if statement runs
                if exp % max_exp == 0 and exp != 0:
                    max_exp += 50
                    level = int(level)
                    level += 1
                    level = str(level)
                    exp = 0
                    stat += 1

                # Get the direction of the player, using the mouse location as a coordinate point to look towards
                player_direction = int(get_angle_distance(mousePos[0], mousePos[1], playerX, playerY)[0] - 90)

                # If the player is shooting, then we will decrement the amount of bullets in the current mag until it reaches 0
                # We will also keep in track of the amount of bullets shot
                if shooting == True and timer % 2 == 0:
                    current_mag = int(current_mag)
                    current_mag -= 1
                    bullets_shot += 1
                    
                    if current_mag < 0:
                        current_mag = 0
                        bullets_shot = 30
                        shooting = False

                    # This allows the player to rotate towards the crosshair, as well as place their image on the screen
                    rotateImage(player_flash, playerPos[0], playerPos[1], player_direction)

                    current_mag = str(current_mag)

                else:
                    # This allows the player to rotate towards the crosshair, as well as place their image on the screen
                    rotateImage(playerImg, playerPos[0], playerPos[1], player_direction)

                # Increments spawn timer
                spawn_timer += 1
                
                # Updates the entire screen to account for the location changes of zombies and the player
                pygame.display.flip()

                # When the game state has reached its end
                while game_over:

                    # Play the game over image sequence
                    if has_played == False:
                        for image in sequence("Game Over Screen"):
                            pygame.time.delay(50)
                            image = pygame.transform.scale(image, (1100, 800))
                            place_image(image, 0, 0)
                            pygame.display.update()
                        has_played = True

                        get_txt('goodbye.txt')

                    # Play the game over controls image sequence
                    if controls_put == False:
                        for image in sequence("Game Over Controls"):     
                            pygame.time.delay(50)
                            image = pygame.transform.scale(image, (500, 150))
                            place_image(image, 300, 650)
                            pygame.display.update()
                        controls_put = True
                        
                    for event in pygame.event.get():
                        # Keydown is for when a key is pressed
                        if event.type == pygame.KEYUP:
                            # If key is space, the game will start
                            if event.key == pygame.K_SPACE:
                                    running = False
                                    intro = True
                                    game_over = False
                                    initialize()

                            # Quits the game
                            if event.key == pygame.K_ESCAPE:
                                    pygame.display.quit()
                                    pygame.quit()
                                    running = False
                                    intro = False
                                    sys.exit()
                                    return
                                                                       
    # Starts the game loop
    game()

# Start the game
initialize()
