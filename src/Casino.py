import random

class Goose:
    def __init__(self, name):
        try:
            self.name = name
            self.stolen_chips = 0

            self.is_alive = True



        except Exception as e:
            print(f"Ошибка в __init__: {e}")

    def steal_chips(self, player):


        try:
            if self.is_alive and player.is_alive and player.chips > 0:
                stolen = min(random.randint(1, 5), player.chips)
                player.chips -= stolen


                
                self.stolen_chips += stolen
                print(f"Гусь {self.name} украл {stolen} фишек у {player.name}")


                print(f"У {player.name} осталось {player.chips} фишек")
                return stolen
            else:
                print(f"Гусь {self.name} не смог украсть фишки")
                return 0
        except Exception as e:


            print(f"Ошибка в steal_chips: {e}")
            return -1



    def __repr__(self):
        if self.is_alive:


            status = "ЖИВ" 
        else:
            status = "МЁРТВ"
        return f"Гусь {self.name} украл фишек: {self.stolen_chips}, Статус: {status}"




    def __add__(self, other):
        try:
            if isinstance(other, Goose):
                print(f"Гуси {self.name} и {other.name} объединились")


                return self.stolen_chips + other.stolen_chips
            else:
                return NotImplemented
            

        except Exception as e:
            print(f"Ошибка в __add__: {e}")
            return 0




class WarGoose(Goose):
    def attack(self, player):
        try:
            if self.is_alive and player.is_alive:
                stolen = random.randint(1, 3)

                if player.chips >= stolen:
                    player.chips -= stolen


                    self.stolen_chips += stolen
                    print(f"Боевой гусь {self.name} атаковал {player.name} и украл {stolen} фишек")
                    return stolen
                
                else:
                    print(f"{player.name} не имеет фишек для кражи")
                    return 0
            else:
                print("Атака невозможна")


                return 0
            

        except Exception as e:
            print(f"Ошибка в attack: {e}")
            return -1


class HonkGoose(Goose):
    def __call__(self, player):
        return self.honk(player)
    
    def honk(self, player):
        try:
            if self.is_alive and player.is_alive and player.chips > 0:

                lost = random.randint(1, 2)
                player.chips = max(0, player.chips - lost)

                print(f"Гусь {self.name} крикнул на {player.name}. Потеряно {lost} фишек")
                return lost
            
            else:

                print("Крик не подействовал")
                return 0
            
        except Exception as e:
            print(f"Ошибка в honk: {e}")
            return -1



class Player:
    def __init__(self, name):
        try:
            self.name = name
            self.chips = 20
            self.is_alive = True


        except Exception as e:
            print(f"Ошибка в __init__: {e}")
    
    def bet(self):
        try:
            if self.is_alive and self.chips > 0:

                bet_amount = random.randint(1, 3)
                if self.chips >= bet_amount:

                    if random.random() < 0.5:
                        win = bet_amount * 2
                        self.chips += win

                        print(f"{self.name} выиграл {win} фишек. Всего: {self.chips}")
                        return win
                    
                    else:
                        self.chips -= bet_amount
                        print(f"{self.name} проиграл {bet_amount} фишек. Осталось: {self.chips}")
                        return -bet_amount
                else:
                    print(f"У {self.name} недостаточно фишек для ставки")
                    return 0
                


            else:
                print(f"{self.name} не может делать ставки")
                return 0
        except Exception as e:
            print(f"Ошибка в bet: {e}")
            return -1
    


    def panic(self):
        try:
            if self.is_alive and self.chips > 0:
                lost = random.randint(2, 4)
                self.chips = max(0, self.chips - lost)
                print(f"{self.name} впал в панику и потерял {lost} фишек")
                return lost
            
            else:
                print(f"{self.name} не может иметь панику")


                return 0
            
        except Exception as e:
            print(f"Ошибка в panic: {e}")
            return -1
    
    def __repr__(self):
        if self.is_alive:
            status = "ЖИВ" 
        else:
            status = "МЁРТВ"
        return f"Игрок {self.name} Фишки: {self.chips}, Статус: {status}"


class GooseCollection:
    def __init__(self):
        self.geese = []
    
    def __getitem__(self, key):
        try:
            if isinstance(key, slice):

                return self.geese[key.start:key.stop:key.step]
            else:
                return self.geese[key]
            

        except Exception as e:
            print(f"Ошибка в __getitem__: {e}")
            return None
    
    def __setitem__(self, key, value):
        try:
            self.geese[key] = value
        except Exception as e:
            print(f"Ошибка в __setitem__: {e}")
    
    def __delitem__(self, key):
        try:
            del self.geese[key]
        except Exception as e:
            print(f"Ошибка в __delitem__: {e}")


    
    def __iter__(self):
        return iter(self.geese)
    

    def __len__(self):
        return len(self.geese)
    

    def add_goose(self, goose):
        try:
            self.geese.append(goose)
            return 0
        except Exception as e:
            print(f"Ошибка в add_goose: {e}")
            return -1
    
    def remove_goose(self, goose):
        try:
            if goose in self.geese:
                self.geese.remove(goose)
                return 0
            

            return -1
        except Exception as e:
            print(f"Ошибка в remove_goose: {e}")
            return -1
    
    def get_alive_geese(self):
        return [x for x in self.geese if x.is_alive]
    




    def __repr__(self):
        return f"количество гусей: {len(self)}"


