import sys
from stats import get_count
from stats import get_dict_char
from stats import get_sorted_report
from stats import dict_tuple_list
from stats import dict_print

def get_book_text(filepath):
    with open(filepath) as f:
        c_book = f.read()
    return c_book

def main():
    print('Usage: python3 main.py <path_to_book>\n')
    c_book = get_book_text(sys.argv[1])
    c_dict = get_dict_char(c_book)
    t_list = dict_tuple_list(c_dict)
    s_dict = get_sorted_report(t_list)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {get_count(c_book)} total words\n--------- Character Count -------\n")
    dict_print(s_dict)
    print(f"============= END ===============")

if __name__=="__main__":main()