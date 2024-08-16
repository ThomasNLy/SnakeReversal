import pygame


class GameObject():
    def __init__(self, x, y, img=None, width=50, height=50):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 0
        if img is not None:
            self.img = pygame.image.load(img)
            self.img = pygame.transform.scale(self.img, (width, height))
            self.hit_box = pygame.Rect(self.x, self.y, width, height)
            self.w = width
            self.h = height


        else:
            self.img = None
            self.hit_box = pygame.Rect(width, height, self.x, self.y)

    def display(self, screen):
        if self.img is not None:
            screen.blit(self.img, (self.x, self.y))
        else:
            pygame.draw.rect(screen, ((255, 255, 255), (100, 100, self.x, self.y)))

    def collision(self, other):
        if self.hit_box.colliderect(other.hit_box):
            return True
        return False

    def show_hit_box(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hit_box)

    def update_hit_box_loc(self):
        self.hit_box.x = self.x
        self.hit_box.y = self.y

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.update_hit_box_loc()


