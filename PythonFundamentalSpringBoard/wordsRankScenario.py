def remove_punctuation(st, case = 'a'):
    import string
    for c in string.punctuation:
        st = st.replace(c, '')
    if case == 'a':
        return st.split()
    if case == 'l':
        st = st.lower()
        return st.split()
    if case == 't':
        st = st.title()
        return st.split()

def frequency_dictionary(words):
    freq_dict = {}
    uniq_word = []
    for word in words:
        if word not in uniq_word:
            uniq_word.append(word)
    for word in uniq_word:
        freq_dict[word] = words.count(word)
    return freq_dict
def strip_common_words(words):
    unique = []
    common_words = open('1000 words.txt','r')
    common_words = common_words.read()
    for word in words:
        if word not in common_words:
            unique.append(word)
    return unique

def print_ranked_dictionary(dictionary, count = 20):
    rankedDict = sorted(dictionary, key= dictionary.get, reverse= True) # doubt
    for i in range(count):
        print(rankedDict[i],'repeats', dictionary[rankedDict[i]],'times')

def main():
    text = open('Happy Potter.txt', 'r')
    text = text.read()
    word_list = remove_punctuation(text, 't')
    uniques = strip_common_words(word_list)
    dictionary = frequency_dictionary(uniques)
    print_ranked_dictionary(dictionary)

# dictionary = frequency_dictionary()
# print_ranked_dictionary(dictionary)
main()