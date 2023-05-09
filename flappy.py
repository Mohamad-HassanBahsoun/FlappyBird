import pygame, sys, random

def draw_floor():
    # puts 2 floor beside one another so when one moves to the left is basically
    # resets and keeps going when applied to the while loop
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576,900))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height) # randomely pics a pipe hieght so its not always the same
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos-300))
    return bottom_pipe,top_pipe
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)

#Creating our window
pygame.init()
pygame.display.set_caption('Bahsoun_Test1')
screen = pygame.display.set_mode((576,1024)) #width and height
clock = pygame.time.Clock()

#Game variables
gravity = 0.25
bird_movement = 0


bg_surface = pygame.image.load('assets/background-day.png').convert() # helps pygame run easier, runs at a more consistant pace, usually used for things that move
#bg_surface = pygame.transform.scale2x(bg_surface) if you dont edit the actual png you could do this to make the size of the background bigger


floor_surface = pygame.image.load('assets/base.png')
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_sruface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_sruface)
bird_rect = bird_surface.get_rect(center = (100,512)) # adds a rectangle around it, and where its center is

pipe_surface =pygame.image.load('assets/pipe-green.png')
pipe_surface =pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT # event will be triggered by timer
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # what allows us to close via the x in the corner
            sys.exit() # most definitely ends our code/ loop
        if event.type == pygame.KEYDOWN: # checks if a key is pressed
            if event.key == pygame.K_SPACE: # keyboard
                bird_movement = 0 # we do this to disable the effects of gravity
                bird_movement-= 12
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface,(0,0)) # blit basically draws

    # Bird
    bird_movement +=gravity #adds gravity to the birds movement
    bird_rect.centery +=bird_movement #we change the birds y (up and down movement) so now it falls
    screen.blit(bird_surface,bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list) # re assigns pipelist so that
    draw_pipes(pipe_list)

    # Floor
    floor_x_pos -=1 # allows the floor to move, constantly changing the x position
    draw_floor()
    if floor_x_pos <= -576:
        # once the floor goes to far to the left we reset so the floor movement is fluid
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(120) # says that max framerate is 120

