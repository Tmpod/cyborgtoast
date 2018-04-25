# This is an external library for calculating levels.
# It's basically a copy of https://github.com/Plancke/hypixel-php/blob/master/src/util/Leveling.php
# But written in Python.

from math import sqrt, floor

EXP_FIELD = 0
LVL_FIELD = 0

BASE = 10000
GROWTH = 2500

HALF_GROWTH = 0.5 * GROWTH

REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH)/GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX * REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2/GROWTH

BW_XP_PER_PRESTIGE = 489000
BW_LVLS_PER_PRESTIGE = 100


def getLevel(exp):
    return floor(1+REVERSE_PQ_PREFIX + sqrt(REVERSE_CONST+GROWTH_DIVIDES_2*exp))

def getExactLevel(exp):
    return getLevel(exp) + getPercentageToNextLevel(exp)

def getExpFromLevelToNext(level):
    return GROWTH * (level-1) + BASE

def getTotalExpToLevel(level):
    lv = floor(level)
    x0 = getTotalExpToFullLevel(lv)
    if level == lv:
        return x0
    else:
        return (getTotalExpToFullLevel(lv+1) - x0) * (level % 1) + x0

def getTotalExpToFullLevel(level):
    return (HALF_GROWTH * (level-2) + BASE) * (level-1)

def getPercentageToNextLevel(exp):
    lv = getLevel(exp)
    x0 = getTotalExpToLevel(lv)
    return (exp-x0) / (getTotalExpToLevel(lv+1) - x0)

def getExperience(EXP_FIELD, LVL_FIELD):
    exp = int(EXP_FIELD)
    exp += getTotalExpToFullLevel(LVL_FIELD+1)
    return exp

def getBedWarsLvl(exp):
    
    prestige = exp // BW_XP_PER_PRESTIGE
    exp = exp % BW_XP_PER_PRESTIGE
    
    if prestige > 5:
        over = prestige % 5
        exp += over * BW_XP_PER_PRESTIGE
        prestige -= over

    if exp < 500:
        return 0 + (prestige * BW_LVLS_PER_PRESTIGE)
    elif (exp < 1500):
        return 1 + (prestige * BW_LVLS_PER_PRESTIGE)
    elif (exp < 3500):
        return 2 + (prestige * BW_LVLS_PER_PRESTIGE)
    elif (exp < 5500):
        return 3 + (prestige * BW_LVLS_PER_PRESTIGE)
    elif (exp < 9000):
        return 4 + (prestige * BW_LVLS_PER_PRESTIGE)

    exp -= 9000

    return (exp / 5000 + 4) + (prestige * BW_LVLS_PER_PRESTIGE)
