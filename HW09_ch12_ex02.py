"""1. Write a program that reads a word list from a ﬁle (see Section 9.1) and
prints all the sets of words that are anagrams. Here is an example of what the
output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries'] ['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of
letters to a list of words that can be spelled with those letters. The
question is, how can you represent the collection of letters in a way that
can be used as a key?
2. Modify the previous program so that it prints the
longest list of anagrams ﬁrst, followed by the second longest, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along
with a letter on the board, to form an eight-letter word. What collection of
8 letters forms the most possible bingos? Hint: there are seven."""
def word_file_to_anagram_dictionary():
    anagram_dictionary = {}
    with open("words.txt","r") as word_file:
        for each_word in word_file:
            sorted_word = ''.join(sorted(each_word.strip()))
            anagram_dictionary[sorted_word] = anagram_dictionary.get(sorted_word,[])+[each_word.strip()]
    return anagram_dictionary

def sorted_list_of_anagrams():
    anagram_dictionary = word_file_to_anagram_dictionary()
    for each_key in (sorted(anagram_dictionary,key = lambda x:len(anagram_dictionary[x]), reverse = True)):
        if(len(anagram_dictionary[each_key])> 1):
            print(anagram_dictionary[each_key])
def eight_letter_bingo():
    anagram_dictionary = {}
    with open("words.txt","r") as word_file:
        for each_word in word_file:
            if(len(each_word.strip()) == 8):
                sorted_word = ''.join(sorted(each_word.strip()))
                anagram_dictionary[sorted_word] = anagram_dictionary.get(sorted_word,[])+[each_word.strip()]
    top_eight_bingo_list = anagram_dictionary[(sorted(anagram_dictionary,key = lambda x:len(anagram_dictionary[x]), reverse = True))[0]]
    print("Collection of 8 letters that forms the most possible bingos is : {}".format(" ".join(sorted(top_eight_bingo_list[0]))))
    print("The words these letters can form are : {}".format(" , ".join(sorted(top_eight_bingo_list))))
def main():
    #word_file_to_anagram_dictionary()
    #sorted_list_of_anagrams()
    eight_letter_bingo()
if __name__ == "__main__":
    main()
