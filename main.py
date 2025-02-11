# Imports
import sys
import pygame
from ld_images import *
from pyplot import *
import maze
import race
import RhythmGame
import wakeUp
import const

# Configuration
pygame.init()
info = pygame.display.Info()
fps = 10
fpsClock = pygame.time.Clock()
pygame.display.set_caption('HSE! STUDENT! LIFE!')
width = info.current_w
height = info.current_h

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.SCALED | pygame.HWSURFACE)
game_started = False
font = pygame.font.Font('TT Norms Pro Regular.otf', 30)
nm = (0, 0)
tfon = home

# ПЕРЕКИНУТЬ В const.pe

obj_messageNum_to_game_func = {
    (1, 2, 2): wakeUp.wakeUp,  # 1lvl
    (1, 5, 4): wakeUp.wakeUp,
    (1, 3, 5): maze.start_maze,
    (1, 6, 3): maze.start_maze,
    (1, 7, 9): race.start_race,
    (1, 4, 2): RhythmGame.rhythm_game_start,
    (1, 9, 8): RhythmGame.rhythm_game_start,

    (2, 2, 8): wakeUp.wakeUp,  # 2lvl
    (2, 5, 2): race.start_race,
    (2, 7, 4): maze.start_maze,
    (2, 8, 1): race.start_race,
    (2, 9, 6): wakeUp.wakeUp,
    (2, 13, 2): race.start_race,
    (2, 15, 4): maze.start_maze,
    (2, 16, 1): race.start_race,
    (2, 25, 7): wakeUp.wakeUp,

    (3, 4, 4): race.start_race,  # 3lvl
    (3, 6, 0): RhythmGame.rhythm_game_start,
    (3, 7, 0): RhythmGame.rhythm_game_start,
    (3, 8, 0): RhythmGame.rhythm_game_start,
    (3, 10, 2): wakeUp.wakeUp,
    (3, 16, 4): race.start_race,
    (3, 16, 5): maze.start_maze,
    (3, 17, 0): RhythmGame.rhythm_game_start

}


# ПЕРЕКИНУТЬ В const.py


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, font, fc, image, size, where):
        pygame.sprite.Sprite.__init__(self)
        if image == ex:
            image.set_alpha(255)
        image = pygame.transform.scale(image, size)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.buttonText = font.render(text, True, fc)
        self.where = where

    def use(self):
        return self.where


class BackGround(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        if image != startback and image != dg:
            image.set_alpha(250)
        image = pygame.transform.smoothscale(image, (width, height))
        self.image = image
        self.rect = self.image.get_rect(center=(width / 2, height / 2))


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, image, size):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.transform.scale(image, size)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))


use_sprites = pygame.sprite.Group()  # interactive sprites
dec_sprites = pygame.sprite.Group()
# starting screen
back = BackGround(startback)
st1 = Button([width / 4, height / 2 + 50], 's', font, (0, 0, 0), sb1, (808, 152), (1, 0, 0))
st2 = Button([width / 4 + 10, height / 2 + 200], '', font, (0, 0, 0), sb2, (804, 151), (2, 0, 0))
st3 = Button([width / 4, height / 2 + 350], '', font, (0, 0, 0), sb3, (800, 150), (3, 0, 0))
use_sprites.add(st1)
use_sprites.add(st2)
use_sprites.add(st3)
dec_sprites.add(back)


def blit_text(surface, text, pos, font, color=pygame.Color('gray'), size=30):
    words = [word.split(' ') for word in text.splitlines()]
    font = pygame.font.Font('TT Norms Pro Regular.otf', size)
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()[0] - 230, surface.get_size()[1]
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


