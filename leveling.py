# This is an external library for calculating levels.
# It's basically a copy of https://github.com/Plancke/hypixel-php/blob/master/src/util/Leveling.php
# But written in Python.

BW_XP_PER_PRESTIGE = 489000
BW_LVLS_PER_PRESTIGE = 100

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
