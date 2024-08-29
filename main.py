import random
import pygame
from DoublyLinkedList import DoublyLinkedList
from Stack import Stack
from GameObject import GameObject
from SnakeObject import SnakeObject

pygame.init()
pygame.font.init()

#----------COLOURS------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (201, 60, 60)



screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
frame_rate = 30

running = True

snake_head_img = "images/snakehead.png"
snake_body_img = "images/snakebody.png"
apple_img = "images/apple.png"
heart_img = "images/heart.png"


global snake_speed
snake_speed =  5# spacing between snake body parts
SNAKE_SIZE = 30
global snake_list
snake_list = DoublyLinkedList()
snake_list.append(SnakeObject(200, 200, snake_head_img, SNAKE_SIZE, SNAKE_SIZE))
snake_list.append(SnakeObject(170, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
snake_list.append(SnakeObject(140,200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
snake_list.append(SnakeObject(110, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))


global snake_head
snake_head = snake_list.head.value
snake_head.xspeed = 1

#-------------arena size, width and coords------
global arena_x, arena_y, arena_w, arena_h
arena_x = 150
arena_y = 80
arena_w = 1000
arena_h = 550

global apple
apple = GameObject(random.randint(arena_x, arena_w), random.randint(arena_y, arena_h), apple_img, 25, 25)
global apple_can_pickup
apple_can_pickup = True
global points
points = 0

global start_game
start_game = False
global game_over
game_over = False

#----------lives----
global lives
lives = 3
lives_icon = pygame.image.load(heart_img)
lives_icon = pygame.transform.scale(lives_icon, (25, 25))
global taking_damage
taking_damage = False
global damage_timer
damage_timer = 0

#-----------time travel code--------------
TIME_TRAVEL_LIMIT = 5
global previous_locations
previous_locations = Stack()
# number of time stamps recorded so far, can only record up to the last 5 moments at a time to count as 1 set before starting a new one
global num_temporal_recordings
num_temporal_recordings = 0
global record_loc_timer
record_loc_timer = 0
global previous_points
previous_points = Stack()
global previous_apple_loc
previous_apple_loc = Stack()

global previous_speed
previous_speed = Stack()

global using_reverse_time
using_reverse_time = False
global reverse_time_uses
reverse_time_uses = 2

global num_recent_time_stamps # number of recent moments the snake can jump back in time too
num_recent_time_stamps = 0

regular_font = pygame.font.get_default_font()
regular_font = pygame.font.Font(regular_font, 18)
h1_font = pygame.font.get_default_font()
h1_font = pygame.font.Font(h1_font, 32)
FLASH_TEXT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FLASH_TEXT_EVENT, 500)
global flash_text
flash_text = False

#---------main menu variables-------
start_game_option_loc = {
    "x": 570,
    "y": 400
}
quit_game_option_loc = {
    "x": 570,
    "y": 450
}
main_menu_options_cursor_loc = [start_game_option_loc, quit_game_option_loc]
main_menu_option = 0
on_main_menu = True
cursor = pygame.image.load(apple_img)
cursor = pygame.transform.scale(cursor, (25, 25))
global main_menu_snake_animation
main_menu_snake_animation = DoublyLinkedList()
main_menu_snake_animation.append(SnakeObject(200, 200, snake_head_img, SNAKE_SIZE, SNAKE_SIZE))
main_menu_snake_animation.append(SnakeObject(170, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
main_menu_snake_animation.append(SnakeObject(140,200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
main_menu_snake_animation.append(SnakeObject(110, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
main_menu_snake_animation.append(SnakeObject(80, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
global snake_anim_direction
snake_anim_direction = {
    "x_dir": 1,
    "y_dir": 0
}
SNAKE_ANIM_DIR_CHANGE = pygame.USEREVENT + 2
pygame.time.set_timer(SNAKE_ANIM_DIR_CHANGE, 7000)

def reset_game():


    global snake_list
    snake_list = DoublyLinkedList()
    snake_list.append(SnakeObject(200, 200, snake_head_img, SNAKE_SIZE, SNAKE_SIZE))
    snake_list.append(SnakeObject(170, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
    snake_list.append(SnakeObject(140, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
    snake_list.append(SnakeObject(110, 200, snake_body_img, SNAKE_SIZE, SNAKE_SIZE))

    global snake_head
    snake_head = snake_list.head.value
    snake_head.xspeed = 1

    global apple
    apple = GameObject(random.randint(arena_x, arena_w), random.randint(arena_y, arena_h), apple_img, 25, 25)
    global apple_can_pickup
    apple_can_pickup = True
    global points
    points = 0

    global start_game
    start_game = False
    global game_over
    game_over = False

    # -----------time travel code--------------
    global num_recent_time_stamps
    num_recent_time_stamps = 0
    global previous_locations
    previous_locations = Stack()
    global num_temporal_recordings
    num_temporal_recordings = 0
    global record_loc_timer
    record_loc_timer = 0
    global previous_points
    previous_points = Stack()
    global previous_apple_loc
    previous_apple_loc = Stack()

    global previous_speed
    previous_speed = Stack()

    global using_reverse_time
    using_reverse_time = False
    global reverse_time_uses
    reverse_time_uses = 5
    global snake_speed
    snake_speed = 5

def record_previous_locations_and_points():
    global previous_locations, num_temporal_recordings, snake_list, record_loc_timer
    global previous_points, previous_apple_loc, previous_speed
    global num_recent_time_stamps
    delta_time = clock.tick(frame_rate)
    record_loc_timer += delta_time
    if record_loc_timer > 2000:
        print("recording")
        record_loc_timer = 0
        if num_temporal_recordings < TIME_TRAVEL_LIMIT:
            num_temporal_recordings += 1
            if num_recent_time_stamps < TIME_TRAVEL_LIMIT:
                num_recent_time_stamps += 1
            temp = snake_list.head
            temp_list_coords = []
            while temp.has_next():
                coords = {
                    "x":temp.value.x,
                    "y": temp.value.y,
                    "prev_x": temp.value.prev_x,
                    "prev_y": temp.value.prev_y,
                    "x_dir": temp.value.x_dir,
                    "y_dir": temp.value.y_dir,
                }
                temp_list_coords.append(coords)
                temp = temp.next
            # need to add in the tail as the while loop stops before the tail
            coords = {
                "x": snake_list.tail.value.x,
                "y": snake_list.tail.value.y,
                "prev_x": snake_list.tail.value.prev_x,
                "prev_y": snake_list.tail.value.prev_y,
                "x_dir": snake_list.tail.value.x_dir,
                "y_dir": snake_list.tail.value.y_dir,
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
            previous_speed.add(snake_speed)
            
        else:
            temp_prev_snake_loc_stack = Stack()
            temp_points_stack = Stack()
            temp_apple_coords_stack = Stack()
            temp_previous_speed_stack = Stack()
            previous_locations.reverse_stack()
            previous_points.reverse_stack()
            previous_speed.reverse_stack()
            previous_apple_loc.reverse_stack()
            for i in range(TIME_TRAVEL_LIMIT): #resets the list by having it add the 5 most recent time steps recorded before recording more
                temp_prev_snake_loc_stack.add(previous_locations.as_list()[i])
                temp_points_stack.add(previous_points.as_list()[i])
                temp_apple_coords_stack.add(previous_apple_loc.as_list()[i])
                temp_previous_speed_stack.add(previous_speed.as_list()[i])
            previous_locations = temp_prev_snake_loc_stack
            previous_points = temp_points_stack
            previous_apple_loc = temp_apple_coords_stack
            previous_speed = temp_previous_speed_stack


            
            num_temporal_recordings = 0
        
def reverse_time():
    global previous_locations, snake_list, using_reverse_time
    global previous_points, points
    global snake_speed
    using_reverse_time = True
    temp = snake_list.head
    if previous_locations.size() != 0:
        last_loc = previous_locations.pop()
        if(last_loc != 0):
            for i in range(len(last_loc)):
                if temp is not None:
                    temp.value.x = last_loc[i]["x"]
                    temp.value.y = last_loc[i]["y"]
                    temp.value.prev_x = last_loc[i]["prev_x"]
                    temp.value.prev_y = last_loc[i]["prev_y"]
                    temp.value.x_dir = last_loc[i]["x_dir"]
                    temp.value.y_dir = last_loc[i]["y_dir"]
                    temp = temp.next
            # snake_list.tail.value.x = last_loc[-1]["x"]
            # snake_list.tail.value.y = last_loc[-1]["y"]
            # snake_list.tail.value.prev_x = last_loc[-1]["prev_x"]
            # snake_list.tail.value.prev_y = last_loc[-1]["prev_y"]
            # snake_list.tail.value.x_dir = last_loc[-1]["x_dir"]
            # snake_list.tail.value.y_dir = last_loc[-1]["y_dir"]
            # snake_list.tail.value.xspeed = 0
            # snake_list.tail.value.yspeed = 0
            if len(last_loc) < snake_list.size:
                difference = snake_list.size - len(last_loc)
                for i in range(difference):
                    snake_list.remove_last_object()

    if previous_points.size() != 0:
        points = previous_points.pop()


  
    if previous_apple_loc.size() != 0:
        previous_coords = previous_apple_loc.pop()
        if previous_coords != 0:
            apple.x = previous_coords["x"]
            apple.y = previous_coords["y"]
            apple.update_hit_box_loc()

    if previous_speed.size() != 0:
        snake_speed = previous_speed.pop()

            
def select_moment_in_time():
    global using_reverse_time
    if event.key == pygame.K_a and snake_head.xspeed <= 0:
        using_reverse_time = False
    elif event.key == pygame.K_d and snake_head.xspeed >= 0:
        using_reverse_time = False
    elif event.key == pygame.K_w and snake_head.yspeed <= 0:
        using_reverse_time = False
    elif event.key == pygame.K_s and snake_head.yspeed >= 0:
        using_reverse_time = False
def screen_wrap(gameObject: GameObject):
    if gameObject.x > 1400:
        gameObject.x = 0
        return True
    if gameObject.x < -50:
        gameObject.x = 1400
        return True
    if gameObject.y > 780:
        gameObject.y = 0
        return True
    elif gameObject.y < -50:
        gameObject.y = 720
        return True
    return False



def out_of_bounds():
    global snake_head, game_over
    if snake_head.x < arena_x:
        game_over = True
    if snake_head.x > arena_w + arena_x - SNAKE_SIZE:
        game_over = True
    if snake_head.y < arena_y:
        game_over = True
    if snake_head.y > arena_h + arena_y - SNAKE_SIZE:
        game_over = True


def take_damage_cooldown():
    global damage_timer, taking_damage
    if damage_timer < 90 and taking_damage is True:
        damage_timer += 1
    else:
        damage_timer = 0
        taking_damage = False
    print(damage_timer)
def move_display_snake():
    global snake_head, points
    global start_game, game_over, lives, taking_damage


    if start_game and using_reverse_time == False and game_over == False:
        snake_head.move()
        record_previous_locations_and_points()
    snake_head.display(screen)
    # snake_head.show_hit_box(screen)




    temp = snake_list.head.next
    while temp != None:
        if start_game and using_reverse_time == False and game_over == False:
            temp.value.x_dir = temp.prev.value.x_dir
            temp.value.y_dir = temp.prev.value.y_dir
            temp.value.move_to_new_spot(temp.prev.value.prev_x + -temp.prev.value.x_dir * (SNAKE_SIZE - 10 - snake_speed),
                                     temp.prev.value.prev_y + -temp.prev.value.y_dir * (SNAKE_SIZE - 10 - snake_speed))


        temp.value.update_hit_box_loc()
        temp.value.image_direction(temp.prev.value.x_dir, temp.prev.value.y_dir)
        temp.value.display(screen)
        # temp.value.show_hit_box(screen)

        if temp != snake_list.head.next and snake_head.collision(temp.value) and using_reverse_time == False:
            points -= 5
            if points < 0:
                points = 0
            for i in range(3):
                snake_list.remove_last_object()
            if taking_damage is False:
                taking_damage = True
                lives -= 1

        temp = temp.next

    take_damage_cooldown()



def draw_arena(x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 1)
#used to control the gameplay/things that render on the screen
def gameplay():
    global snake_head, apple_can_pickup, snake_list, points, snake_speed
    draw_arena(arena_x, arena_y, arena_w, arena_h)

    out_of_bounds()
    move_display_snake()

    apple.display(screen)
    if snake_head.collision(apple):

        apple.x = random.randint(arena_x, arena_w + arena_x - 25)
        apple.y = random.randint(arena_y, arena_h + arena_y - 25)
        apple.update_hit_box_loc()

        snake_list.append(SnakeObject(snake_list.tail.value.prev_x + -snake_list.tail.value.x_dir * SNAKE_SIZE
                                               , snake_list.tail.value.prev_y + -snake_list.tail.value.y_dir * SNAKE_SIZE,
                                               snake_body_img, SNAKE_SIZE, SNAKE_SIZE))
        points += 1
        if snake_speed < 25:
            snake_speed += 2

def main_menu():
    screen.fill(BLACK)
    title_text = pygame.font.Font.render(h1_font, f"SNAKE REVERSAL", True, WHITE)
    screen.blit(title_text, (475, 300))
    start_game_option_text = pygame.font.Font.render(regular_font, "start", True, WHITE)
    screen.blit(start_game_option_text, (600, 400))

    quit_game_option_text = pygame.font.Font.render(regular_font, "quit", True, WHITE)
    screen.blit(quit_game_option_text, (600, 450))

    screen.blit(cursor, (main_menu_options_cursor_loc[main_menu_option]["x"],
                         main_menu_options_cursor_loc[main_menu_option]["y"] - 5))

    global main_menu_snake_animation
    snake_anim_head = main_menu_snake_animation.head.value
    snake_anim_head.xspeed = snake_anim_direction["x_dir"] * 2
    snake_anim_head.x_dir = snake_anim_direction["x_dir"]
    snake_anim_head.yspeed = snake_anim_direction["y_dir"] * 2
    snake_anim_head.y_dir = snake_anim_direction["y_dir"]
    snake_anim_head.image_direction(snake_anim_head.x_dir, snake_anim_head.y_dir)
    snake_anim_head.display(screen)
    snake_anim_head.move()
    screen_wrap(snake_anim_head)

    temp = main_menu_snake_animation.head.next
    while temp != None:
        temp.value.x_dir = temp.prev.value.x_dir
        temp.value.y_dir = temp.prev.value.y_dir
        temp.value.move_to_new_spot(
            temp.prev.value.prev_x + -temp.prev.value.x_dir * (SNAKE_SIZE - 10),
            temp.prev.value.prev_y + -temp.prev.value.y_dir * (SNAKE_SIZE - 10))
        temp.value.image_direction(temp.prev.value.x_dir, temp.prev.value.y_dir)
        temp.value.display(screen)
        temp = temp.next
def UI():
    global flash_text, game_over
    points_text = pygame.font.Font.render(regular_font, f"Points: {points}", True, WHITE)
    screen.blit(points_text, (80, 50))
    using_reverse_time_text = pygame.font.Font.render(regular_font, "REWIND", True, WHITE)
    reverse_time_uses_text = pygame.font.Font.render(regular_font, f"{reverse_time_uses}", True, WHITE)
    if using_reverse_time:
        if flash_text:
            screen.blit(using_reverse_time_text, (200, 50))
    else:
        screen.blit(using_reverse_time_text, (200, 50))

    screen.blit(reverse_time_uses_text, (290, 50))

    for i in range(num_recent_time_stamps):
        pygame.draw.circle(screen, WHITE, (510 + 22 * i, 58), 10)
    num_temporal_recordings_text = pygame.font.Font.render(regular_font, "RECORDINGS:", True, WHITE)
    screen.blit(num_temporal_recordings_text, (350, 50))

    #---------life bar------------
    lives_text = pygame.font.Font.render(regular_font, "LIVES:", True, WHITE)
    screen.blit(lives_text, (820, 50))
    for i in range(lives):
        # pygame.draw.circle(screen, RED, (900 + 22 * i, 58), 10)
        screen.blit(lives_icon, (900 + 22 * i, 45))

    if game_over:
        game_over_text = pygame.font.Font.render(h1_font, "GAMEOVER", True, WHITE)
        screen.blit(game_over_text, (550, 320))






while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == FLASH_TEXT_EVENT:
            flash_text = not flash_text
        if event.type == SNAKE_ANIM_DIR_CHANGE:
            random_dir = random.randrange(4)
            if random_dir > 3:
                snake_anim_direction["x_dir"] = 1
                snake_anim_direction["y_dir"] = 0
            elif random_dir > 2:
                snake_anim_direction["x_dir"] = 0
                snake_anim_direction["y_dir"] = 1
            elif random_dir > 1:
                snake_anim_direction["x_dir"] = -1
                snake_anim_direction["y_dir"] = 0
            else:
                snake_anim_direction["x_dir"] = 0
                snake_anim_direction["y_dir"] = -1


        if event.type == pygame.KEYDOWN:
            if on_main_menu == True:
                if event.key == pygame.K_s:
                    main_menu_option = 1
                elif event.key == pygame.K_w:
                    main_menu_option = 0
                if event.key == pygame.K_RETURN:
                    if main_menu_option == 0:
                        on_main_menu = False
                    if main_menu_option == 1:
                        running = False
            else:
                if event.key == pygame.K_RETURN:
                    # reset_game()
                     snake_list.append(SnakeObject(200, 200, snake_body_img, 30, 30))

                if using_reverse_time:
                    select_moment_in_time()
                if event.key == pygame.K_a and snake_head.xspeed <= 0:
                    snake_head.image_direction(-1, 0)
                    snake_head.x_dir = -1
                    snake_head.y_dir = 0
                    snake_head.xspeed = -snake_speed
                    snake_head.yspeed = 0
                    start_game = True

                elif event.key == pygame.K_d and snake_head.xspeed >= 0:
                    snake_head.image_direction(1, 0)
                    snake_head.x_dir = 1
                    snake_head.y_dir = 0
                    snake_head.xspeed = snake_speed
                    snake_head.yspeed = 0
                    start_game = True

                elif event.key == pygame.K_w and snake_head.yspeed <= 0:
                    snake_head.image_direction(0, -1)
                    snake_head.x_dir = 0
                    snake_head.y_dir = -1
                    snake_head.yspeed = -snake_speed
                    snake_head.xspeed = 0
                    start_game = True

                elif event.key == pygame.K_s and snake_head.yspeed >= 0:
                    snake_head.image_direction(0, 1)
                    snake_head.x_dir = 0
                    snake_head.y_dir = 1
                    snake_head.yspeed = snake_speed
                    snake_head.xspeed = 0
                    start_game = True

                if event.key == pygame.K_SPACE:

                    if previous_locations.size() != 0 and num_recent_time_stamps != 0 and reverse_time_uses > 0:
                        num_recent_time_stamps -= 1
                        num_temporal_recordings -= 1
                        if using_reverse_time is False:
                            reverse_time_uses -= 1
                        reverse_time()







    screen.fill(BLACK)
    if on_main_menu:
        main_menu()
    else:
        gameplay()
        UI()
    pygame.display.flip()
    clock.tick(frame_rate)


pygame.quit()



