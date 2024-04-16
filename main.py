import pygame as pg
import sys
from sound_handler import SoundHandler


class App:
    def __init__(self):
        pg.init()
        self.win_size = (800, 800)
        self.win = pg.display.set_mode(self.win_size)
        self.clock = pg.Clock()
        self.sound = SoundHandler()

        self.timer = 0
        self.play = True

    def draw(self):
        self.win.fill((15, 15, 15))
                
        pg.display.flip()

    def update(self):
        self.draw ()

    def start(self):
        MUSIC_END = pg.USEREVENT+1
        while True:
            self.dt = self.clock.tick()/1000
            self.timer += self.dt
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT: 
                        self.sound.fast_forward()
                    if event.key == pg.K_UP:
                        self.sound.play_track('Dungeon')
                    if event.key == pg.K_DOWN:
                        self.sound.play_track('Shop')
                    if event.key == pg.K_LEFT:
                        self.sound.play_playlist("Example_Playlist")
                    if event.key == pg.K_SPACE:
                        self.sound.play_sound("jump")
                if event.type == MUSIC_END:
                    self.sound.update_playlist()

            self.update()

if __name__ == '__main__':
    app = App()
    app.start()