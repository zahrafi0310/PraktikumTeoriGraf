import pygame
import sys
import math

pygame.init()

BS, CS, MARGIN = 8, 70, 60
WIDTH, HEIGHT = BS * CS + 2 * MARGIN + 280, BS * CS + 2 * MARGIN
FPS = 60

BG_COLOR, L_SQ, D_SQ = (25, 20, 15), (240, 217, 181), (181, 136, 99)
SEL_COLOR, PATH_COLOR, TXT_COLOR = (173, 216, 230), (139, 90, 43), (255, 255, 255)
SUCC_COLOR, GRID_COLOR = (150, 190, 100), (100, 80, 60, 50)

class KnightsTour:
    def __init__(self):
        self.mx = [2, 1, -1, -2, -2, -1, 1, 2]
        self.my = [1, 2, 2, 1, -1, -2, -2, -1]
        self.path, self.board = [], []

    def is_valid(self, x, y):
        return 0 <= x < BS and 0 <= y < BS and self.board[x][y] == -1

    def get_deg(self, x, y):
        return sum(1 for i in range(8) if self.is_valid(x + self.mx[i], y + self.my[i]))

    def solve(self, sx, sy, cl=False):
        self.board = [[-1]*BS for _ in range(BS)]
        self.path = []
        return self._util(sx, sy, 0, sx, sy, cl)

    def _util(self, x, y, count, sx, sy, cl):
        self.board[x][y] = count
        self.path.append((x, y))
        
        if count == BS * BS - 1:
            if not cl: 
                return True
            can_return = any(x + self.mx[i] == sx and y + self.my[i] == sy for i in range(8))
            if not can_return:
                self.board[x][y] = -1
                self.path.pop()
                return False
            return True
        
        moves = []
        for i in range(8):
            nx, ny = x + self.mx[i], y + self.my[i]
            if self.is_valid(nx, ny): 
                moves.append((self.get_deg(nx, ny), nx, ny))
        moves.sort()
        
        for _, nx, ny in moves:
            if self._util(nx, ny, count + 1, sx, sy, cl): 
                return True
        
        self.board[x][y] = -1
        self.path.pop()
        return False

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.is_hovered = False

    def draw(self, screen, font):
        color = (110, 70, 35) if self.is_hovered else PATH_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        ts = font.render(self.text, True, TXT_COLOR)
        screen.blit(ts, ts.get_rect(center=self.rect.center))

class Visualizer:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Praktikum 1 - knight's tour")
        self.clock = pygame.time.Clock()
        self.f28 = pygame.font.Font(None, 28)
        self.f32 = pygame.font.Font(None, 32)
        self.f22 = pygame.font.Font(None, 22)
        self.kt = KnightsTour()
        self.start_pos = None
        self.solved = self.anim = False
        self.step = 0
        self.type = ""
        self.last_upd = 0
        
        bx = BS * CS + 2 * MARGIN + 25
        self.btns = {
            'op': Button(bx, 115, 220, 45, "Open Tour"),
            'cl': Button(bx, 170, 220, 45, "Closed Tour"),
            'vs': Button(bx, 240, 220, 45, "Visualisasi"),
            'rs': Button(bx, 295, 220, 45, "Reset")
        }

    def draw_arrow(self, p1, p2):
        angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
        pygame.draw.line(self.screen, PATH_COLOR, p1, p2, 2)
        al = 10
        pt1 = (p2[0] - al * math.cos(angle - 0.5), p2[1] - al * math.sin(angle - 0.5))
        pt2 = (p2[0] - al * math.cos(angle + 0.5), p2[1] - al * math.sin(angle + 0.5))
        pygame.draw.polygon(self.screen, PATH_COLOR, [p2, pt1, pt2])

    def draw(self):
        self.screen.fill(BG_COLOR)
        for r in range(BS):
            for c in range(BS):
                rect = pygame.Rect(MARGIN + c * CS, MARGIN + r * CS, CS, CS)
                color = SEL_COLOR if self.start_pos == (r, c) and not self.anim and self.step == 0 else (L_SQ if (r + c) % 2 == 0 else D_SQ)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, 1)

        if self.step >= 2:
            for i in range(min(self.step - 1, len(self.kt.path) - 1)):
                r1, c1 = self.kt.path[i]; r2, c2 = self.kt.path[i+1]
                p1 = (MARGIN + c1 * CS + CS // 2, MARGIN + r1 * CS + CS // 2)
                p2 = (MARGIN + c2 * CS + CS // 2, MARGIN + r2 * CS + CS // 2)
                self.draw_arrow(p1, p2)
            if self.type == "Closed Tour" and self.step == BS*BS:
                p1 = (MARGIN + self.kt.path[-1][1]*CS+CS//2, MARGIN + self.kt.path[-1][0]*CS+CS//2)
                p2 = (MARGIN + self.kt.path[0][1]*CS+CS//2, MARGIN + self.kt.path[0][0]*CS+CS//2)
                self.draw_arrow(p1, p2)

        if self.step > 0:
            for i, (r, c) in enumerate(self.kt.path[:self.step]):
                ts = self.f22.render(str(i+1), True, (30, 30, 30))
                self.screen.blit(ts, ts.get_rect(center=(MARGIN + c * CS + CS // 2, MARGIN + r * CS + CS // 2)))

        bx = BS * CS + 2 * MARGIN + 20
        if not self.solved:
            txt = "Pilih titik awal" if not self.start_pos else "Titik awal terpilih"
            self.screen.blit(self.f28.render(txt, True, TXT_COLOR), (bx, 40))
        else:
            self.screen.blit(self.f32.render(self.type, True, TXT_COLOR), (bx, 30))
            self.screen.blit(self.f28.render("Solved: 64 kotak", True, SUCC_COLOR), (bx, 65))

        mp = pygame.mouse.get_pos()
        for b in self.btns.values():
            b.is_hovered = b.rect.collidepoint(mp)
            b.draw(self.screen, self.f28)
        pygame.display.flip()

    def run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: return pygame.quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = e.pos
                    if not self.solved:
                        br = pygame.Rect(MARGIN, MARGIN, BS * CS, BS * CS)
                        if br.collidepoint(mx, my): 
                            self.start_pos = ((my - MARGIN) // CS, (mx - MARGIN) // CS)
                    
                    if self.btns['rs'].is_hovered:
                        self.solved = self.anim = False
                        self.step, self.type, self.start_pos, self.kt.path = 0, "", None, []
                    elif self.start_pos:
                        if self.btns['op'].is_hovered: 
                            self.type, self.solved = "Open Tour", self.kt.solve(*self.start_pos, False)
                        if self.btns['cl'].is_hovered: 
                            self.type, self.solved = "Closed Tour", self.kt.solve(*self.start_pos, True)
                        if self.btns['vs'].is_hovered and self.solved: 
                            self.anim, self.step = True, 0

            if self.anim and pygame.time.get_ticks() - self.last_upd > 1000 // 10:
                self.step += 1
                self.last_upd = pygame.time.get_ticks()
                if self.step > len(self.kt.path): 
                    self.anim = False
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    Visualizer().run()