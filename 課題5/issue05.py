import random
class Maze():
    """ 迷路を作るクラス"""
    PATH = 0
    WALL = 1
    def __init__(self, width, height):
        self.maze = []
        self.width = width
        self.height = height
        # 迷路は、幅高さ5以上の奇数で生成する。
        if(self.height < 5 or self.width < 5):
            print('at least 5')
            exit()
        if (self.width % 2) == 0:
            self.width += 1
        if (self.height % 2) == 0:
            self.height += 1
    def set_out_wall(self):
        """ 迷路全体を構成する2次元配列、迷路の外周を壁とし、それ以外を通路とする。"""
        for _x in range(0, self.width):
            row = []
            for _y in range(0, self.height):
                if (_x == 0 or _y == 0 or _x == self.width-1 or _y == self.height -1):
                    cell = self.WALL
                else:
                    cell = self.PATH
                row.append(cell)
            self.maze.append(row)
        return self.maze
    def set_inner_wall_boutaosi(self):
        """迷路の中に棒を立ててランダムな方向に倒す。
        外周の内側に基準となる棒を1セルおき、(x, y ともに偶数の座標)に配置する。"""
        for _x in range(2, self.width-1, 2):
            for _y in range(2, self.height-1, 2):
                self.maze[_x][_y] = self.WALL
                # 棒をランダムな方向に倒して壁とする。
                # (ただし以下に当てはまる方向以外に倒す。)
                # 1行目の内側の壁以外では上方向に倒してはいけない。
                # すでに棒が倒され壁になっている場合、その方向には倒してはいけない。
                while True:
                    if _y == 2:
                        direction = random.randrange(0, 4)
                    else:
                        direction = random.randrange(0, 3)
                    # 棒を倒して壁にする方向を決める。
                    wall_x = _x
                    wall_y = _y
                    # 右
                    if direction == 0:
                        wall_x += 1
                    # 下
                    elif direction == 1:
                        wall_y += 1
                    # 左
                    elif direction == 2:
                        wall_x -= 1
                    # 上
                    else:
                        wall_y -= 1
                    # 壁にする方向が壁でない場合は壁にする。
                    if self.maze[wall_x][wall_y] != self.WALL:
                        self.maze[wall_x][wall_y] = self.WALL
                        break
        return self.maze
    def set_start_goal(self):
        """ スタートとゴールを迷路にいれる。"""
        self.maze[1][1] = 'S'
        self.maze[self.width-2][self.height-2] = 'G'
        return self.maze
    def print_maze(self):
        """ 迷路を出力する。"""
        for row in self.maze:
            for cell in row:
                if cell == self.PATH:
                    print('   ', end='')
                elif cell == self.WALL:
                    print('###', end='')
                elif cell == 'S':
                    print('STR', end='')
                elif cell == 'G':
                    print('GOL', end='')
            print()
maze = Maze(20, 20)
maze.set_out_wall()
maze.set_inner_wall_boutaosi()
maze.set_start_goal()
maze.print_maze()