def level(num):
    global nm, tfon

    use_sprites.empty()
    dec_sprites.empty()

    nm = num
    if num in TimeSkip.keys():
        back = BackGround(tsk)
        dec_sprites.add(back)
        for i in range(25):
            dec_sprites.update()
            screen.fill((0, 0, 0))
            dec_sprites.draw(screen)
            pygame.display.flip()
    if num == (0, 0):
        exit(0)
    if num == (-1, 0):
        back = BackGround(busted)
        dec_sprites.add(back)
        exi = Button([width / 2, 60], '', font, (0, 0, 0), ex, (300, 120), (0, 0))
        use_sprites.add(exi)
        return 0
    if num == (-1, 1):
        back = BackGround(good)
        dec_sprites.add(back)
        exi = Button([width / 2, 60], '', font, (0, 0, 0), ex, (300, 120), (0, 0))
        use_sprites.add(exi)
        return 0
    pygame.display.flip()
    if num in backs.keys():
        tfon = backs[num]
    back = BackGround(tfon)
    dec_sprites.add(back)
    if num in hero.keys():
        hr = hero[num]
        h1 = Hero(width / 5 * 3, height / 2, hr[0], (1080, height))
        dec_sprites.add(h1)
        if len(hr) == 2:
            h2 = Hero(width / 3, height / 2, hr[1], (1080, height))
            dec_sprites.add(h2)
    dlg = BackGround(dg)
    dec_sprites.add(dlg)
    frw = Button([width - 150, 50], '', font, (0, 0, 0), sk, (240, 60), (num[0], num[1], min(mx[(num[0], num[1])], num[2] + 1)))
    bck = Button([150, 50], '', font, (0, 0, 0), bc, (240, 60), (num[0], num[1], max(num[2] - 1, 0)))
    exi = Button([width / 2, 60], '', font, (0, 0, 0), ex, (300, 120), (0, 0))
    use_sprites.add(bck)
    use_sprites.add(frw)
    use_sprites.add(exi)

    if num in obj_messageNum_to_game_func.keys():
        obj_messageNum_to_game_func[num](screen, width, height)

    if num[2] == mx[num[0], num[1]] and num not in finale.keys():
        ch1 = Button([width / 2, 282], '', font, (0, 0, 0), btup, (width, 475), btn[num[0], num[1], 1][1])
        ch2 = Button([width / 2, height / 2 + 231], '', font, (0, 0, 0), btdn, (width, 605), btn[num[0], num[1], 2][1])
        ask = Hero(width / 2, height / 6,ak , (width, height/6))
        use_sprites.add(ch1)
        use_sprites.add(ch2)
        use_sprites.add(ask)
        textpos = (width / 2, 60)
        blit_text(ask.image, question[num[0], num[1], 1], textpos, font, size=40)
        textpos = (width / 2, 330)
        blit_text(ch1.image, btn[num[0], num[1], 1][0], textpos, font)
        textpos = (int(width / 2 - width * 0.0052 * len(btn[num[0], num[1], 2][0])), height * 0.083)
        blit_text(ch2.image, btn[num[0], num[1], 2][0], textpos, font)
    if num in finale.keys():
        ch1 = Button([width / 2, height * 0.2], '', font, (0, 0, 0), btup, (width, height * 0.495),
                     (-1, finale[num]))
        ch2 = Button([width / 2, height * 0.72], '', font, (0, 0, 0), btdn, (width, height * 0.63),
                     (-1, finale[num]))
        use_sprites.add(ch1)
        use_sprites.add(ch2)
        textpos = (int(width / 2 - width * 0.0052 * 7), height * 0.344)
        blit_text(ch1.image, 'THE END', textpos, font)
        textpos = (int(width / 2 - width * 0.0052 * 7), height * 0.083)
        blit_text(ch2.image, 'THE END', textpos, font)

    textpos = (width * 0.143, height * 0.76)
    blit_text(dlg.image, text[num], textpos, font)


# dialogue window
# back = BackGround()
# hero = Hero()
temp = 0
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in use_sprites:
                if sprite.rect.collidepoint(event.pos):
                    sprite.image.set_alpha(150)
                    temp = sprite
        elif event.type == pygame.MOUSEBUTTONUP and temp:
            level(temp.use())
            temp = 0
        elif event.type == pygame.KEYDOWN:
            if nm[0] == -1:
                exit(0)
            if event.key == pygame.K_RIGHT:
                if nm != (0, 0):
                    level((nm[0], nm[1], min(mx[(nm[0], nm[1])], nm[2] + 1)))
            if event.key == pygame.K_LEFT:
                if nm != (0, 0):
                    level((nm[0], nm[1], max(nm[2] - 1, 0)))

    dec_sprites.update()
    use_sprites.update()
    screen.fill((0, 0, 0))
    dec_sprites.draw(screen)
    use_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

#WE ARE PROGRAMMERS TEAM WE ENTIRELY DEAD AFTER THIS WORK ITS SO HARD TO MAKE IT LOOK EXACTLY AS WE WANT IT TO BE/ SAVE OUR SOULS