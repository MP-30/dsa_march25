def uniqueMorseRepresentations(words):
    code ={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",
     'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",
     'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
    
    main_dict = {}
    for i in words:
        s = ""
        for j in i:
            s += code[j]
        if s not in main_dict:
            main_dict[s] = 1
        elif s in main_dict:
            main_dict[s] +=1
    return(len(main_dict))
    
# words = ["gin","zen","gig","msg"]
words = ["a"]

print(uniqueMorseRepresentations(words))