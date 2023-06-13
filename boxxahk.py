import logging
import pygame
from JoycontrolPlugin import JoycontrolPlugin
logger = logging.getLogger(__name__)
pygame.init()
joystick = None
clock = pygame.time.Clock()
class boxxahk(JoycontrolPlugin):
    async def run(self):
        logger.info('boxxahk joycontrol plugin starting up...')
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        logger.info('joystick found')
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                d = event.__dict__
                if event.type == 1536:
                    logger.info('stick')
                    if abs(d['value']) < 0.01:
                        d['value'] = 0
                    if d['axis'] == 0: await self.stick2('left', 'horizontal', d['value'])
                    elif d['axis'] == 1: await self.stick2('left', 'vertical', d['value'])
                    elif d['axis'] == 3: await self.stick2('right', 'horizontal', d['value'])
                    elif d['axis'] == 4: await self.stick2('right', 'vertical', d['value'])
                elif event.type == 1539:
                    logger.info('press')
                    if d['button'] == 0: await self.button_press('l')
                    elif d['button'] == 1: await self.button_press('y')
                    elif d['button'] == 2: await self.button_press('r')
                    elif d['button'] == 3: await self.button_press('b')
                    elif d['button'] == 4: await self.button_press('a')
                    elif d['button'] == 5: await self.button_press('x')
                    elif d['button'] == 6: await self.button_press('zr')
                    elif d['button'] == 7: await self.button_press('plus')
                elif event.type == 1540:
                    logger.info('release')
                    if d['button'] == 0: await self.button_release('l')
                    elif d['button'] == 1: await self.button_release('y')
                    elif d['button'] == 2: await self.button_release('r')
                    elif d['button'] == 3: await self.button_release('b')
                    elif d['button'] == 4: await self.button_release('a')
                    elif d['button'] == 5: await self.button_release('x')
                    elif d['button'] == 6: await self.button_release('zr')
                    elif d['button'] == 7: await self.button_release('plus')
