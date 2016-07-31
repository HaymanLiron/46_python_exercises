# kids game where you choose a category and go in a circle
# and next word has to start with the last letter of the previous word
# find the longest sequence using list of words provided


import sys, threading
sys.setrecursionlimit(10000)
global_info = {"max length": 0}


def available_words(used_list, word_list):
    return [x for x in word_list if x not in used_list]


def word_works(a, b):
    return a[-1] == b[0]


def backtrack_solve(i, used_list, word_list):
    # goal is defined as "to reach no more"
    # get word based on i
    word = available_words(used_list, word_list)[i]
    # base case of if used list is empty
    if not used_list:
        used_list = [word]
        return backtrack_solve(i+1, used_list, word_list)

    # if word works:
    if word_works(used_list[-1], word):
        # pop word to used_words list
        used_list.append(word)
        # call backtrack_solve
        return backtrack_solve(0, used_list, word_list)

    # elif word does not work:
    else:
        # if this is the last word in the list of available words,
        if i == len(available_words(used_list, word_list)) - 2:
            # if length > max_length[0],
            if len(used_list) > global_info["max length"]:
                # make that the new max_length
                global_info["max length"] = len(used_list)
                print(used_list)
            # pop last word from the list of used words
            popped = used_list.pop()
            # call backtrack_solve
            return backtrack_solve(word_list.index(popped) + 1, used_list, word_list)
        # else move onto the next available word
        else:
            if i+1 < len(available_words(used_list, word_list)) - 1:
                return backtrack_solve(i+1, used_list, word_list)
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
    word_list = words_one_string.split(" ")
    return backtrack_solve(0, [], word_list)

run_backtrack()
