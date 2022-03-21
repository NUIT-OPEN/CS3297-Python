class GuessGame:
    def __init__(self):
        self._items = {}
        self._selected = None

    @property
    def selected_item_price(self):
        return self._items.get(self._selected)

    def append_item(self, item, price):
        self._items[item] = price

    def guess(self):
        price_str = input('请输入竞猜价格(只能输入整数价格)：')
        if not price_str.isnumeric():
            print('输入价格非法，请重新输入！')

        price = int(price_str)
        sip = self.selected_item_price
        if price < sip:
            print('猜的价格小了...')
        elif price > sip:
            print('猜的价格大了...')
        else:
            print('恭喜，你猜对了!')
            return True

        return False

    def select_item(self):
        print('数字猜谜游戏!')
        print('可以竞猜的商品如下:')
        for i, k in enumerate(self._items, 1):
            print(i, k)

        while True:
            index_str = input('请输入竞猜商品前面的数字: ')
            if index_str.isnumeric():
                index = int(index_str)
                if 0 < index <= len(self._items):
                    break

        self._selected = list(self._items.keys())[index - 1]
        print('您选择的竞猜商品是:', self._selected)

    def start(self):
        self.select_item()
        while not self.guess():
            pass


if __name__ == '__main__':
    g = GuessGame()
    g.append_item('小米手环4', 199)
    g.append_item('荣耀手环5', 169)
    g.append_item('华为手环B5', 849)
    g.append_item('ZNNCO智能血压手环', 368)
    g.start()
