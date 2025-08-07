def get_num_words(textazo):
    splitlist = str.split(textazo)
    return len(splitlist)

def char_stats(textazo):
    charlist = list(textazo.lower())
    char_dict = {}
    for letra in charlist:
        if (letra in char_dict ):
            char_dict[letra] +=1
        else:
            char_dict[letra] = 1
    return char_dict

def key_sort(items):
    return items["num"]

def sort_chars(unsorted_dict):
    sorted_list=[]
    for items in unsorted_dict:
        if items.isalpha():
            sorted_list.append({"char":items,"num":unsorted_dict[items]})
    ###vale aca ya tengo la lista surtida
    ## sorted_list.sort(key=lambda word : word["num"] , reverse=True)
    ## esto es bueno, pero hay que probar con una funcion key;
    sorted_list.sort(reverse=True, key= key_sort)
    return sorted_list

