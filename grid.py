import pygame
import sys
from include.system.Settings import FPS, BGCOLOR, GREEN, RED, BLUE, YELLOW, WHITE, TILESIZE

COLS = 50
ROWS = 30

screenWidth = COLS * TILESIZE
screenHeight = ROWS * TILESIZE

def init():
    pygame.init()
   #pygame.mixer.init()
    win = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("UI System")
    clock = pygame.time.Clock()
    
    return win, clock

win, clock = init()

class LeftMargin:
    def __init__(self):
        self.size = [0, int((COLS / 4) * TILESIZE)]
        self.cols = int((self.size[1] - self.size[0]) / TILESIZE) 
    def printMarginSize(self):
        return self.size

    def printMarginCols(self):
        return self.cols


class RightMargin:
    def __init__(self):
        self.size = [screenWidth - int((COLS / 4) * TILESIZE), screenWidth]
        self.cols = int((self.size[1] - self.size[0]) / TILESIZE)

    def printMarginSize(self):
        return self.size

    def printMarginCols(self):
        return self.cols

class CenterMargin:
    def __init__(self) -> None:
        self.leftMargin = LeftMargin()
        self.rightMargin = RightMargin()

        self.sector = [self.leftMargin.size[1], self.rightMargin.size[0]]
        self.cols = int((self.sector[1] - self.sector[0]) / TILESIZE)

class Grid:
    def __init__(self) -> None:
        self.leftMargin = LeftMargin()
        self.rightMargin = RightMargin()
        self.centerMargin = CenterMargin()

    def pack(self, rect, x, y, sx, sy):
        self.rect = rect
        self.rect.x = screenWidth / 4
        self.rect.y = screenHeight / 4

        if x > 0 and sx == "+":
            self.rect.x += x
        if x > 0 and sx == "-":
            self.rect.x -= x
        if y > 0 and sy == "+":
            self.rect.y += y
        if y > 0 and sy == "-":
            self.rect.y -= y
        # if margin == "left" and (cols <= self.leftMargin.cols and rows <= ROWS):
        #     self.rect.x = float(cols * TILESIZE)
        #     self.rect.y = float(rows * TILESIZE)
        #     return self.rect.x, self.rect.y
        #
        # if margin == "right" and (cols <= self.rightMargin.cols and rows <= ROWS):
        #     self.rect.x = float(self.rightMargin.size[0] + (cols * TILESIZE))
        #     self.rect.y = float((rows * TILESIZE))
        #     return self.rect.x, self.rect.y
        #
        # if margin == "center" and (cols <= self.centerMargin.cols and rows <= ROWS):
        #     self.rect.x = float(self.leftMargin.size[1] + cols * TILESIZE)
        #     self.rect.y = float(rows * TILESIZE)
        #     return self.rect.x, self.rect.y
        
class Margins:
    def __init__(self) -> None:
        self.leftMarginEnd = int((COLS / 4) * TILESIZE)
        self.rightMarginEnd = screenWidth - int((COLS / 4) * TILESIZE)
        self.topMarginEnd = int((ROWS / 4) * TILESIZE)
        self.bottomMarginEnd = int((ROWS / 2) * TILESIZE) + int((ROWS / 4) * TILESIZE) - 16 
    # Currently Not Functional Margins. Just simply visual to see what is happening
    """Margins need to have a range of points that establish its area 
       Margins need to take their range and remove the rest of the screen from their coordinates
       so that way each margin has its own (1, 1). when calling widget.grid(4, 4, center)
       this places the widget in the center margin on column 4 and row 4"""
    def leftMargin(self): 
        for x in range(0, self.leftMarginEnd, TILESIZE):
            for y in range(0, screenHeight, TILESIZE):
                rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
                pygame.draw.rect(win, BLUE, rect, 1)
    
    def rightMargin(self):
        for x in range(self.rightMarginEnd, screenWidth, TILESIZE):
            for y in range(0, screenHeight, TILESIZE):
                rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
                pygame.draw.rect(win, RED, rect, 1)
    
    def topMargin(self):
        for x in range(self.leftMarginEnd, self.rightMarginEnd - 16, TILESIZE):
            for y in range(0, self.topMarginEnd, TILESIZE):
                rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
                pygame.draw.rect(win, WHITE, rect, 1)
    
    def bottomMargin(self):
        for x in reversed(range(self.leftMarginEnd, self.rightMarginEnd - 8, TILESIZE)):
            for y in range(self.bottomMarginEnd, screenHeight, TILESIZE):
                rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
                pygame.draw.rect(win, YELLOW, rect, 1)
    
    def centerMargin(self):
        for x in range(self.leftMarginEnd, self.rightMarginEnd - 8, TILESIZE):
            for y in range(self.topMarginEnd + 16, self.bottomMarginEnd - 16, TILESIZE):
                rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
                pygame.draw.rect(win, GREEN, rect, 1)
    
class Main():
    def __init__(self) -> None:
        self.margins = Margins()
        self.leftMargin = LeftMargin()
        self.rightMargin = RightMargin()

    def run(self):
        win.fill(BGCOLOR)
        self.margins.leftMargin()
        self.margins.rightMargin()
        self.margins.topMargin()
        self.margins.bottomMargin()
        self.margins.centerMargin()
        print(self.margins.rightMarginEnd)
        print(f"Left Size is {self.leftMargin.printMarginSize()}")
        print(f"Left Columns are {self.leftMargin.printMarginCols()}")

        print(f"Right Size is {self.rightMargin.printMarginSize()}")
        print(f"Right Columns are {self.rightMargin.printMarginCols()}")
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            pygame.display.update()

main = Main()
if __name__ == "__main__":
    main.run()
