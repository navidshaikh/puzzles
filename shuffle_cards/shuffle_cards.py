#!/usr/bin/env python2

from random import choice


def shuffle_cards(cards):
    if not cards:
        return cards
    shuffled = []
    for i, card in enumerate(cards):
        picked = choice(cards[i:])
        picked_index = cards.index(picked)
        cards[i], cards[picked_index] = cards[picked_index], cards[i]
        shuffled.append(picked)
    return shuffled



if __name__ == "__main__":
    deck1 = range(52)
    print "For deck of cards {}".format(deck1)
    print "Shuffled {}".format(shuffle_cards(deck1))

