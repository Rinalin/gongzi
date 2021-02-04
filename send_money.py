#!/user/bin/env python
# -*- coding:utf-8 -*-
from jinjie.money import Money
from jinjie.select_money import Select_Money


def Send_Money():
    base_money = Money()
    saved_money = Select_Money()
    send_money = base_money+saved_money
    return  send_money