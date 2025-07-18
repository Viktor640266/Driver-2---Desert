import random
import time
from driver import Driver

class Desert(Driver):
    def __init__(self):
        super().__init__()
        self.world = [['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'],
                      ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m']]
        self.dragon = [['\x1b[38;5;21;48;5;21m / \x1b[0m', '\x1b[38;5;226;48;5;0m . \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;226;48;5;0m . \x1b[0m', '\x1b[38;5;21;48;5;21m \\ \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;8;48;5;15m | \x1b[0m', '\x1b[38;5;0;48;5;9m = \x1b[0m', '\x1b[38;5;21;48;5;21m | \x1b[0m'], 
                       ['\x1b[38;5;21;48;5;21m \\ \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m - \x1b[0m', '\x1b[38;5;21;48;5;21m / \x1b[0m']]
        self.spider =  [['\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;226;48;5;226m - \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m . \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;226;48;5;226m - \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m'], 
                        ['\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m'], 
                        ['\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m'], 
                        ['\x1b[38;5;196;48;5;196m = \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m', '\x1b[38;5;0;48;5;0m . \x1b[0m']]
        self.values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.all_values = []
        for a in range(len(self.values)):
            index = random.randint(0, len(self.values) - 1)
            self.all_values.append(self.values[index])
            self.values.remove(self.values[index])
        self.actions = ["water -= 10", "self.thunder = 1", "truck_hp -= 2", "self.world = self.dragon", "cargo_hp -= 2", "fuel -= 2", "self.world = self.spider", "self.energy -= 10", "bottles -= 2"]
        if time.localtime().tm_hour < 7 or time.localtime().tm_hour > 21:
            self.actions.append("self.temp -= 5")
        else:
            self.actions.append("self.temp += 10")
        self.flat = [226, 11]
        self.day = [51, 21, 51]
        self.night = [13, 12, 0]
        self.temp = 0
        self.thunder = 0
        self.km = 0
    def desertgame(self):
        force_counter = 0
        start_world = self.world
        bottle = random.randint(1, 50)
        real_km = 0
        truck_hp = 100
        cargo_hp = 100
        bottles = 20
        water = 100
        height = 4
        fuel = 100
        value = 2
        parameters = [self.temp, self.thunder, self.energy, truck_hp, cargo_hp, height, water, bottles]
        player_coords = [height, 0]
        daytime = "night"
        if time.localtime().tm_hour < 7 or time.localtime().tm_hour > 21:
            daytime = "night"
        else:
            daytime = "day"
        while True:
            if self.km % 10 == 0:
                height = random.randint(3, len(self.world) - 1)
                if self.thunder == 1:
                    self.thunder = 0
                randparam = random.randint(0, len(parameters)- 1) 
                if self.km >= 10:
                    for g in range(len(self.all_values)): 
                        if abs(self.all_values[g] - parameters[randparam]) < 10:
                            value = g
                            break
                    exec(self.actions[value])
            if self.km % 50 == 0:
                bottle = random.randint(1, 50)
                real_km = 0
            if real_km == bottle:
                print("\nYou found a bottle of water!!!!!\nВы нашли бутылку воды!!!!!\n")
                bottles += 1
            if self.world != self.dragon and self.world != self.spider:
                for i in range(len(self.world)):
                    for j in range(len(self.world[i])):
                        randsand = random.randint(0, 1)
                        randsky = random.randint(0, 2)
                        if i < height:
                            if daytime == "night":  
                                self.world[i][j] = f'\x1b[38;5;226;48;5;{self.night[randsky]}m * \x1b[0m'
                            else:
                                self.world[i][j] = f'\x1b[38;5;226;48;5;{self.day[randsky]}m - \x1b[0m'
                        else:
                            self.world[i][j] = f'\x1b[38;5;226;48;5;{self.flat[randsand]}m . \x1b[0m'
            if self.thunder == 0 and fuel > 0 and self.world != self.spider and self.world != self.dragon:
                self.player = f'\x1b[38;5;196;48;5;196m U \x1b[0m'
                what = input("If right - d. If left - a. Forward - w. Back - s.\nНаправо - d. Налево - a. Вперёд - w. Назад - s.\n")
                if what != "s" and what != "S" and what != "drink":
                    if player_coords[1] < 8:
                        player_coords[1] += 1
                        randsand = random.randint(0, 1)
                        self.world[player_coords[0]][player_coords[1] - 1] = f'\x1b[38;5;226;48;5;{self.flat[randsand]}m . \x1b[0m'
                    else:
                        player_coords[1] = 0
                    self.km += 1
                    real_km += 1
                elif what == "drink":
                    water += 5
                    bottles -= 1
                else:
                    if player_coords[1] > 1:
                        player_coords[1] -= 1
                        self.world[player_coords[0]][player_coords[1] + 1] = f'\x1b[38;5;226;48;5;{self.flat[randsand]}m . \x1b[0m'
                    else:
                        player_coords[1] = 0
                    self.km -= 1
            player_coords[0] = height
            if self.thunder == 1 and fuel > 0:
                if self.km % 10 <= 9:
                    for w in range(len(self.world)):
                        for q in range(len(self.world[w])):
                            if w < height:
                                randsand = random.randint(0, 1)
                                self.world[w][q] = f'\x1b[38;5;226;48;5;{self.flat[randsand]}m . \x1b[0m'
                    self.player = f'\x1b[38;5;226;48;5;{self.flat[randsand]}m . \x1b[0m'
                    t1 = time.perf_counter()
                    drive = input("IT`S SAND THUNDER! DRIVE FASTER!\nПЕСЧАНАЯ БУРЯ! НУЖНО ПРОРВАТЬСЯ! БЫСТРЕЙ ВПЕРЁД!\n")
                    t2 = time.perf_counter()
                    if drive != "s" and drive != "S" and drive != "drink" and t2 - t1 < 0.3:
                        self.km += 1
                    elif drive == "drink":
                        water += 5
                        bottles -= 1
                    else:
                        self.km -= int(t2 - t1)
                        cargo_hp -= 5
                        truck_hp -= 5
            if self.world != self.spider and self.world != self.dragon:
                self.world[player_coords[0]][player_coords[1]] = self.player
            if self.world == self.dragon:
                print("Hello, trucker...\nПривет, дальнобойщик...\n")
                dragon_hp = 100
                player_hp = 100
                dragon_energy = 20
                player_energy = 10
                while True:
                    if dragon_energy > 10:
                        move = input("The dragon attacks you! Say something to strike back\nДракон атакует! Напишите что-нибудь чтобы атаковать в ответ.\n")
                        dragon_energy -= 5
                        player_hp -= random.randint(1, 25)
                    else:
                        move = input("The dragon is preparing for the next attack...Say something to attack.\nДракон готовится к следующей атаке...Скажите что-нибудь чтобы атаковать.\n")
                        dragon_energy += 5
                    if move != "" and player_energy > 0:
                        if move == "drink":
                            water += 5
                            bottles -= 1
                            player_hp += 10
                        else:
                            print("You attacked back.")
                            dragon_hp -= random.randint(1, 25)
                            player_energy -= 5
                    if player_energy <= 0:
                        move = input("The dragon attacks you! Say something to defend\nДракон атакует! Напишите что-нибудь чтобы защититься.\n")
                        if move != "":
                            if move == "drink":
                                water += 5
                                bottles -= 1
                                player_hp += 10
                            else:
                                luck = random.randint(1, 3)
                                if luck == 2:
                                    print("You partially blocked the attack\nВы частично заблокировали атаку\n")
                                    player_hp -= random.randint(1, 10)
                                else:
                                    print("You are too tired to block the attack\n")
                                    player_hp -= random.randint(1, 25)
                            player_energy += 5
                    if player_hp <= 0 or dragon_hp <= 0:
                        if player_hp <= 0:
                            print("Game over. The dragon is won.\nИгра окончена. Дракон победил.\n")
                        else:
                            print("The dragon defended 100 units of fuel. You took it and refueled the truck.\nДракон защищал 100 единиц топлива. Вы взяли топливо и заправили машину.\n")
                            fuel += 100
                        cargo_hp = player_hp
                        self.world = start_world
                        break
                    for row in self.dragon:
                        print("".join(row))
                    print("Dragon HP\Здоровье дракона:", dragon_hp)
                    print("Dragon energy\Энергия дракона:", dragon_energy)
                    print("Player HP\Здоровье игрока:", player_hp)
                    print("Player energy\Энергия игрока:", player_energy)
            if self.world == self.spider:
                print("Hello, trucker...\nПривет, дальнобойщик...\n")
                spider_hp = 75
                player_hp = 100
                spider_energy = 40
                player_energy = 10
                while True:
                    if spider_energy > 10:
                        move = input("The spider attacks you! Say something to strike back\nПаук атакует! Напишите что-нибудь чтобы атаковать в ответ.\n")
                        spider_energy -= 5
                        player_hp -= random.randint(1, 25)
                    else:
                        move = input("The spider is preparing for the next attack...Say something to attack.\nПаук готовится к следующей атаке...Скажите что-нибудь чтобы атаковать.\n")
                        spider_energy += 10
                    if move != "" and player_energy > 0:
                        if move == "drink":
                            water += 5
                            bottles -= 1
                            player_hp += 10
                        else:
                            print("You attacked back.")
                            spider_hp -= random.randint(1, 25)
                            player_energy -= 5
                    if player_energy < 10:
                        move = input("The spider attacks you! Say something to defend\nПаук атакует! Напишите что-нибудь чтобы защититься.\n")
                        if move != "":
                            if move == "drink":
                                water += 5
                                bottles -= 1
                                player_hp += 10
                            else:
                                luck = random.randint(1, 3)
                                if luck == 2:
                                    print("You partially blocked the attack\nВы частично заблокировали атаку\n")
                                    player_hp -= random.randint(1, 10)
                                else:
                                    print("You are too tired to block the attack")
                                    player_hp -= random.randint(1, 25)
                                player_energy += 5
                    if player_hp <= 0 or spider_hp <= 0:
                        if player_hp <= 0:
                            print("Game over. The spider is won.\nИгра окончена. Паук победил.\n")
                        else:
                            print("You won.\nВы победили.\n")
                            print("The spider defended 100 units of fuel. You took it and refueled the truck.\nПаук защищал 100 единиц топлива. Вы взяли топливо и заправили машину.\n")
                            fuel += 100
                        cargo_hp = player_hp
                        self.world = start_world
                        break
                    for row in self.world:
                        print("".join(row))
                    print("Spider HP\Здоровье паука:", spider_hp)
                    print("Spider energy\Энергия паука:", spider_energy)
                    print("Player HP\Здоровье игрока:", player_hp)
                    print("Player energy\Энергия игрока:", player_energy)
            if cargo_hp <= 0:
                print("Game over.\nИгра окончена.")
                break
            if 0 <= self.temp <= 50 or -50 < self.temp <= 0:
                self.energy -= 2
                water -= 1
            elif self.temp > 50:
                cool = input("The cargo and the truck are need cooling... It takes 2 minutes. If you agree, say something. Else, skip.\nВам нужно охладить груз и машину... Это займёт 2 минуты. Если вы согласны, скажите что-нибудь. Если нет, пропустите.\n")
                self.energy -= self.temp / 10
                cargo_hp -= 2
                water -= 3
                if cool != "":
                    colors = [15, 21]
                    for c in range(len(self.world)):
                        for o in range(len(self.world[c])):
                            cooling = random.randint(0, 1)
                            self.world[c][o] = f'\x1b[38;5;226;48;5;{colors[cooling]}m * \x1b[0m'
                            for row in self.world:
                                print("".join(row))
                            time.sleep(1.2)
                    cargo_hp += 10
                    self.temp -= 25
            else:
                heat = input("The cargo and the truck are need heating... It takes 2 minutes. If you agree, say something. Else, skip.\nВам нужно согреть груз и машину... Это займёт 2 минуты. Если вы согласны, скажите что-нибудь. Если нет, пропустите.\n")
                self.energy += self.temp / 10
                cargo_hp -= 2
                water -= 1
                if heat != "":
                    colors = [202, 196]
                    for c in range(len(self.world)):
                        for o in range(len(self.world[c])):
                            heating = random.randint(0, 1)
                            self.world[c][o] = f'\x1b[38;5;226;48;5;{colors[heating]}m * \x1b[0m'
                            for row in self.world:
                                print("".join(row))
                            time.sleep(1.2)
                    cargo_hp += 10
                    self.temp += 30
            if daytime == "night":
                self.temp -= random.randint(0, 3)
            else:
                self.temp += random.randint(0, 3)
            fuel -= 1
            if water < 20:
                self.energy -= 5
            if fuel <= 0:
                fuel = 0
                tf_1 = time.perf_counter()
                for z in range(7):
                    force = input("Press 'w' + 'Enter' fast to move the truck\nПишите 'w' + 'Enter' быстро чтобы сдвинуть машину\n")
                    if force == "w" or force == "W":
                        force_counter += 1
                    for row in self.world:
                        print("".join(row))
                tf_2 = time.perf_counter()
                if self.thunder == 0:
                    if tf_2 - tf_1 <= 3 and force_counter >= 6:
                        if player_coords[1] <= 8:
                            player_coords[1] += 1
                        else:
                            player_coords[1] = 0
                        self.km += 1
                        real_km += 1
                if self.thunder == 1 and force_counter == 7:
                    if tf_2 - tf_1 <= 2:
                        if player_coords[1] <= 7:
                            player_coords[1] += 1
                        else:
                            player_coords[1] = 0
                        self.km += 1
                        real_km += 1
                if player_coords[1] <= 8:
                    self.world[player_coords[0]][player_coords[1] + 1] = self.player
                self.energy -= 2
            if self.energy <= 0 and self.world != self.dragon and self.world != self.spider:
                print("You need to sleep...\nВам нужно поспать...\n")
                for v in range(len(self.world)):
                    for f in range(len(self.world[v])):
                        self.world = self.bed
                        random_dream = random.randint(0, len(self.dream) - 1)
                        self.world[v][f] = f'\x1b[38;5;226;48;5;{self.dream[random_dream]}m * \x1b[0m'
                        for row in self.world:
                            print("".join(row))
                        time.sleep(1.2)
                self.energy = 100
            if self.km == 100:
                print(f"You are in the town! Your money: {cargo_hp + truck_hp * 10}\nВы в городе! Ваша зарплата: {cargo_hp + truck_hp * 10}\n")
                self.km = 0
                fuel = 100
                cargo_hp = 100
                truck_hp = 100
                self.energy = 100
                water = 100
                bottles = 20
            for row in self.world:
                print("".join(row))
            print("Distance\Расстояние:", self.km)
            print("Temperature\Температура:", self.temp)
            print("Truck HP\ХП машины:", truck_hp)
            print("Cargo HP\ХП груза:", cargo_hp)
            print("Thirsty\Жажда:", 100 - water)
            print("Water remaining\Воды осталось:", bottles)
            print("Fuel\Топливо:", fuel)
            print("Energy\Энергия:", self.energy)
desert = Desert()
desert.desertgame()