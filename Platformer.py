import arcade 
from arcade import TileMap
import arcade.key
import arcade.key 

#physicsPlayer1
movement_speed = 8
jump_speed = 28
gravity = 1.1

#physicsPlayer1
movement_speed2 = 8
jump_speed2 = 28
gravity2 = 1.1

#maps
map_width = 128 * 30
map_height = 93 * 20
tile_width = 128

#window 
window_width = 1280
window_height = 896
window_half = 1280 // 2 


class GameWindow(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title,resizable=True)
        self.set_viewport(10,120,10,40)
        self.set_location(x=125,y=40)
        self.set_max_size(1280,720)

        
        
        arcade.set_background_color(arcade.color.BLACK)
        self.ground_list = None
        self.player_list = None
        self.player_sprite = None
        self.physics_engine = None

        self.original_angle = 0 
        self.setup()

    def setup(self):
        my_map = TileMap(r"untitled2.tmx", scaling=0.35)
    
        self.ground_list = my_map.sprite_lists["Tile Layer 1"]

        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(r"Player.png",0.15)
        self.player_sprite.center_x = 640 
        self.player_sprite.center_y = 357
        self.player_list.append(self.player_sprite)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,self.ground_list,gravity_constant=gravity)

        self.player_list2 = arcade.SpriteList()
        self.player_sprite2 = arcade.Sprite(r"Player2.png",0.13)
        self.player_sprite2.center_x = 620 
        self.player_sprite2.center_y = 357
        self.player_list2.append(self.player_sprite2)
        self.physics_engine2 = arcade.PhysicsEnginePlatformer(self.player_sprite2,self.ground_list,gravity_constant=gravity2)

    def on_draw(self):
        arcade.start_render()
        self.ground_list.draw()
        self.player_list.draw()
        self.player_list2.draw()
        arcade.draw_text(f"Testing text",start_x=0.0,start_y=0.0,italic=True,color=arcade.color.GOLD_FUSION,font_size=20)
    
    def clamp(self,value,mini,maxi):
        return max(min(value,maxi),mini)
    

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.physics_engine2.update()
        #self.player_sprite.update()

        self.player_sprite.center_x = self.clamp(self.player_sprite.center_x,0,map_width)
        self.player_sprite2.center_x = self.clamp(self.player_sprite2.center_x,0,map_width)

        if self.player_sprite.center_x > window_half and self.player_sprite.center_x < map_width - tile_width - window_half:
            change_view= True
        else:
            change_view = False
        if change_view:
            arcade.set_viewport(self.player_sprite.center_x-window_half,self.player_sprite.center_x+window_half,0,window_height)

        if self.player_sprite2.center_x > window_half and self.player_sprite2.center_x < map_width - tile_width - window_half:
            change_view= True
        else:
            change_view = False
        if change_view:
            arcade.set_viewport(self.player_sprite2.center_x-window_half,self.player_sprite2.center_x+window_half,0,window_height)
           
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player_sprite.change_x= movement_speed
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -movement_speed
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = jump_speed
        if symbol == arcade.key.RCTRL:
            self.player_sprite.angle = 90
        if symbol == arcade.key.D:
            self.player_sprite2.change_x= movement_speed2
        if symbol == arcade.key.A:
            self.player_sprite2.change_x = -movement_speed2
        if symbol == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite2.change_y = jump_speed2
        if symbol == arcade.key.C:
            self.player_sprite2.angle = 90
            
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 0 
        if symbol == arcade.key.RCTRL:
            self.player_sprite.angle= 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player_sprite2.change_x = 0
        if symbol == arcade.key.C:
            self.player_sprite2.angle= 0

            
    

GameWindow(map_width,map_height,'GameWindow')
arcade.run()