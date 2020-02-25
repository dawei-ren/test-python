"""
特殊方法

如何使用特殊方法：
特殊方法的存在是为了呗Python解释器调用的，自己并不需要调用他们。
也就是说没有my_object.__len__()这种方法，而是应该使用len(my_object)。
在执行len(my_object)的时候，如果my_object是一个自定义类的对象，那么python会自己去调用由你实现的__len__方法。
"""
import collections

# 创建一个纸牌的命名元组类，类名称为Card为纸牌，里面有两个属性，一个rank数字，一个suit花色
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 纸牌数字
    suits = 'spades diamonds clubs hearts'.split()  # 黑桃、梅花、方片、红桃 ，纸牌花色

    def __init__(self):
        # 创建一个纸牌列表，列表包括所有数字和花色构成的一副纸牌，每张纸牌为一个Card对象，每个对象都有数字和花色两个属性
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        当使用len(a)方法的时候，会调用 a.__len__()方法
        返回纸牌数量
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        从一叠纸牌中抽取特定的一张纸牌，比如说第一张或者最后一张
        当使用a[0]方法的时候，会调用 a.__getitem__(0)方法
        """
        return self._cards[position]

    def __repr__(self):
        """
        类的字符串表示形式，它能把一个对象用字符串的形式表达出来以便辨认。
        其实，str.format方法也是利用了repr方法
        """
        return "FrenchDeck"

    def __bool__(self):
        """
        自定义bool值
        在调用bool(x)的时候，会调用此方法
        """
        return True


if __name__ == '__main__':
    deck = FrenchDeck()

    # # 查看牌数
    # print(len(deck))
    # # 查看第一张牌和最后一张牌
    # print(deck[0], deck[-1])
    # # 随机抽取一张牌
    # from random import choice
    # print(choice(deck))
    # # 查看一摞牌最上面的三张
    # print(deck[:3])
    # # 只看牌面是A的牌，先抽出索引是12的那张牌，然后每隔13张牌拿一张
    # print(deck[12::13])
    # # 正向迭代
    # for card in deck:
    #     print(card)
    # # 反向迭代
    # for card in reversed(deck):
    #     print(card)

    # 查询类的字符串表示形式
    print(deck)
