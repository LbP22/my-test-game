# Example file showing a circle moving on screen
import asyncio
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((2560, 1440))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 4)

async def printtest():
    i = 0
    while True:
        print(i)
        i += 1
        await asyncio.sleep(1)


def moveUp():
    player_pos.y -= 300 * dt

def moveDown():
    player_pos.y += 300 * dt

def moveLeft():
    player_pos.x -= 300 * dt

def moveRight():
    player_pos.x += 300 * dt

def skip():
    pass


def keys_wrapper(current_keys: list[bool]):
    keys = {
        pygame.K_w: moveUp,
        pygame.K_s: moveDown,
        pygame.K_a: moveLeft,
        pygame.K_d: moveRight,
        pygame.K_ESCAPE: quit
    }
    for i, _ in enumerate(current_keys):
        if current_keys[i]:
            keys.get(i, skip)()


def events_wrapper(current_events: list[pygame.event]):
    global running
    events = {
        pygame.QUIT: pygame.quit
    }
    for event in current_events:
        events.get(event.type, skip)()


async def main():
    global running, dt, player_pos
    while running:
        events_wrapper(pygame.event.get())

        screen.fill("gray") # fill the screen with a color to wipe away anything from last frame

        pygame.draw.circle(screen, "red", player_pos, 100)

        keys = pygame.key.get_pressed()
        keys_wrapper(keys)

        pygame.display.flip() # flip() the display to put your work on screen
        dt = clock.tick(1000) / 1000 # dt is delta time in seconds since last frame, used for framerate-independent physics.

asyncio.run(main())
pygame.quit()
