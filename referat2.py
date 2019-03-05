with open("referat.txt", 'r', encoding="utf-8") as new_file:
    content =  new_file.read()
    print("Len_of_content =", len(content))
    word_list = content.replace(',','').replace(':','').replace('.','').replace('«', ' ').replace('»', ' ').lower().split()
    print(len(word_list))
    new_word_list = content.replace("." , "!")
    print(new_word_list)

        
