  # Welcome to
  # __________         __    __  .__                               __
  # \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
  #  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
  #  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
  #  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
  #
  # This file can be a nice home for your Battlesnake logic and helper functions.
  #
  # To get you started we've included code to prevent your Battlesnake from moving backwards.
  # For more info see docs.battlesnake.com
  
  import random
  import typing
  
  
  # info is called when you create your Battlesnake on play.battlesnake.com
  # and controls your Battlesnake's appearance
  # TIP: If you open your Battlesnake URL in a browser you should see this data
  def info() -> typing.Dict:
    print("INFO")
  
    return {
      "apiversion": "1",
      "author": "Zapier Sidewinders",  # TODO: Your Battlesnake Username
      "color": "#F28500",  # TODO: Choose color
      "head": "default",  # TODO: Choose head
      "tail": "curled",  # TODO: Choose tail
    }
  
  
  # start is called when your Battlesnake begins a game
  def start(game_state: typing.Dict):
    print("GAME START")
  
  
  # end is called when your Battlesnake finishes a game
  def end(game_state: typing.Dict):
    print("GAME OVER\n")
  
  
  # move is called on every turn and returns your next move
  # Valid moves are "up", "down", "left", or "right"
  # See https://docs.battlesnake.com/api/example-move for available data
  def move(game_state: typing.Dict) -> typing.Dict:
  
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}
  
    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"
  
    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
      is_move_safe["left"] = False
  
    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
      is_move_safe["right"] = False
  
    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
      is_move_safe["down"] = False
  
    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
      is_move_safe["up"] = False
  
    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    board_width = game_state['board']['width'] - 1
    board_height = game_state['board']['height'] - 1
  
    if my_head["y"] == board_height:
      is_move_safe["up"] = False
  
    if my_head["y"] == 0:
      is_move_safe["down"] = False
  
    print(f"My Head X: {my_head['x']}")
    print(f"My Head Y: {my_head['y']}")
    print(f"Board Width: {board_width}")
    print(f"Board Height: {board_height}")
    if my_head["x"] == board_width:
      is_move_safe["right"] = False
  
    if my_head["x"] == 0:
      is_move_safe["left"] = False
  
    # # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    my_body = game_state['you']['body']
    print(f"My body: {my_body}")
    for snake in game_state["board"]["snakes"]:
      for body in snake["body"]:
        print(body)
        if body['x'] == my_head['x'] - 1 and body['y'] == my_head['y']:
           is_move_safe["left"] = False
        if body['x'] == my_head['x'] + 1 and body['y'] == my_head['y']:
           is_move_safe["right"] = False
        if body['y'] == my_head['y'] + 1 and body['x'] == my_head['x']:
           is_move_safe["up"] = False
        if body['y'] == my_head['y'] - 1 and body['x'] == my_head['x']:
           is_move_safe["down"] = False
        # if body['x'] == my_head['x']:
        #   is_move_safe["right"] = False
        # if body['y'] == my_head['y'] + 1:
        #   is_move_safe["up"] = False
        # if body['y'] == my_head['y'] - 1:
        #   is_move_safe["down"] = False
  
    #print(f"Snake: {snake}")
  
    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    # opponents = game_state['board']['snakes']
  
    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
      if isSafe:
        safe_moves.append(move)
  
    print(safe_moves)
    if len(safe_moves) == 0:
      print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
      return {"move": "down"}
  
    # Choose a random move from the safe ones
    
  
    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    next_move = ""
    foods = game_state['board']['food']
    #print(foods)
    #print("food")
    #print(foods[0])
    for food in foods:
      if(food["x"] == my_head['x'] - 1 and food['y'] == my_head['y'] and is_move_safe['right']):
        next_move = "right"
      if(food['x'] == my_head['x'] + 1 and food['y'] == my_head['y'] and is_move_safe['left']):
        next_move = "left"
      if(food['x'] == my_head['x'] and food['y'] == my_head['y'] -1 and is_move_safe['down']):
        next_move = "down"
      if(food["x"] == my_head['x'] and food['y'] == my_head['y'] +1 and is_move_safe['up']):
        next_move = "up"
      
    if(next_move == ""):
      next_move = random.choice(safe_moves)
    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}
  
  
  # Start server when `python main.py` is run
  if __name__ == "__main__":
    from server import run_server
  
    run_server({"info": info, "start": start, "move": move, "end": end})
  