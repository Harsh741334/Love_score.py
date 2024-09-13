def calculate_love_score(name1, name2):
    # for True
    count1 = 0
    name_a = name1.lower()
    name_b = name2.lower()

    count1 = 0
    count2 = 0
    x = "true"
    y = "love"
    for i in x:
        count1 += name_a.count(i)
        count1 += name_b.count(i)
    for i in y:
        count2 += name_a.count(i)
        count2 += name_b.count(i)
    ans = str(count1) +str(count2)
    print(ans)


calculate_love_score("Kanye West", "Kim Kardashian")



