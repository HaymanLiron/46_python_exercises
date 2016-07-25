def make_3sg_form(verb):
    # converts a verb from infinitive to third person singular
    # e.g. try becomes tries
    if verb.endswith("y"):
        return str(verb[:-1] + "ies")
    elif verb.endswith(tuple(["o", "ch", "s", "sh", "x", "z"])):
        return verb + "es"
    else:
        return verb + "s"