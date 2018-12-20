#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import sys
import random


class Cards(object):
    """扑克牌类
    """

    def __init__(self, card_type, card_value, card_real_value):
        self.card_type = card_type
        self.card_value = card_value
        self.card_real_value = card_real_value


class Roles(object):

    def __init__(self, role):
        """
        初始化角色
        :param role: 角色，'computer','player'
        """
        self.role = role
        self.cards = []

    def show_cards(self):
        """
        显示扑克牌
        :return:null
        """
        print(self.role, end=':')
        for card in self.cards:
            print(card.card_type, card.card_value, sep='', end=' ')
        print()

    def get_max_or_min(self, max_or_min):
        """
        计算当前的点数
        :return:int
        """
        sum_points = 0
        A = 0

        for card in self.cards:
            sum_points += card.card_real_value
            if card.card_value == 'A':
                A += 1

        if max_or_min == 'min':
            sum_points -= A * 10
            return sum_points

        for i in range(A):
            sum_points -= 10
            if sum_points <= 21:
                return sum_points

        return sum_points

    def is_bust(self):
        """
        判断是否爆牌
        :return: bool
        """
        return self.get_max_or_min('min') > 21


class Cards_Manager(object):
    """
    扑克牌管理类
    """

    def __init__(self):
        '''
        初始化扑克牌
        '''
        self.cards = []
        card_type = "♠♥♣♦"
        card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_real_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for type in card_type:
            for index, value in enumerate(card_value):
                card = Cards(type, value, card_real_value[index])
                self.cards.append(card)
        random.shuffle(self.cards)


    def send_card(self, role1, role2):
        """
        发牌
        """
        card = self.cards.pop()
        role1.cards.append(card)
        role2.cards.append(self.cards.pop())
        role2.cards.append(self.cards.pop())
        role2.show_cards()
        while True:
            choice = input("是否要牌(Y/N)?")
            if choice.capitalize() == 'Y':
                role2.cards.append(self.cards.pop())
                role2.show_cards()
                if role2.is_bust():
                    print("You lose!")
                    return
            else:
                break
        while True:
            role1.cards.append(self.cards.pop())
            role1.show_cards()
            if role1.get_max_or_min('max') < 17:
                continue
            elif role1.get_max_or_min('min') > 21:
                print('You win!')
                return
            else:
                break
        if role1.get_max_or_min('max') >= role2.get_max_or_min('max'):
            print('You lose!')
        else:
            print('You win!')


computer = Roles('computer')
player = Roles('player')
manager = Cards_Manager()
manager.send_card(computer, player)

