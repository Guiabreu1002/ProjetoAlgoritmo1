import random
import curses

# Tamanho do mapa
MAP_WIDTH = 20
MAP_HEIGHT = 10

# Classe para representar o jogador
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 100
        self.damage = 10

    def move(self, dx, dy):
        if 0 <= self.x + dx < MAP_WIDTH and 0 <= self.y + dy < MAP_HEIGHT:
            self.x += dx
            self.y += dy

    def attack(self, enemy):
        damage_dealt = random.randint(0, self.damage)
        enemy.hp -= damage_dealt
        return damage_dealt

# Classe para representar um inimigo
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 20
        self.damage = 5

    def attack(self, player):
        damage_dealt = random.randint(0, self.damage)
        player.hp -= damage_dealt
        return damage_dealt

# Função para desenhar o mapa
def draw_map(stdscr, player, enemies):
    stdscr.clear()
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if x == player.x and y == player.y:
                stdscr.addstr(y, x, "P")
            elif any(enemy.x == x and enemy.y == y for enemy in enemies):
                stdscr.addstr(y, x, "E")
            else:
                stdscr.addstr(y, x, ".")
    stdscr.addstr(MAP_HEIGHT + 1, 0, f"HP: {player.hp}")
    stdscr.refresh()

# Função principal do jogo
def main(stdscr):
    curses.curs_set(0)  # Esconde o cursor
    stdscr.nodelay(True)  # Não aguarda a entrada do usuário
    player = Player()
    enemies = [Enemy(random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)) for _ in range(3)]

    while True:
        draw_map(stdscr, player, enemies)

        move = stdscr.getch()
        if move == ord('q'):
            break
        elif move == curses.KEY_UP:
            player.move(0, -1)
        elif move == curses.KEY_DOWN:
            player.move(0, 1)
        elif move == curses.KEY_LEFT:
            player.move(-1, 0)
        elif move == curses.KEY_RIGHT:
            player.move(1, 0)

        for enemy in enemies:
            if enemy.hp <= 0:
                enemies.remove(enemy)
                continue
            enemy.move(random.randint(-1, 1), random.randint(-1, 1))
            if enemy.x == player.x and enemy.y == player.y:
                damage_taken = enemy.attack(player)

        if player.hp <= 0:
            stdscr.addstr(MAP_HEIGHT + 2, 0, "Você morreu!")
            stdscr.refresh()
            stdscr.getch()
            break

if __name__ == "__main__":
    curses.wrapper(main)