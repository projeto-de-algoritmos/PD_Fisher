import pygame
import random
import math
import time

import merge_sort as mg, closest_pair_of_points as closest, auxiliary as aux, colors

pygame.init()
clock = pygame.time.Clock()
size = (1366, 768)
level = 1

screen = pygame.display.set_mode(size)
screen.fill(colors.WHITE)

# variables for window customization
menu = pygame.image.load('../src/images/menu2.png')
players_img = pygame.image.load('../src/images/ship-player.png')
shoals_img = pygame.image.load('../src/images/bubbles.png')
port_img = pygame.image.load('../src/images/port.png')
pygame.display.set_caption("Cargo")
icon = pygame.image.load('../src/images/icon.png')
pygame.display.set_icon(icon)


# fazer função de fade in fade out pra dar blit nos cardumes


def player_interface(player):
    screen.blit(
        aux.text_outline(pygame.font.SysFont('default', 25), "Carga atual: " + str(player.current_load) + "/" + str(player.max_load), colors.WHITE, colors.BLACK),
        (5, 730))
    screen.blit(
        aux.text_outline(pygame.font.SysFont('default', 25),
                         "Valor da carga: " + str(player.total_value), colors.WHITE,
                         colors.BLACK),
        (5, 750))

    blit_pos = [10, 10]
    for shoal in player.shoals:
        pygame.draw.rect(screen, colors.BLACK, (blit_pos[0], blit_pos[1], 50, 50))
        pygame.draw.rect(screen, colors.WHITE, (blit_pos[0]+5, blit_pos[1]+5, 40, 40))
        screen.blit(shoal.fish_image, (blit_pos[0]+5, blit_pos[1]+10))
        screen.blit(
            aux.text_outline(pygame.font.SysFont('default', 25), str(shoal.name), colors.WHITE, colors.BLACK),
            (70, blit_pos[1] + 5))
        screen.blit(
            aux.text_outline(pygame.font.SysFont('default', 22), "V: " + str(shoal.value), colors.WHITE, colors.BLACK),
            (70, blit_pos[1]+30))
        screen.blit(
            aux.text_outline(pygame.font.SysFont('default', 22), "P: " + str(shoal.weight), colors.WHITE, colors.BLACK),
            (110, blit_pos[1]+30))
        blit_pos[1] += 60


def harbor_interface(out):
    screen.blit(
        aux.text_outline(pygame.font.SysFont('default', 25),
                         "Carga atual: " + str(out.load) + "/" + str(out.max_load), colors.WHITE,
                         colors.BLACK),
        (1140, 730))
    screen.blit(
        aux.text_outline(pygame.font.SysFont('default', 25),
                         "Valor total: " + str(out.current_value) + "/" + str(out.quota), colors.WHITE,
                         colors.BLACK),
        (1150, 750))


# updates and redraws position of all objects on screen
def update(player, out, shoals):
    player.rect[1] -= player.movement[0]
    player.rect[1] += player.movement[1]
    player.rect[0] -= player.movement[2]
    player.rect[0] += player.movement[3]
    if player.rect[0] < 0:
        player.rect[0] = 0
    elif player.rect[0] > 1346:
        player.rect[0] = 1346
    elif player.rect[1] < 0:
        player.rect[1] = 0
    elif player.rect[1] > 748:
        player.rect[1] = 748
    screen.fill(colors.BRIGHT_GREEN)
    screen.blit(players_img, player)
    screen.blit(port_img, out)
    for shoal in shoals:
        if time.perf_counter() - shoal.time_of_creation > random.uniform(4.0, 6.0):
            shoals.remove(shoal)
            continue
        screen.blit(shoals_img, shoal)
    player_interface(player)
    harbor_interface(out)


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(10, 10, 20, 20)
        self.movement = [0, 0, 0, 0]
        self.current_load = 0
        self.max_load = 20
        self.total_value = 0
        self.shoals = []


class Exit(object):
    def __init__(self):
        self.load = 0
        self.current_value = 0
        self.max_load = 60
        self.quota = 80
        self.rect = pygame.Rect(1298, 698, 20, 20)
        self.shoals = []


class Shoal(object):
    def __init__(self):
        self.rect = pygame.Rect(random.randint(20, 1340), random.randint(20, 740), 20, 20)
        self.time_of_creation = time.perf_counter()
        self.fish_image = None
        self.name = None
        fish = {
            "pink salmon": aux.pink_salmon,
            "pollock": aux.pollock,
            "gilt-head bream": aux.gilt_head_bream,
            "rockfish": aux.rockfish,
            "mackerel": aux.mackerel,
            "sea bass": aux.sea_bass,
            "keta": aux.keta,
            "codfish": aux.codfish,
            "barracuda": aux.barracuda,
            "lemonema": aux.lemonema,
            "tuna": aux.tuna,
            "halibut": aux.halibut
        }
        fishes = ["pink salmon", "pollock", "gilt-head bream", "rockfish", "mackerel", "sea bass", "keta", "codfish", "barracuda", "lemonema", "tuna", "halibut"]
        chances = [0.1, 0.25, 0.25, 0.1, 0.25, 0.2, 0.3, 0.25, 0.15, 0.25, 0.25, 0.2]
        self.value = random.randint(1, 20)
        self.weight = random.randint(1, 5)
        fish[random.choices(fishes, chances)[0]](self)


