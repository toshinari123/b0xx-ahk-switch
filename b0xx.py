import logging
import pygame
import copy
from JoycontrolPlugin import JoycontrolPlugin
logger = logging.getLogger(__name__)
pygame.init()
display = pygame.display.set_mode((300, 300))
stickscancode = [23, 28, 13, 87, 44, 230]
cstickscancode = [79, 80, 229, 82]
buttonscancode = [29, 9, 95, 81, 92, 96, 97]
stick, cstick, scale, cscale = [], [], 1, 1
scancodedict = {23: 'left', 28: 'down', 13: 'right', 87: 'up', 44: 'modx', 230: 'mody', \
    79: 'up', 80: 'down', 229: 'left', 82: 'right', \
    29: 'plus', 9: 'l', 95: 'r', 81: 'a', 92: 'b', 96: 'x', 97: 'zr'}
clock = pygame.time.Clock()

def clean(state, a, b):
    if a in state and b in state:
        if state.index(a) < state.index(b):
            state.remove(b)
        else:
            state.remove(a)
    return state

def calculatestick(stick):
    state = copy.deepcopy(clean(clean(clean(copy.deepcopy(stick), 'left', 'right'), 'up', 'down'), 'modx', 'mody'))
    xrefl, yrefl, x, y = False, False, 0, 0
    if 'left' in state:
        xrefl = True
        state[state.index('left')] = 'right'
    if 'up' in state:
        yrefl = True
        state[state.index('up')] = 'down'
    if 'right' in state:
        if 'down' in state:
            if 'modx' in state:
                x, y = 0.7375, 0.3125
            elif 'mody' in state:
                x, y = 0.3125, 0.7375
            else:
                x, y = 0.7, 0.7
        else:
            if 'modx' in state:
                x, y = 0.6625, 0
            elif 'mody' in state:
                x, y = 0.3375, 0
            else:
                x, y = 1, 0
    else:
        if 'down' in state:
            if 'modx' in state:
                x, y = 0, 0.5375
            elif 'mody' in state:
                x, y = 0, 0.7375
            else:
                x, y = 0, 1
    if xrefl:
        x = -x
    if yrefl:
        y = -y
    return x, y

class boxxahk(JoycontrolPlugin):
    async def run(self):
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == 768:
                    print(event)
                    d = event.__dict__
                    if d['scancode'] in stickscancode:
                        stick.append(scancodedict[d['scancode']])
                        x, y = calculatestick(stick)
                        print(f'stick {x} {y}')
                        await self.stick2('left', 'horizontal', x * scale)
                        await self.stick2('left', 'vertical', y * scale)
                    elif d['scancode'] in cstickscancode:
                        cstick.append(scancodedict[d['scancode']])
                        x, y = calculatestick(cstick)
                        print(f'cstick {x} {y}')
                        await self.stick2('right', 'horizontal', x * cscale)
                        await self.stick2('right', 'vertical', y * cscale)
                    elif d['scancode'] in buttonscancode:
                        print(f'button press {scancodedict[d["scancode"]]}')
                        await self.button_press(scancodedict[d['scancode']])
                elif event.type == 769:
                    print(event)
                    d = event.__dict__
                    if d['scancode'] in stickscancode:
                        stick.remove(scancodedict[d['scancode']])
                        x, y = calculatestick(stick)
                        print(f'stick {x} {y}')
                        await self.stick2('left', 'horizontal', x * scale)
                        await self.stick2('left', 'vertical', y * scale)
                    elif d['scancode'] in cstickscancode:
                        cstick.remove(scancodedict[d['scancode']])
                        x, y = calculatestick(cstick)
                        print(f'cstick {x} {y}')
                        await self.stick2('right', 'horizontal', x * cscale)
                        await self.stick2('right', 'vertical', y * cscale)
                    elif d['scancode'] in buttonscancode:
                        print(f'button release {scancodedict[d["scancode"]]}')
                        await self.button_release(scancodedict[d['scancode']])
