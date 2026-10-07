from pico2d import *


CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_WIDTH, FRAME_HEIGHT = 100, 100
FRAME_COUNT = 8
FRAME_DELAY = 0.05
MOVE_SPEED = 5
MIN_X, MAX_X = FRAME_WIDTH // 2, CANVAS_WIDTH - FRAME_WIDTH // 2
MIN_Y, MAX_Y = FRAME_HEIGHT // 2, CANVAS_HEIGHT - FRAME_HEIGHT // 2
CHARACTER_SHEET_FILE = 'animation_sheet.png'
FACE_RIGHT = 'right'
FACE_LEFT = 'left'
STATE_IDLE = 'IDLE'
STATE_MOVE = 'MOVE'
IDLE_RIGHT_Y = 300
IDLE_LEFT_Y = 200
MOVE_RIGHT_Y = 100
MOVE_LEFT_Y = 0


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
            return
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
                return
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
    if state == STATE_IDLE:
        row_y = IDLE_RIGHT_Y if facing == FACE_RIGHT else IDLE_LEFT_Y
    else:
        row_y = MOVE_RIGHT_Y if facing == FACE_RIGHT else MOVE_LEFT_Y
    character.clip_draw(frame * FRAME_WIDTH, row_y, FRAME_WIDTH, FRAME_HEIGHT, x, y)
    update_canvas()
    handle_events()
    if not running:
        break
    frame = (frame + 1) % FRAME_COUNT
    old_x, old_y = x, y
    horizontal = int(key_state[SDLK_RIGHT]) - int(key_state[SDLK_LEFT])
    vertical = int(key_state[SDLK_UP]) - int(key_state[SDLK_DOWN])
    x += horizontal * MOVE_SPEED
    y += vertical * MOVE_SPEED
    x = max(MIN_X, min(MAX_X, x))
    y = max(MIN_Y, min(MAX_Y, y))
    state = STATE_MOVE if x != old_x or y != old_y else STATE_IDLE
    delay(FRAME_DELAY)

close_canvas()

