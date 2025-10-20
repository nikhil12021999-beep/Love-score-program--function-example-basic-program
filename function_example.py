def calculate_love_score(name1,name2):
    list_name1=list(name1.upper())
    list_name2=list(name2.upper())
    combine_list=list_name1+list_name2
    list_true=list("TRUE")
    list_love=list("LOVE")
    number1=[]
    number2=[]
    for i in combine_list:
        if i in list_true:
            number1.append(i)
            
    final1=len("".join(number1))
    for j in combine_list:
        if j in list_love:
            number2.append(j)
    final2=len("".join(number2))
    print(f"Love Score:{final1}{final2}")

calculate_love_score("Kanye West","Kim Kardashian")
