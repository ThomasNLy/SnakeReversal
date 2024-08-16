from LinkedList import LinkedList
from GameObject import GameObject
from SnakeObject import SnakeObject
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
frame_rate = 30

running = True

snake_head_img = "images/snakehead.png"

snake_body_img = "images/snakebody.png"
snake_speed = 15 # spacing between snake body parts
global snakeList
snake_list = LinkedList()
snake_list.append(SnakeObject(200, 200, snake_head_img, 30, 30))
snake_list.append_to_front(SnakeObject(200, 200, snake_body_img, 30, 30))

global snake_head
snake_head = snake_list.tail.value


#used to control the gameplay/things that render on the screen
def gameplay():
    global snake_head


    snake_head.move()


    snake_head.display(screen)

    temp = snake_list.head
    while temp.has_next():

        temp.value.display(screen)
        temp.value.move_to_new_spot(temp.next.value.prev_x, temp.next.value.prev_y)
        temp.value.image_direction(snake_head.xspeed, snake_head.yspeed)
        temp.value.update_hit_box_loc()

        if temp.next != snake_list.tail and snake_head.collision(temp.value):
            print(True)


        temp = temp.next








while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                snake_list.append_to_front(SnakeObject(200, 200, snake_body_img, 30, 30))
            if event.key == pygame.K_a:
                snake_head.image_direction(-1, 0)

                snake_head.xspeed = -snake_speed
                snake_head.yspeed = 0
            elif event.key == pygame.K_d:
                snake_head.image_direction(1, 0)

                snake_head.xspeed = snake_speed
                snake_head.yspeed = 0
            elif event.key == pygame.K_w:
                snake_head.image_direction(0, -1)

                snake_head.yspeed = -snake_speed
                snake_head.xspeed = 0
            elif event.key == pygame.K_s:
                snake_head.image_direction(0, 1)

                snake_head.yspeed = snake_speed
                snake_head.xspeed = 0




    screen.fill("black")
    gameplay()
    pygame.display.flip()
    clock.tick(frame_rate)


pygame.quit()