def get_x_coordinates(shoals, player):
    temp = []
    for shoal in shoals:
        temp.append((shoal.rect[0], shoal.rect[1]))
    temp.append((player.rect[0], player.rect[1]))
    return temp


# detects collision using closest pair algorithm
def collision(shoals, ordered_array, player):
    if shoals:
        pair = closest.closest_pair(ordered_array)
        p1 = pair[0]
        p2 = pair[1]
        if p1 and math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) < 30:
            if p1 == (player.rect[0], player.rect[1]) or p2 == (player.rect[0], player.rect[1]):
                for shoal in shoals:
                    if (shoal.rect[0], shoal.rect[1]) == p1 or (shoal.rect[0], shoal.rect[1]) == p2:
                        if player.max_load >= player.current_load + shoal.weight:
                            player.current_load += shoal.weight
                            player.total_value += shoal.value
                            player.shoals.append(shoal)
                            shoals.remove(shoal)
                        break
            else:
                for shoal in shoals:
                    if (shoal.rect[0], shoal.rect[1]) == p1:
                        shoals.remove(shoal)
                        break


def menu_window():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aux.quit_game()

        screen.fill(colors.WHITE)
        screen.blit(menu, (0, 0))

        aux.button(screen, 'START', 550, 55, 240, 100, colors.START, game_loop)
        pygame.display.update()
        clock.tick(15)


def restart_game_window(win):
    global level
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aux.quit_game()

        if win and level == 5:
            finish_game_window()

        aux.button(screen, 'RESTART', 510, 450, 100, 50, colors.GREEN, game_loop)
        if win:
            aux.game_win_text(screen)
            aux.button(screen, 'NEXT', 630, 450, 100, 50, colors.BLUE, game_loop)
        else:
            aux.game_lose_text(screen)
        aux.button(screen, 'QUIT', 750, 450, 100, 50, colors.RED, aux.quit_game)

        pygame.display.update()
        clock.tick(15)


def finish_game_window():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aux.quit_game()

        aux.game_finish_text(screen)
        aux.button(screen, 'QUIT', 630, 450, 100, 50, colors.RED, aux.quit_game)

        pygame.display.update()
        clock.tick(15)


# increase difficulty
def next_level(out):
    global level
    level += 1
    if level == 6:
        finish_game_window()
    out.load = 0
    out.current_value = 0
    out.max_load -= 5
    out.quota += 10


def game_loop():
    level_timer = time.perf_counter()
    show_timer = 60
    elapsed = time.perf_counter()
    player = Player()
    out = Exit()
    shoals = []

    while True:
        update(player, out, shoals)

        aux.timer_text(screen, show_timer)
        show_timer -= (time.perf_counter() - level_timer)
        level_timer = time.perf_counter()
        if show_timer < 0:
            restart_game_window(False)
        if time.perf_counter() - elapsed > random.uniform(1.0, 2.0):
            shoals.append(Shoal())
            elapsed = time.perf_counter()

        ordered_array = mg.merge_sort(get_x_coordinates(shoals, player))
        collision(shoals, ordered_array, player)

        if math.sqrt((player.rect[0] - out.rect[0]) ** 2 + (player.rect[1] - out.rect[1]) ** 2) < 30:
            # knapsack usando os cardumes do navio e do porto, descartar os q n forem selecionados
            if out.current_value >= out.quota:
                next_level(out)
                restart_game_window(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aux.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.shoals:
                        temp = player.shoals.pop()
                        player.current_load -= temp.weight
                        player.total_value -= temp.value
                if event.key == pygame.K_UP:
                    player.movement[0] = 1
                if event.key == pygame.K_DOWN:
                    player.movement[1] = 1
                if event.key == pygame.K_LEFT:
                    player.movement[2] = 1
                if event.key == pygame.K_RIGHT:
                    player.movement[3] = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.movement[0] = 0
                if event.key == pygame.K_DOWN:
                    player.movement[1] = 0
                if event.key == pygame.K_LEFT:
                    player.movement[2] = 0
                if event.key == pygame.K_RIGHT:
                    player.movement[3] = 0

        pygame.display.update()
        clock.tick(240)


def main():
    menu_window()
    game_loop()


if __name__ == "__main__":
    main()
