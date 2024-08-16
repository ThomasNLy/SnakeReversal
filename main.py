import random
import pygame
from LinkedList import LinkedList
from Stack import Stack
from GameObject import GameObject
from SnakeObject import SnakeObject

pygame.init()
pygame.font.init()

#----------COLOURS------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
frame_rate = 30

running = True

snake_head_img = "images/snakehead.png"
snake_body_img = "images/snakebody.png"
apple_img = "images/apple.png"


snake_speed = 15 # spacing between snake body parts
SNAKE_SIZE = 30
global snakeList
snake_list = LinkedList()
snake_list.append(SnakeObject(200, 200, snake_head_img, SNAKE_SIZE, SNAKE_SIZE))
snake_list.append_to_front(SnakeObject(snake_list.head.value.prev_x, snake_list.head.value.prev_y, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))

global snake_head
snake_head = snake_list.tail.value


global apple
apple = GameObject(random.randint(0,1280), random.randint(0, 720), apple_img, 25, 25)
global apple_can_pickup
apple_can_pickup = True
global points
points = 0

#-----------time travel code--------------
TIME_TRAVEL_LIMIT = 5
global previous_locations
previous_locations = Stack()
global num_locs_recorded
num_locs_recorded = 0
global record_loc_timer
record_loc_timer = 0
global previous_points
previous_points = Stack()
global previous_apple_loc
previous_apple_loc = Stack()

global using_stop_time
using_stop_time = False

font = pygame.font.get_default_font()
font = pygame.font.Font(font, 18)

def record_previous_locations_and_points():
    global previous_locations, num_locs_recorded, snake_list, record_loc_timer
    global previous_points, previous_apple_loc
    delta_time = clock.tick(frame_rate)
    record_loc_timer += delta_time
    if record_loc_timer > 2000:
        print("recroding")
        record_loc_timer = 0
        if num_locs_recorded < TIME_TRAVEL_LIMIT:
            num_locs_recorded+=1
            temp = snake_list.head
            temp_list_coords = []
            while temp.has_next():
                coords = {
                    "x":temp.value.x,
                    "y": temp.value.y
                }
                temp_list_coords.append(coords)
                temp = temp.next
            # need to add in the tail as the while loop stops before the tail
            coords = {
                "x": snake_list.tail.value.x,
                "y": snake_list.tail.value.y
            }
            temp_list_coords.append(coords)
            previous_locations.add(temp_list_coords)
            #------------------------------
            

            previous_points.add(points)
            apple_coords = {
                "x": apple.x,
                "y": apple.y
            }
            previous_apple_loc.add(apple_coords)
            
        else:
            temp_prev_snake_loc_stack = Stack()
            temp_points_stack = Stack()
            temp_apple_coords_stack = Stack()
            for i in range(TIME_TRAVEL_LIMIT - 1):
                temp_prev_snake_loc_stack.add(previous_locations.pop())
                temp_points_stack.add(previous_points.pop())
                temp_apple_coords_stack.add(previous_apple_loc.pop())
            previous_locations = temp_prev_snake_loc_stack
            previous_points = temp_points_stack
            previous_apple_loc = temp_apple_coords_stack


            
            num_locs_recorded = 0
        
def reverse_time():
    global previous_locations, snake_list, using_stop_time
    global previous_points, points
    using_stop_time = True
    temp = snake_list.head
    if previous_locations.size() !=0:
        last_loc = previous_locations.pop()
        if(last_loc != 0):
            for i in range(len(last_loc)-1):
                temp.value.x = last_loc[i]["x"]
                temp.value.y = last_loc[i]["y"]
            snake_list.tail.value.x = last_loc[-1]["x"]
            snake_list.tail.value.y = last_loc[-1]["y"]
            # snake_list.tail.value.xspeed = 0
            # snake_list.tail.value.yspeed = 0

    if previous_points.size() !=0:
        points = previous_points.pop()
    using_stop_time = False

  
    if previous_apple_loc.size() != 0:
        previous_coords = previous_apple_loc.pop()
        if previous_coords != 0:
            apple.x = previous_coords["x"]
            apple.y = previous_coords["y"]
            apple.update_hit_box_loc()

            

def screen_wrap(gameObject: GameObject):
    if gameObject.x > 1280:
        gameObject.x = 0
    if gameObject.x < 0:
        gameObject.x = 1280
    if gameObject.y > 720:
        gameObject.y = 0
    elif gameObject.y < 0:
        gameObject.y = 720

def move_display_snake():
    global snake_head, points


    snake_head.move()
    snake_head.display(screen)
    screen_wrap(snake_head)
    record_previous_locations_and_points()
    

    temp = snake_list.head
    while temp.has_next():

        temp.value.display(screen)
        temp.value.move_to_new_spot(temp.next.value.prev_x, temp.next.value.prev_y)
        temp.value.image_direction(snake_head.xspeed, snake_head.yspeed)
        temp.value.update_hit_box_loc()

        if temp.next != snake_list.tail and snake_head.collision(temp.value) and using_stop_time == False:
            points -= 5
            for i in range(3):
                snake_list.remove_first_object()



        temp = temp.next
#used to control the gameplay/things that render on the screen
def gameplay():
    global snake_head, apple_can_pickup, snake_list, points
   
    move_display_snake()

    apple.display(screen)
    if snake_head.collision(apple) and apple_can_pickup:
        apple_can_pickup = False
        apple.x = random.randint(0, 1280)
        apple.y = random.randint(0,720)
        apple.update_hit_box_loc()
        apple_can_pickup = True
        snake_list.append_to_front(SnakeObject(snake_list.head.value.prev_x, snake_list.head.value.prev_y, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
        points += 1

def UI():
    points_text = pygame.font.Font.render(font, f"Points: {points}", True, WHITE)
    screen.blit(points_text, (80, 50))





while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                snake_list.append_to_front(SnakeObject(200, 200, snake_body_img, 30, 30))
            if event.key == pygame.K_a and snake_head.xspeed <= 0:
                snake_head.image_direction(-1, 0)

                snake_head.xspeed = -snake_speed
                snake_head.yspeed = 0
            elif event.key == pygame.K_d and snake_head.xspeed >= 0:
                snake_head.image_direction(1, 0)

                snake_head.xspeed = snake_speed
                snake_head.yspeed = 0
            elif event.key == pygame.K_w and snake_head.yspeed <= 0:
                snake_head.image_direction(0, -1)

                snake_head.yspeed = -snake_speed
                snake_head.xspeed = 0
            elif event.key == pygame.K_s and snake_head.yspeed >= 0:
                snake_head.image_direction(0, 1)

                snake_head.yspeed = snake_speed
                snake_head.xspeed = 0
            if event.key == pygame.K_SPACE:
                
                if previous_locations.size() != 0: 
                    reverse_time()
                 
                    # snake_head.x = snake_list.tail.value.x
                    # snake_head.y = snake_list.tail.value.y
                    # print(snake_list.tail.value.x)
                print("works")




    screen.fill(BLACK)
    gameplay()
    UI()
    pygame.display.flip()
    clock.tick(frame_rate)


pygame.quit()



