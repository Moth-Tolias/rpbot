"""RPbot"""
#[holds you close and nuzzles gently]
#{[actions] you [modifier]} and {[actions][modifier]}
#
#[snuggles down close and purrs against you warmly]
#{snuggles [down/up] [distance]} and {purrs against you [strength]}
#
#[nuzzles deeply and nyas softly~]
#{[actions][modifer]} and {nyas [strength]}
#
#[holds you in my arms and rocks softly]
#and rocks you [strength]}
#
#-always enclosed in square brackets
#-lowercase

import random


#modifiers
ACTIONSET1 = ("holds", "hugs", "nuzzles")
ACTIONSET2 = ("nyas", "purrs against you", "rocks you")
#ACTIONSET3 = ("snuggles")

MODELS = ("{action} you {mod}", "{action} {mod}",
          "{special} {strength}", "snuggles down {distance}")

#MODIFIERS = ("gently", "softly", "close", "tight", "warmly")
STRENGTHS = ("gently", "softly", "warmly")
DISTANCES = ("close", "tight")
MODIFIERS = STRENGTHS + DISTANCES

def returncards(deck):
    """return a random two-item tuple harvested from the given sequence"""
    #amount=2
    randno1 = 0
    randno2 = 0
    while randno1 == randno2:
        randno1 = random.randrange(0, len(deck), 1)
        randno2 = random.randrange(0, len(deck), 1)

    return (deck[randno1], deck[randno2])


def generate_rp_action():
    """return a rp action"""
    #assmble the cards
    mycards = returncards(ACTIONSET1)
    action1 = mycards[0]
    action2 = mycards[1]

    mycards = returncards(ACTIONSET2)
    action_special1 = mycards[0]
    action_special2 = mycards[1]

    mycards = returncards(MODIFIERS) #mod, strength and distances need to be checked for dupes
    mod1 = mycards[0]
    mod2 = mycards[1]

    mycards = returncards(STRENGTHS)
    strength1 = mycards[0]
    strength2 = mycards[1]

    mycards = returncards(DISTANCES)
    distance1 = mycards[0]
    distance2 = mycards[1]

    mycards = returncards(MODELS)
    model1 = mycards[0]
    model2 = mycards[1]
    #the cards are now assembled

    rp_part_1 = model1
    rp_part_1 = rp_part_1.format(action=action1, special=action_special1,
                                 mod=mod1, strength=strength1, distance=distance1)
    rp_part_2 = model2
    rp_part_2 = rp_part_2.format(action=action2, special=action_special2,
                                 mod=mod2, strength=strength2, distance=distance2)
    return rp_part_1 + " and " + rp_part_2

print("["+generate_rp_action()+"]") #need to implement~
input()#debug
