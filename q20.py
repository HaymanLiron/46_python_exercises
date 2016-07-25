def translate():
    # translates a greeting from English to Swedish
    translation_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    for english in translation_dict.keys():
        print(translation_dict[english], end=" ")

