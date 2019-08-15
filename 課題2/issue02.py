import random
import collections

suit_list_raw = ["spade","club","dia","heart"]
suit_list = ["♠","♣","♦","♥"]
# trump_list_raw = {"spade":[1,2,3,4,5,6,7,8,9,10,11,12,13],
# "club":[1,2,3,4,5,6,7,8,9,10,11,12,13],"dia":[1,2,3,4,5,6,7,8,9,10,11,12,13],"heart":[1,2,3,4,5,6,7,8,9,10,11,12,13]}
# trump_list = [[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]

# random.choices(trump_list)
# print(random.choices(trump_list[],k=4))
# print(trump_list[suit_list[random.randint(0,3)]][random.randint(0,12)])
# print("your cards :",end=" | ")
# for i in range(4):
#     suit = random.choice(suit_list)
#     print(suit,random.choice(trump_list_raw[suit]),end=" | ")

trump = []
hand =[]
for i in range(4):
    for m in range(1,14):
        trump.append(suit_list[i]+" " +str(m).zfill(2))
# print(trump)
print("your cards :",end="")
#手札handにランダムで5枚格納して表示
hand.append(random.sample(trump,k=5))
print(hand[0])

#hand_numはソート済み数字のみの配列
hand_num =[*range(5)]
for i in range(5):
    hand_num[i] = int(hand[0][i][2:4])
hand_num.sort()
# print(hand_num)

# print(hand[0][0][0],hand[0][0][1],hand[0][0][2:4],hand[0][1][0])

# print(int(hand[0][0][2:4]))
# if hand[0][0][2:4]=="10":
#     print("10です")

def is_royal(hand):
    role=0
    if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0] and (hand[0][0][2:4]=="10" or hand[0][1][2:4]=="10" or hand[0][2][2:4]=="10" or hand[0][3][2:4]=="10" or hand[0][4][2:4]=="10") and (hand[0][0][2:4]=="11" or hand[0][1][2:4]=="11" or hand[0][2][2:4]=="11" or hand[0][3][2:4]=="11" or hand[0][4][2:4]=="11") and (hand[0][0][2:4]=="12" or hand[0][1][2:4]=="12" or hand[0][2][2:4]=="12" or hand[0][3][2:4]=="12" or hand[0][4][2:4]=="12") and (hand[0][0][2:4]=="13" or hand[0][1][2:4]=="13" or hand[0][2][2:4]=="13" or hand[0][3][2:4]=="13" or hand[0][4][2:4]=="13") and (hand[0][0][2:4]=="01" or hand[0][1][2:4]=="01" or hand[0][2][2:4]=="01" or hand[0][3][2:4]=="01" or hand[0][4][2:4]=="01"):
        role = 1
        print("ロイヤルストレートフラッシュ")
    return role

def is_straight_flush(hand,hand_num):
    role=0
    if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0] and hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
        role = 2
        print("ストレートフラッシュ")
    else:
        for i in range(5):
            if hand_num[i] <= 4:
                hand_num[i] = hand_num[i]+13
        hand_num.sort()
        if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0] and hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
            role = 2
            print("ストレートフラッシュ")
    return role

def is_four_card(hand_num):
    role=0
    cnt = collections.Counter(hand_num)
    for i in cnt.values():
        if i == 4:
            role = 3
            print("フォーカード")
        break
    return role
    # print(cnt[key[0]])

def is_fullhouse(hand_num):
    role=0
    flag=0
    cnt = collections.Counter(hand_num)
    for i in cnt.values():
        if flag == 0 and i == 3:
            flag = 1
            continue
        else:
            break
        if flag == 1 and i == 2:
            role = 4
            print("フルハウス")
        else:
            break
    return role

def is_flush(hand):
    role=0
    if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0]:
        role = 5
        print("フラッシュ")
    return role

def is_straight(hand_num):
    role=0
    if hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
        role = 6
        print("ストレート")
    else:
        for i in range(5):
            if hand_num[i] <= 4:
                hand_num[i] = hand_num[i]+13
        hand_num.sort()
        if hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
            role = 6
            print("ストレート")
    return role

def is_three_card(hand_num):
    role=0
    cnt = collections.Counter(hand_num)
    for i in cnt.values():
        if i == 3:
            role = 7
            print("スリーカード")
        break
    return role

def is_pair(hand_num):
    cnt = collections.Counter(hand_num)
    flag=0
    role=10
    for i in cnt.values():
        if flag==0 and i == 2:
            flag = 1
            role = 9
            continue
        if flag==1 and i==2:
            role = 8
        break
    if role==8:
        print("ツーペア")
    elif role==9:
        print("ワンペア")
    else:
        print("残念")


role = is_royal(hand)
if role == 0:
    role = is_straight_flush(hand,hand_num)
if role == 0:
    role = is_four_card(hand_num)
if role == 0:
    role = is_fullhouse(hand_num)
if role == 0:
    role = is_flush(hand)
if role == 0:
    role = is_straight(hand_num)
if role == 0:
    role = is_three_card(hand_num)
if role == 0:
    role = is_pair(hand_num)

# if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0] and (hand[0][0][2:4]=="10" or hand[0][1][2:4]=="10" or hand[0][2][2:4]=="10" or hand[0][3][2:4]=="10" or hand[0][4][2:4]=="10") and (hand[0][0][2:4]=="11" or hand[0][1][2:4]=="11" or hand[0][2][2:4]=="11" or hand[0][3][2:4]=="11" or hand[0][4][2:4]=="11") and (hand[0][0][2:4]=="12" or hand[0][1][2:4]=="12" or hand[0][2][2:4]=="12" or hand[0][3][2:4]=="12" or hand[0][4][2:4]=="12") and (hand[0][0][2:4]=="13" or hand[0][1][2:4]=="13" or hand[0][2][2:4]=="13" or hand[0][3][2:4]=="13" or hand[0][4][2:4]=="13") and (hand[0][0][2:4]=="01" or hand[0][1][2:4]=="01" or hand[0][2][2:4]=="01" or hand[0][3][2:4]=="01" or hand[0][4][2:4]=="01"):
#     role = 1
#     print("ロイヤルストレートフラッシュ")

# else:

    #下記判定は13の後に1に連続する考えが無いため検討
    # if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0] and hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
    #     role = 2
    #     print("ストレートフラッシュ")
    # elif hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0]:
    #     role = 5
    #     print("フラッシュ")
    # elif hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
    #     role = 6
    #     print("ストレート")


    # #KからAにつないで連続した場合、K,1,2,3,4が最大だから4以下の数字は13足して再度判定する
    # else:
    #     for i in range(5):
    #         if hand_num[i] <= 4:
    #             hand_num[i] = hand_num[i]+13
    #     hand_num.sort()
        # if hand[0][0][0]==hand[0][1][0]==hand[0][2][0]==hand[0][3][0]==hand[0][4][0] and hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
        #     role = 2
        #     print("ストレートフラッシュ")
        # elif hand_num[0]+1==hand_num[1] and hand_num[1]+1==hand_num[2] and hand_num[2]+1==hand_num[3] and hand_num[3]+1==hand_num[4]:
        #     role = 6
        #     print("ストレート")
