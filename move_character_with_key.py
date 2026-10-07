from pico2d import *


CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_WIDTH, FRAME_HEIGHT = 100, 100
MOVE_SPEED = 5
CHARACTER_SHEET_FILE = 'animation_sheet.png'


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image(CHARACTER_SHEET_FILE)
key_state = {
    SDLK_RIGHT: False,
    SDLK_LEFT: False,
    SDLK_UP: False,
    SDLK_DOWN: False,
}


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in key_state:
                key_state[event.key] = True
        elif event.type == SDL_KEYUP and event.key in key_state:
            key_state[event.key] = False
running = True
x, y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
frame = 0

# fill here
while running:
    clear_canvas()
    background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_WIDTH, 100, FRAME_WIDTH, FRAME_HEIGHT, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if key_state[SDLK_RIGHT]:
        x += MOVE_SPEED
    if key_state[SDLK_LEFT]:
        x -= MOVE_SPEED
    delay(0.05)

close_canvas()

