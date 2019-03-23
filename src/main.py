import os, sys
cwd = os.getcwd()
sys.path.append(cwd + "/GameEngine/Engine")
from Engine import Engine, EngineInit
from MainMenu import MainMenu

class Main(EngineInit):

    def startWorld(self, ex):
        return MainMenu(ex)

if __name__ == "__main__":
    main = Main()
    Engine.start(main)
