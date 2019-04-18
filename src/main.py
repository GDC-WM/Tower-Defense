import os, sys
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from Engine import Engine, EngineInit
from MainMenu import MainMenu

class Main(EngineInit):

    def __init__(self, world):
        self.world = world

    def startWorld(self, ex):
        return self.world(ex)

if __name__ == "__main__":
    world = MainMenu

    for i in range(1, len(sys.argv[1:])):
        if sys.argv[i] == "-w":
            i+=1
            world = eval(sys.argv[i])
        
        elif sys.argv[i] == "-l":
            i+=1
            world = Level(int(sys.argv[i]))

    Engine.start(Main(world))
