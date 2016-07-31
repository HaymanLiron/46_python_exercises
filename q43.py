# find the largest set of words that are all anagrams to each other
# largest in the sense that it contains the most number of words
# use this word list: http://www.puzzlers.org/pub/wordlists/unixdict.txt


# get words into list
# each word gets a "score"
# the score is calculated by associating a numerical value to each character in the word
# anagrams will all have the same score
# note that other words might also coincidentally get the same score, but we still go ahead with this
# approach because of the time it saves

def get_word_score(word):
    sum_score, mult_score = 0, 2
    for c in word:
        c = c.lower()
        sum_score += ord(c)
        mult_score *= ord(c)
    return mult_score - sum_score


def get_max_set(word_dict):
    max_num_words = 0
    for a, b in word_dict.items():
        if len(b) > max_num_words:
            max_num_words = len(b)
            set_words = b
    print(set_words)


def generate_score_dict():
    word_dict = {}
    f = open("q43.txt", "r")
    for word in f.readlines():
        word = word.strip("\n")
        score = get_word_score(word)
        if score in word_dict:
            word_dict[score].append(word)
        else:
            word_dict[score] = [word]
    f.close()
    get_max_set(word_dict)


generate_score_dict()