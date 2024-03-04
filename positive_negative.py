from stop_word_removal import stop_words_set

def remove_stop_word_from_pos_neg():
    with open(r'C:\Users\DELL\PycharmProjects\dataminner\MasterDictionary\negative-words.txt', 'r', encoding='utf-8', errors='replace') as stopwords_file:
        response_negative = set(stopwords_file.read().split())

    with open(r'C:\Users\DELL\PycharmProjects\dataminner\MasterDictionary\positive-words.txt', 'r', encoding='utf-8', errors='replace') as stopwords_file:
        response_postive = set(stopwords_file.read().split())

    rem_postive_word = response_postive - stop_words_set
    rem_negative_word = response_negative - stop_words_set
    return rem_postive_word, rem_negative_word


pos_word_res, neg_word_res = remove_stop_word_from_pos_neg()
dict_pos_neg = {
    'Positive_Words' : pos_word_res,
    'Negative_Words' : neg_word_res
}

