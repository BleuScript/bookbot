import sys
from stats import get_count
from stats import get_char
from stats import get_dict_char
from stats import get_sorted_report
from stats import dict_tuple_list
from stats import dict_print
#from stats import sort_help

def get_book_text(filepath):
    with open(filepath) as f:
        c_book = f.read()
    return c_book

def main():
    c_book = get_book_text(sys.argv[1])
    c_dict = get_dict_char(c_book)
    t_list = dict_tuple_list(c_dict)
    s_dict = get_sorted_report(t_list)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound 75767 total words\n--------- Character Count -------\n")
    dict_print(s_dict)
    print(f"============= END ===============")
    #print(get_dict_char(c_book))
    #print(get_char(c_book))
    #print(c_book.split())
    #print(f"{get_count(c_book)} words found in the document")

if __name__=="__main__":main()