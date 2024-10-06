class Camera:
    def __init__(self,sensor,mp):
        self.sensor = sensor
        self.mp = mp
    
class Keyboard:
    def __init__(self,keys,light):
        self.keys = keys
        self.light = light

class Screen:
    def __init__(self,size,resolution,type):
        self.size = size
        self.resolution = resolution
        self.type = type

class Laptop:
    logo_name = "lenovo"
    def __init__(self,name,camera,keyboard,screen):
        self.name = name
        self.camera = camera
        self.keyboard = keyboard
        self.screen = screen

    def __str__(self):
        return f"model:{self.name}, \n\t Camera:(sensor:{self.camera.sensor},mp:{self.camera.mp}),\n\t keyboard:(keys:{self.keyboard.keys}, light:{self.keyboard.light}, \n\t Screen:(size:{self.screen.size}, resolution:{self.screen.resolution}, type:{self.screen.type}))"


camera1=Camera("sony","64")
keyboard1=Keyboard("mechanical","rgb")
screen1=Screen("16inch","1080","oled")

Laptop1=Laptop("ROG",camera1,keyboard1,screen1)
print(Laptop1)


