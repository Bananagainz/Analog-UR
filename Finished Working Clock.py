import pygame
import math
import datetime

pygame.init() 
pygame.display.set_caption("Miniprojekt - UR")
clock=pygame.time.Clock()
screen = pygame.display.set_mode((600, 600)) 


def print_text(text, x, y):
    font = pygame.font.SysFont("Times New Roman", 40, True, False, None)
    surface = font.render(text, True, (255,0,0))
    screen.blit(surface, (x, y))

    

def viser_placering(R,degree):
    x=math.sin(2*math.pi*degree/360)*R
    y=math.cos(2*math.pi*degree/360)*R
    return x+300, -(y-300)



def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
            
        screen.fill((255, 255, 255)) 
        pygame.draw.circle(screen, (0,0,0), center=(300, 300), radius=(250))

        current_time=datetime.datetime.now()
        second=current_time.second
        minute=current_time.minute
        hour=current_time.hour

        for number in range(1, 13):
            angle = math.radians(number * 30)  
            radius = 210  
            x = 285 + radius * math.sin(angle)
            y = 285 - radius * math.cos(angle)
            print_text(str(number), x, y)


        #second
        R=230
        degree=second*(360/60)
        pygame.draw.line(screen, (255, 0,0), (300, 300), viser_placering(R, degree), 2)

        #minute
        R=200
        degree=(minute+second/60)*(360/60)
        pygame.draw.line(screen, (0, 255, 0), (300, 300), viser_placering(R, degree), 6)

        #hour
        R=140
        degree=(hour+minute/60)*(360/12)
        pygame.draw.line(screen, (0, 0, 255), (300, 300), viser_placering(R, degree), 6)

        pygame.display.update()
        clock.tick(60)            
game()
pygame.quit()           
    