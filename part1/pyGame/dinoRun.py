import pygame 
import os 

pygame.init()

ASSETS = 'part1/pyGame/Assets/'
SCREEN = pygame.display.set_mode((1100, 600))

BG = pygame.image.load(os.path.join(f'{ASSETS}Other', 'Track.png'))

icon = pygame.image.load('part1/pyGame/dinorun.png')
pygame.display.set_icon(icon)


class Dino:
    X_Pos = 80; Y_Pos = 310

    def __init__(self) -> None:
        pass 

    def update(self, userInput) -> None:
        pass 

    def run(self):
        self.image = self.run_img[self.step_index // 5]

    def duck(self):
        pass
    
    def jump(self):
        pass

    def update(self, userInput) -> None:
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
        
        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True 
            self.dino_jump = False 
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True 
            self.dino_duck = False
            self.dino_jump = False



def main():
    run = True 
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        clock.tick(30)
        pygame.display.update()

if __name__ == '__main__':
    main()