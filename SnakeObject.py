from GameObject import GameObject
import pygame

class SnakeObject(GameObject):
    def __init__(self, x, y, img=None, width=50, height=50):
        super().__init__(x, y, img, width, height)
        self.prev_x = self.x
        self.prev_y = self.y
        self.face_right_img = pygame.transform.rotate(self.img, -90)
        self.face_left_img = pygame.transform.rotate(self.img, 90)
        self.face_down_img = pygame.transform.flip(self.img, False, True)
        self.face_up_img = self.img
        self.hit_box = pygame.Rect(self.x, self.y, 15, 15)
        self.x_dir = 0 # direction it is heading in
        self.y_dir = 0

    def set_speed(self, xspeed, yspeed):
        self.xspeed = xspeed
        self.yspeed = yspeed
    def move(self):
        self.prev_x = self.x
        self.prev_y = self.y
        super().move()


    def move_to_new_spot(self, newx, newy):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = newx
        self.y = newy


    def image_direction(self, xdir, ydir):
        if xdir < 0:
            self.img = self.face_left_img
        elif xdir > 0:
            self.img = self.face_right_img
        elif ydir > 0:
            self.img = self.face_down_img
        elif ydir < 0:
            self.img = self.face_up_img

    def update_hit_box_loc(self):
        self.hit_box.x = self.x + 7
        self.hit_box.y = self.y + 7




