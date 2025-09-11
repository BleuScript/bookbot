from operator import itemgetter

def get_count(txt):
    words = txt.split()
    count = len(words)
    return count

def get_char(txt):
    char = 0
    for i in txt:
        if i != None:
            char += 1
    return char

def get_dict_char(txt):
    l_words = txt.lower()
    book_dict = {}
    for c_char in l_words:
        if c_char in book_dict: book_dict[c_char] += 1
        else: book_dict[c_char] = 1
    return book_dict

def get_sorted_report(t_list):
    t_list.sort(key=sort_help, reverse=True)
    s_dict = []
    for ch, n in t_list:
        s_dict.append({"char": ch, "num": n})
    return s_dict

def sort_help(item):
    return item[1]

def dict_tuple_list(dic): #dict > tuple list
    t_list = []
    for ch, n in dic.items():
        t_list.append((ch,n))
    return t_list

def dict_print(s_dict):
    for item in s_dict:
        print(f"{item["char"]}: {item["num"]}\n")