from pico2d import *


CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_WIDTH, FRAME_HEIGHT = 100, 100
CHARACTER_SHEET_FILE = 'animation_sheet.png'


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image(CHARACTER_SHEET_FILE)


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
running = True
x, y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
frame = 0
dir = 0 # 정지 상태

# fill here
while running:
    clear_canvas()
    background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_WIDTH, 100, FRAME_WIDTH, FRAME_HEIGHT, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)

close_canvas()