class PlayerCollection:
    def __init__(self):
        self.players = []


    
    def __getitem__(self, key):
        try:
            if isinstance(key, slice):
                return self.players[key.start:key.stop:key.step]
            

            else:
                return self.players[key]
            
        except Exception as e:
            print(f"Ошибка в __getitem__: {e}")
            return None
        
    
    def __setitem__(self, key, value):
        try:
            self.players[key] = value

        except Exception as e:
            print(f"Ошибка в __setitem__: {e}")
    


    def __delitem__(self, key):
        try:
            del self.players[key]


        except Exception as e:
            print(f"Ошибка в __delitem__: {e}")
    
    def __iter__(self):
        return iter(self.players)
    def __len__(self):
        return len(self.players)
    
    def add_player(self, player):
        try:
            self.players.append(player)
            return 0
        except Exception as e:
            print(f"Ошибка в add_player: {e}")
            return -1
        

    
    def remove_player(self, player):
        try:
            if player in self.players:

                self.players.remove(player)

                return 0
            


            return -1
        

        except Exception as e:
            print(f"Ошибка в remove_player: {e}")
            return -1
    

    def get_alive_players(self):
        return [x for x in self.players if x.is_alive]
    

    def __repr__(self):
        return f"количество игроков: {len(self)}"


class ChipBalanceDict:
    def __init__(self):
        self.balances = {}
    
    def __getitem__(self, player_name):
        try:
            return self.balances.get(player_name, 0)
        
        except Exception as e:
            print(f"Ошибка в __getitem__: {e}")
            return 0
    

    def __setitem__(self, player_name, chips):
        try:
            old_value = self.balances.get(player_name, 0)
            print(f"{player_name}: {old_value} -> {chips}")
            self.balances[player_name] = chips
        except Exception as e:
            print(f"Ошибка в __setitem__: {e}")
    


    def __delitem__(self, player_name):
        try:
            del self.balances[player_name]
            print(f"Удалён игрок {player_name}")
        except Exception as e:
            print(f"Ошибка в __delitem__: {e}")
    
    def __len__(self):
        return len(self.balances)
    

    def __contains__(self, player_name):
        return player_name in self.balances
    
    def __iter__(self):
        return iter(self.balances.items())
    


    def update(self, player_name, chips):
        try:
            self[player_name] = chips
            return 0
        
        except Exception as e:
            print(f"Ошибка в update: {e}")
            return -1
    
    def __repr__(self):
        return f"записей: {len(self)}"


class Casino:
    def __init__(self, name):
        try:
            self.name = name
            self.geese = GooseCollection()

            self.players = PlayerCollection()
            self.balances = ChipBalanceDict()
            self.step_count = 0


        except Exception as e:
            print(f"Ошибка в __init__: {e}")
    
    def register_player(self, player):
        try:
            self.players.add_player(player)
            self.balances.update(player.name, player.chips)


            return 0
        except Exception as e:
            print(f"Ошибка в register_player: {e}")
            return -1
        
def run_simulation_casino(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
    
    casino = Casino("Гусиное Казино")
    
    for i in range(steps):
        event = random.choice(["add_player", "add_wargoose", "add_honkgoose", "attack", "honk", "bet", "panic"])
        
        if event == "add_player":
            name = f"Игрок{random.randint(1, 100)}"
            player = Player(name)

            casino.register_player(player)

            print(f"Шаг {i+1}: Добавлен {name}")
            



        elif event == "add_wargoose":

            name = f"Wargoose{random.randint(1, 100)}"

            goose = WarGoose(name)
            casino.geese.add_goose(goose)
            print(f"Шаг {i+1}: Добавлен боевой гусь {name}")
            
        elif event == "add_honkgoose":
            name = f"Honkgoose{random.randint(1, 100)}"
            goose = HonkGoose(name)
            casino.geese.add_goose(goose)
            print(f"Шаг {i+1}: Добавлен кричащий гусь {name}")
            
        elif event == "attack" and len(casino.players) > 0 and len(casino.geese) > 0:
            players = list(casino.players)


            geese = [x for x in casino.geese if isinstance(x, WarGoose)]
            

            if players and geese:
                player = random.choice(players)

                goose = random.choice(geese)
                goose.attack(player)


                casino.balances.update(player.name, player.chips)
                print(f"Шаг {i+1}: {goose.name} атаковал {player.name}")
                


        elif event == "honk" and len(casino.players) > 0 and len(casino.geese) > 0:
            players = list(casino.players)
            geese = [x for x in casino.geese if isinstance(x, HonkGoose)]
            
            if players and geese:
                player = random.choice(players)
                goose = random.choice(geese)
                goose.honk(player)


                casino.balances.update(player.name, player.chips)
                print(f"Шаг {i+1}: {goose.name} крикнул на {player.name}")
                
        elif event == "bet" and len(casino.players) > 0:
            player = random.choice(list(casino.players))

            player.bet()
            casino.balances.update(player.name, player.chips)


            print(f"Шаг {i+1}: {player.name} сделал ставку")
            
        elif event == "panic" and len(casino.players) > 0:

            player = random.choice(list(casino.players))
            player.panic()

            casino.balances.update(player.name, player.chips)

            print(f"Шаг {i+1}: {player.name} впал в панику")