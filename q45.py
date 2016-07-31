# kids game where you choose a category and go in a circle
# and next word has to start with the last letter of the previous word
# find the longest sequence using list of words provided


import sys, threading
sys.setrecursionlimit(10000)
global_info = {"max length": 0,
               "word list": [],
               "used list": []}


def word_works(a, b):
    if a != b:
        return a[-1] == b[0]
    return False


def backtrack_solve(i):
    # goal is defined as "to reach no more"
    # get word based on i
    word = global_info["word list"][i]
    # base case of if used list is empty
    if not global_info["used list"]:
        global_info["used list"] = [word]
        return backtrack_solve(i+1)

    # if word works:
    if word not in global_info["used list"] and word_works(global_info["used list"][-1], word):
        # pop word to used_words list
        global_info["used list"].append(word)
        # call backtrack_solve
        return backtrack_solve(0)
    # elif word does not work:

    else:
        # if this is the last word in the list of available words,
        if i == len(global_info["word list"]) - 2:
            # if length > max_length[0],
            if len(global_info["used list"]) > global_info["max length"]:
                # make that the new max_length
                global_info["max length"] = len(global_info["used list"])
                print(global_info["used list"])
            # pop last word from the list of used words
            popped = global_info["used list"].pop()
            # call backtrack_solve
            return backtrack_solve(global_info["word list"].index(popped) + 1)
        # else move onto the next available word
        else:
            if i+1 < len(global_info["word list"]) - 1:
                return backtrack_solve(i+1)
            return None


def run_backtrack():
    words_one_string = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon " \
                       "cresselia croagunk darmanitan deino emboar emolga exeggcute gabite " \
                       "girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan " \
                       "kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine " \
                       "nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 " \
                       "porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking " \
                       "sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko " \
                       "tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"
    global_info["word list"] = words_one_string.split(" ")
    return backtrack_solve(0)

run_backtrack()
