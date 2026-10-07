from pico2d import *


CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_WIDTH, FRAME_HEIGHT = 100, 100
MOVE_SPEED = 5
CHARACTER_SHEET_FILE = 'animation_sheet.png'
FACE_RIGHT = 'right'
FACE_LEFT = 'left'
STATE_IDLE = 'IDLE'
STATE_MOVE = 'MOVE'
IDLE_RIGHT_Y = 300
IDLE_LEFT_Y = 200


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
    global running, facing

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in key_state:
                key_state[event.key] = True
                # Up/down movement keeps the existing left/right facing direction.
                if event.key == SDLK_RIGHT:
                    facing = FACE_RIGHT
                elif event.key == SDLK_LEFT:
                    facing = FACE_LEFT
        elif event.type == SDL_KEYUP and event.key in key_state:
            key_state[event.key] = False
            if event.key == SDLK_RIGHT and key_state[SDLK_LEFT]:
                facing = FACE_LEFT
            elif event.key == SDLK_LEFT and key_state[SDLK_RIGHT]:
                facing = FACE_RIGHT
running = True
x, y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
frame = 0
facing = FACE_RIGHT
state = STATE_IDLE

# fill here
while running:
    clear_canvas()
    background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    row_y = 100
    if state == STATE_IDLE:
        row_y = IDLE_RIGHT_Y if facing == FACE_RIGHT else IDLE_LEFT_Y
    character.clip_draw(frame * FRAME_WIDTH, row_y, FRAME_WIDTH, FRAME_HEIGHT, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    horizontal = int(key_state[SDLK_RIGHT]) - int(key_state[SDLK_LEFT])
    vertical = int(key_state[SDLK_UP]) - int(key_state[SDLK_DOWN])
    x += horizontal * MOVE_SPEED
    y += vertical * MOVE_SPEED
    state = STATE_MOVE if horizontal != 0 or vertical != 0 else STATE_IDLE
    delay(0.05)

close_canvas()

