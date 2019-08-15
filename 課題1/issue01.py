# 自機・敵機のデータ格納
my_ship_raw = [100,100,70,100]
my_ship = []
my_ship.append(my_ship_raw[0]+my_ship_raw[2]/2)
my_ship.append(my_ship_raw[1]+my_ship_raw[1]/2)
my_ship.append(my_ship_raw[2]/2)
my_ship.append(my_ship_raw[3]/2)

# print(my_ship)
enemy_count = 3

# for i in range(enemy_count):

#[左上位置x,y,幅,高さ]
enemy_ships_raw = [[50,60,100,50],[10,120,100,50],[165,115,70,70]]
enemy_ships =[[] for i in range(enemy_count)]

#中心点、中心からの幅と高さを格納する
for i in range(enemy_count):
    enemy_ships[i].append(enemy_ships_raw[i][0]+enemy_ships_raw[i][2]/2)
    enemy_ships[i].append(enemy_ships_raw[i][1]+enemy_ships_raw[i][3]/2)
    enemy_ships[i].append(enemy_ships_raw[i][2]/2)
    enemy_ships[i].append(enemy_ships_raw[i][3]/2)
        # enemy_ships_raw[i][2] = trans[2]/2
        # trans[3] = trans[3]/2
        # trans[0] = trans[0]+trans[2]
        # trans[1] = trans[1]+trans[3]
# print(enemy_ships)

###以下、判定処理###
dist=[0,0,0,0]
enemy_index = 0
#enemy_shipsから配列１つ抜き出す
for e in enemy_ships:
    enemy_index+=1
    for init in dist:
        init = 0
    dist[0] = abs(my_ship[0] -e[0])
    dist[1] = abs(my_ship[1] -e[1])
    dist[2] = my_ship[2]+e[2]
    dist[3] = my_ship[3]+e[3]
    # print(dist)

    if(dist[0] > dist[2] or dist[1]>dist[3]):
        continue
    # if(dist[1] > dist[3]):
    #     continue
    print("敵機" +str(enemy_index) + "は当たり")
