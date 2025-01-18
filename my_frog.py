import pygame
import sys

pygame.init()
screen_width, screen_height = 1800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frogs and Stones")
clock = pygame.time.Clock()
colors = {
    'frog_color': (0, 255, 0),
    'stone_color': (153, 76, 0),
    'yellow_color': (255, 255, 0),
    'background_color': (200, 235, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0)
}

num_stones = 40
stone_width, stone_height = 80, 50
stones = []
stone_states = []  

for i in range(num_stones):
    x = i * (stone_width + 10) + 50
    y = screen_height - 300
    stones.append(pygame.Rect(x, y, stone_width, stone_height))
    stone_states.append(False) 


num_frogs = 40
frogs = []
frog_positions = []
frog_start_delay = []  

for i in range(num_frogs):
    x = 50
    y = screen_height - 400
    frogs.append((x, y))
    frog_positions.append(0)  
    frog_start_delay.append(i * 10)  


def create_the_frog(x, y,index):
    pygame.draw.ellipse(screen, colors['frog_color'], (x - 20, y - 15, 70, 30))
    pygame.draw.ellipse(screen, colors['black'], (x - 20, y - 15, 70, 30), 3)
    pygame.draw.circle(screen, colors['frog_color'], (x + 15, y - 30), 27)
    pygame.draw.ellipse(screen, colors['red'], (x + 2, y - 25, 30, 10))
    pygame.draw.circle(screen, colors['black'], (x + 15, y - 30), 27, 3)
    pygame.draw.circle(screen, colors['black'], (x + 5, y - 50), 10)
    pygame.draw.circle(screen, colors['black'], (x + 30, y - 50), 10)
    pygame.draw.circle(screen, colors['white'], (x + 5, y - 50), 3)
    pygame.draw.circle(screen, colors['white'], (x + 30, y - 50), 3)
    font=pygame.font.Font(None,25)
    text=font.render(f'{index}',True,colors['black'])
    screen.blit(text,(x+8,y-2))


def draw():
    screen.fill(colors['background_color'])
    for i, stone in enumerate(stones):
        color = colors['yellow_color'] if stone_states[i] else colors['stone_color']
        pygame.draw.ellipse(screen, color, stone)
        pygame.draw.ellipse(screen,colors['black'],stone,5)
        font = pygame.font.Font(None, 40)
        text = font.render(f'{i}', True, colors['black'])  
        screen.blit(text, (stone.x + 30, stone.y + 15))
    index=1
    for x, y in frogs:
        create_the_frog(x, y,index)
        index+=1

    pygame.display.flip()


def update():
    for i in range(num_frogs):
        if frog_start_delay[i] >0:
            frog_start_delay[i] -= 1
            continue

        x, y = frogs[i] #the position
        current_position = frog_positions[i]

        if current_position < num_stones:
            #the next stone of the frog
            target_index = current_position
            target_x = stones[target_index].x + stone_width // 2
            target_y = stones[target_index].y - 40

           
            new_x = x + (target_x - x) // 2 
            new_y = y + (target_y - y) // 2
            frogs[i] = (new_x, new_y)

            
            if abs(new_x - target_x) < 5 and abs(new_y - target_y) < 5:
                stone_states[target_index] = not stone_states[target_index]
                frog_positions[i] += i + 1 #each frog jump according to her index  

frame_counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    frame_counter += 1
    if frame_counter % 15 == 0:  
        update()

    draw()
    clock.tick(100)
