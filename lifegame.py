import random

class Dice:

    def __init__(self):
        pass

    def roll(self):
        return random.randrange(1,7)



class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0


class Tile:

    def __init__(self, number):
        self.num = number
        self.link = 0




class GameBoard():

    def __init__(self):
        self.tiles = [ Tile(x) for x in range(1,26)]
        self.tiles[0].link = 8
        self.tiles[6].link = 3
        self.tiles[14].link = 17
        self.tiles[23].link = 7
        self.tiles[10].link = 21
        self.tiles[22].link = 11
        self.tiles[23].link = 11


    def movePlayer(self,p ,amount):


        visit_tiles = []


        #print('debug',p,amount)
        value = p.position + amount

        current = self.tiles[value]

        visit_tiles.append(current)
        print("Debug", current.num, current.link)

        if current.link != 0:
            p.position = current.link
            visit_tiles.append(self.tiles[current.link])
        else:
            p.position = value

        #print("Debug", p.name, p.position)



class GameUI:

    def __init__(self):
        self.player_list = []
        self.dice = Dice()
        self.board = GameBoard()





    def makeplayers(self):
        players_count = int(input("How many player?"))

        for x in range(players_count):
            player_name = input("Player name: ")
            player = Player(player_name)
            print(player)
            self.player_list.append(player)

    def playGame(self):
        count = 0
        while True:
            current_player = self.player_list[count % len(self.player_list)]
            print(current_player.name, "차례입니다")
            input("주사위 굴리기")
            dice_num = self.dice.roll()
            print('주사위의 눈은',dice_num,'입니다')

            count += 1
            visit_result = self.board.movePlayer(current_player, dice_num)

            print('Tile: ', visit_result[0].num, '입니다')

            if visit_result[0].link !=0:
                print("앗!! 이동해야 합니다.")
                print("Tile: ", visit_result[1].num, "이동했습니다.")


ui = GameUI()
ui.makeplayers()
ui.playGame()
