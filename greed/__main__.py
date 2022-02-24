from game.participants.entity import Entity
from game.participants.participants import Participants

from game.director.director import Director

from game.services.movement import Movement
from game.services.graphics import Graphics
from game.services.waterfall import Waterfall

from game.common.color import Color
from game.common.location import Location

FRAME_RATE = 10
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = MAX_X / CELL_SIZE
ROWS = MAX_Y / CELL_SIZE
CAPTION = "Greed Game - CSE 210"
WHITE = Color(255, 255, 255)

def main():
    # create the participants
    participants = Participants()

    # create the banner
    banner = Entity()
    banner.set_text("Score: 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Location(CELL_SIZE, 0))
    participants.add_participant("banners", banner)

    # create the excavator
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE * 3)
    position = Location(x, y)

    excavator = Entity()
    excavator.set_text("#")
    excavator.set_font_size(FONT_SIZE)
    excavator.set_color(WHITE)
    excavator.set_position(position)
    participants.add_participant("excavators", excavator)
    
    # start the game
    movement = Movement(CELL_SIZE)
    graphics = Graphics(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    waterfall = Waterfall(COLS, MAX_Y, CELL_SIZE, FONT_SIZE)
    director = Director(movement, graphics, waterfall)
    director.start_game(participants)

if __name__ == "__main__":
    main()