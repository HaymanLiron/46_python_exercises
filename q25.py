def make_ing_form(verb):
    # convert a verb to present participle
    # use these heuristics:
    # If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
    # If the verb ends in ie, change ie to y and add ing
    # For words consisting of consonant-vowel-consonant, double the final letter before adding ing
    # By default just add ing
    vowels = ['a', 'e', 'i', 'o', 'u']
    exceptions = ['be', 'see', 'flee', 'knee']
    if verb.endswith("e") and verb not in exceptions:
        return str(verb[:-1] + "ing")
    elif verb.endswith("ie"):
        return str(verb[:-2] + "ying")
    elif len(verb) >= 3 and verb[-1].lower() not in vowels \
            and verb[-2].lower() in vowels and verb[-3].lower() not in vowels:
        return str(verb + verb[-1] + "ing")
    else:
        return verb + "ing"

