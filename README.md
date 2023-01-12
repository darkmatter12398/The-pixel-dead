# Description
"The pixel dead" is a round-based top-down 2D shooter, where you fight off hordes of zombies in a confined area. The player is equipped with an assault rifle, and has to infinitely fight off zombies

# How to use
1. Install [python](https://www.python.org/)
2. Install pygame by pasting this line into command prompt:
```bash
pip install pygame
```
3. Extract the files and folders from the repository
4. Run "the_pixel_dead.py"

# Functionality
## Main menu
The main menu is a background image representing the theme of the game.

![image](https://user-images.githubusercontent.com/77501024/211989521-4923899d-79a0-4d45-989f-c98d1b551016.png)

## Tutorial
To proceed through the tutorial, you need to press space bar while in the menu. This will allow you to treat the tutorial as a series of slides, and to proceed to each slide, you need to continuously press spacebar.

![image](https://user-images.githubusercontent.com/77501024/211989818-f5c50b9b-66c6-4d0e-b624-cdd48e6df9e2.png)

## Movement
The player can move around the map by using the WASD keys, as found in most traditional games.

## Player
The player is an entity equipped with an assault rifle. 

![image](https://user-images.githubusercontent.com/77501024/211990082-e4734a71-8183-479a-b28f-90beaa4df11a.png)

## Combat
To fire the gun, the player has to hold down left mouse click, and it will fire rounds of ammunition.

![image](https://user-images.githubusercontent.com/77501024/211990859-1ccb07bb-aaac-4bc2-9f47-4999aaa92881.png)

If you're crosshair is aiming at a zombie, it will damage the zombie as long as you have ammo, and are holding down left click.
Note: You can't fire at the path of the zombie; the crosshair has to be at the zombie's location for it to damage the zombie

![image](https://user-images.githubusercontent.com/77501024/211990899-470526bf-da4c-41d2-9841-07cf471edcce.png)

You'll know if a zombie has died if there is a blood splatter as shown in this picture:

![image](https://user-images.githubusercontent.com/77501024/211991035-7a840bca-43a7-44aa-82de-0eb8244aea18.png)

## Level
At the top right corner, you can see your current level. 

![image](https://user-images.githubusercontent.com/77501024/211991266-a475424c-31ba-44f9-9512-d6066d20575f.png)

You can increase your level by killing zombies. Once you leveled up, you can upgrade your damage (press 1), ammo (press 2), or speed (press 3)

![image](https://user-images.githubusercontent.com/77501024/211991924-38d9f090-2af3-48e8-bcbd-7bcfdf640523.png)

This is vital to surviving, as zombies progressively get more health and become harder to kill, so adapting to this change can allow you to stay alive longer.

## Game over
Below your level indicator is the amount of hearts you have left

![image](https://user-images.githubusercontent.com/77501024/211992233-15b55660-1d10-4366-8d1d-2cbadf3961b7.png)

If you come into contact of a zombie for long enough, they can tear down the hearts you have. If you lose all 3 hearts, then you end up losing the game

![image](https://user-images.githubusercontent.com/77501024/211992953-5899469f-9bed-4ea5-a168-1323343630a2.png)

## Replay
After you lose the game, the program resets everything so you can start fresh again. You just need to press space in order to go back to the start after you've lost.
