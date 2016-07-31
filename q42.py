# write a sentence splitter
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that
# Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
# Periods followed by a digit with no intervening whitespace are not sentence boundaries.
# Periods followed by whitespace and then an upper case letter, but preceded by any of a
#       short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
# Periods internal to a sequence of letters with no adjacent whitespace are not sentence
#       boundaries (for example, www.aptex.com, or e.g.)
# Periods followed by certain kinds of punctuation (notably comma and more periods)
#       are probably not sentence boundaries.


def split_into_sentences(text_to_parse):
    # strategy: keep two pointers for start and end of sentence
    # once the end pointer is in the right spot, append the sentence that was just formed, to the list
    # once you have gone through the whole string, append what is left to the list
    output = []  # have a list with each element a new sentence
    titles_that_use_period = ["Mr", "Mrs", "Dr"]
    start_pointer, end_pointer = 0, 0
    while end_pointer < len(text_to_parse):
        if text_to_parse[end_pointer] in ["!", "?"]:
            # we immediately know that we have reached the end of the sentence
            output.append(text_to_parse[start_pointer: end_pointer + 1])
            start_pointer = end_pointer + 2  # 2 because we don't want to include the space that precedes the sentence
            end_pointer = start_pointer
        elif text_to_parse[end_pointer] == ".":
            if end_pointer >= 2 and text_to_parse[start_pointer:end_pointer].endswith(("Mr", "Mrs", "Dr")):
                # this period is like Mrs. and shouldn't be counted
                end_pointer += 1
            elif end_pointer < len(text_to_parse) - 1 and text_to_parse[end_pointer + 1] != " ":
                # period is not followed by whitespace
                end_pointer += 1
            elif end_pointer < len(text_to_parse) - 2 and str(text_to_parse[end_pointer + 2]).islower():
                # no capital letter following period, so not end of sentence
                end_pointer += 1
            else:
                # if we have reached this far, we know we've got to the end of the sentence
                output.append(text_to_parse[start_pointer: end_pointer + 1])
                start_pointer = end_pointer + 2  # 2 because we don't want to include the space
                # that precedes the sentence
                end_pointer = start_pointer
        else:
            end_pointer += 1
    if end_pointer > start_pointer:
        output.append(text_to_parse[start_pointer: end_pointer + 1])
    return output


result = split_into_sentences("Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. "
                           "Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, "
                           "with a probability of .9 it isn't.")
for sentence in result:
    print(sentence)