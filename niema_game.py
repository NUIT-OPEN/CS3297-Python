import math
import random


class Player:
    def take(self, remain):
        while True:
            try:
                num = int(input('  > 请输入你要取走物品的数量：'))
            except:
                num = 0

            if num > 0 and (num <= remain / 2 or num == 1):
                break
            print('* 输入无效：至少拿走一个并且最多只能拿走一半物品。')
        return num


class Computer(Player):
    def take(self, remain):
        choices = []
        l2 = int(math.log2(remain))
        for i in range(l2 // 2, l2 + 1):
            choice = remain - pow(2, i) + 1
            if choice <= remain / 2:
                choices.append(choice)

        num = 0
        if choices:
            num = choices[random.randint(0, len(choices) - 1)]
        if num == 0:
            num = random.randint(1, max(1, remain // 2))
        return num


class NiemaGame:
    def __init__(self):
        self._items_num = random.randint(1, 100)
        self._players = [Player(), Computer()]
        self._op_num = 0

    @property
    def remain_items(self):
        return self._items_num

    @property
    def current_player(self):
        return self._players[self._op_num % len(self._players)]

    def take_items(self, num):
        self._items_num -= num

    def start(self):
        while True:
            print('* 当前剩余物品数量：%s' % self.remain_items)
            num = self.current_player.take(self.remain_items)
            self._items_num -= num
            print('* %s 取走了%s件物品。' % (self.current_player, num))

            if not self.remain_items:
                break

            self._op_num += 1

        print('* %s 输掉了游戏。' % self.current_player)


if __name__ == '__main__':
    NiemaGame().start()
