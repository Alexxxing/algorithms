import random


def shuffle_system(cards):
    # 随机洗牌
    for i in range(len(cards)):
        randomi = i + random.randint(0, (len(cards) - i - 1))
        cards[i], cards[randomi] = cards[randomi], cards[i]
    return cards


if __name__ == '__main__':
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'Joker']
    shuffle_system(cards)
    print(cards)