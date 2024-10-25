import math
import time

# ---------------------------------
# переменные для лабиринта
# время на прохождение в сек

delta_time = 100

# произвольно

WIDTH_MAZE_WINDOW, HEIGHT_MAZE_WINDOW = 1200, 800
HALF_WIDTH = WIDTH_MAZE_WINDOW // 2
HALF_HEIGHT = HEIGHT_MAZE_WINDOW // 2
FPS = 60
TILE = 100
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE

# рей кастинг

FOV = math.pi / 3 # чем больше делитель тем ближе стены
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * TILE
SCALE = WIDTH_MAZE_WINDOW // NUM_RAYS
TEXTURE_WIDTH = 200
TEXTURE_HEIGHT = 200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# настройки игрока

player_pos = (TILE * 1.5, TILE * 1.5)
player_angle = 0
player_speed = 3

# цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (140, 0, 0)
DARKGRAY = (40, 40, 40)
FLOOR = (74, 70, 64)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

cur_time = time.time_ns()


def freeze():
    global cur_time
    delta = (time.time_ns() - cur_time) / 1000000000
    cur_time = time.time_ns()
    return delta

# -----------------------------------------------------
# переменные для гонок

WIDTH_CAR_WINDOW, HEIGHT_CAR_WINDOW = 600, 800
CAR_WIDTH, CAR_HEIGHT = 50, 100
BUS_SCALE = 1.44 # во сколько раз автобус больше чем машины
BUS_WIDTH, BUS_HEIGHT = BUS_SCALE * CAR_WIDTH, BUS_SCALE * CAR_HEIGHT
BUS_SPEED, CAR_SPEED = 4, 7
LANE_WIDTH = WIDTH_CAR_WINDOW // 3
MIN_DISTANCE = 100 # минимальное расстояние между машинами
WIN = 40 # столько машин надо преодолеть, чтобы выиграть

length_line = HEIGHT_CAR_WINDOW // 10 # длина пунктирной линии
distance = HEIGHT_CAR_WINDOW // length_line * 3 # расстояние между пунктирными линиями
frequency = 40 # частота появления машин (чем больше число - тем реже)

#    |----------------------------------|
#    |    переменные для РИТМ ИГРЫ      |
#    |----------------------------------|

WIDTH_RYTHM_WINDOW, HEIGHT_RYTHM_WINDOW = 1100, 800
btnEventId = {"RIGHT": 1073741903, "LEFT": 1073741904, "DOWN": 1073741905, "UP":1073741906, "SPACE": 32}

rhythmLine_1LVL = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP"] # список клавиш, которые надо  (1LVL)
setting_rythm_1lvl = (5, 3, 5, rhythmLine_1LVL) # healt_points, wait_new_msg, wait_answer

rhythmLine_2LVL = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP", "DOWN", "RIGHT", "LEFT"] # список клавиш, которые надо  (1LVL)
setting_rythm_2lvl = (3, 2, 3, rhythmLine_1LVL) # healt_points, wait_new_msg, wait_answer

rhythmLine_3LVL = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP", "RIGHT", "LEFT", "DOWN", "UP", "LEFT", "RIGHT"] # список клавиш, которые надо  (3LVL)
setting_rythm_3lvl = (2, 1, 2, rhythmLine_1LVL) # healt_points, wait_new_msg, wait_answer


#    |----------------------------------|
#    |  переменные для ПРОСЫПАШКИ ИГРЫ  |
#    |----------------------------------|

WIDTH_WAKEUP_WINDOW, HEIGHT_WAKEUP_WINDOW = 1100, 800
setting_wakeup_1lvl = (1, 5) # уменьшение прогресса каждую секунду, уменьшение прогресса через 5сек
setting_wakeup_2lvl = (2, 7)
setting_wakeup_3lvl = (3, 10)