import os
import sys
import random
import pygame as pg
import pygame.freetype

FPS = 20  # FPS


def main():
    pg.init()

    size = width, height = 800, 800  # 屏幕大小
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Gomoku")  # 设置标题

    clock = pg.time.Clock()
    run = True
    win = -1  # 输赢标志 -1表示尚未决出胜负
    current_chess = 0  # 当前棋子颜色 0是白棋
    current_i, current_j = -10, -10  # 当前棋子在棋盘上的坐标

    # chessboard = [[-1]*14]*14  # 棋盘数组 14*14, can't init like this, shallow copy!!
    chessboard = []
    for i in range(15):
        chessboard.append([-1]*15)

    # 主循环
    while run:
        clock.tick(FPS)  # 设置fps

        # 绘制背景
        screen.fill((184, 134, 11))

        # 绘制棋盘
        for i in range(15):
            pg.draw.line(screen, (0, 0, 0), (50+i*50, 50),
                         (50+i*50, 800-50), 2)
        for j in range(15):
            pg.draw.line(screen, (0, 0, 0), (50, 50+j*50),
                         (800-50, 50+j*50), 2)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                pass
            elif event.type == pg.QUIT:   # 检测到关闭窗口事件
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # 按下鼠标左键
                x, y = pg.mouse.get_pos()
                if x < 35 or x > 765 or y < 35 or y > 765:
                    break
                if win == -1:
                    i = x // 50
                    j = y // 50

                    xx = x % 50
                    yy = y % 50

                    if xx < 25:
                        i -= 1
                    if yy < 25:
                        j -= 1

                    # 当前棋盘位置没有子才能落子
                    if chessboard[j][i] == -1:
                        chessboard[j][i] = current_chess
                        current_chess ^= 1
                else:
                    pass

            elif event.type == pg.MOUSEMOTION:  # 鼠标移动
                x, y = event.pos
                if x < 35 or x > 765 or y < 35 or y > 765:
                    break
                current_i = x // 50
                current_j = y // 50

                xx = x % 50
                yy = y % 50

                if xx < 25:
                    current_i -= 1
                if yy < 25:
                    current_j -= 1

        # 绘制当前手上拿的棋子
        if win == -1:
            if current_chess == 0:
                pg.draw.circle(screen, (255, 255, 255),
                               (current_i*50+50, current_j*50+50), 20)
            else:
                pg.draw.circle(screen, (0, 0, 0),
                               (current_i*50+50, current_j*50+50), 20)

        # 绘制棋盘上的棋子
        for i in range(len(chessboard[0])):
            for j in range(len(chessboard)):
                if chessboard[j][i] == 0:
                    pg.draw.circle(screen, (255, 255, 255),
                                   (i*50+50, j*50+50), 20)
                elif chessboard[j][i] == 1:
                    pg.draw.circle(screen, (0, 0, 0), (i*50+50, j*50+50), 20)

        # 判断输赢
        if win == -1:
            for i in range(len(chessboard)):
                for j in range(len(chessboard[0])):
                    if win != -1:
                        break
                    if chessboard[i][j] == -1:
                        continue
                    # 当前坐标棋子颜色
                    chess = chessboard[i][j]

                    # 判断横方向
                    n = 1
                    ii, jj = i, j
                    while jj-1 >= 0 and chessboard[ii][jj-1] == chess:
                        jj -= 1
                        n += 1
                    ii, jj = i, j
                    while jj+1 <= 14 and chessboard[ii][jj+1] == chess:
                        jj += 1
                        n += 1
                    if n == 5:
                        print('chess:', chess, 'win!')
                        win = chess

                    # 判断竖方向
                    n = 1
                    ii, jj = i, j
                    while ii-1 >= 0 and chessboard[ii-1][jj] == chess:
                        ii -= 1
                        n += 1
                    ii, jj = i, j
                    while ii+1 <= 14 and chessboard[ii+1][jj] == chess:
                        ii += 1
                        n += 1
                    if n == 5:
                        print('chess:', chess, 'win!')
                        win = chess

                    # 判断斜左上右下方向
                    n = 1
                    ii, jj = i, j
                    while ii-1 >= 0 and jj-1 >= 0 and chessboard[ii-1][jj-1] == chess:
                        ii -= 1
                        jj -= 1
                        n += 1
                    ii, jj = i, j
                    while ii+1 <= 14 and jj+1 <= 14 and chessboard[ii+1][jj+1] == chess:
                        ii += 1
                        jj += 1
                        n += 1
                    if n == 5:
                        print('chess:', chess, 'win!')
                        win = chess

                    # 判断斜右上左下方向
                    n = 1
                    ii, jj = i, j
                    while ii-1 >= 0 and jj+1 <= 14 and chessboard[ii-1][jj+1] == chess:
                        ii -= 1
                        jj += 1
                        n += 1
                    ii, jj = i, j
                    while ii+1 <= 14 and jj-1 >= 0 and chessboard[ii+1][jj-1] == chess:
                        ii += 1
                        jj -= 1
                        n += 1
                    if n == 5:
                        print('chess:', chess, 'win!')
                        win = chess

        # 绘制屏幕上方当前颜色提示
        if current_chess == 0:
            pg.draw.circle(screen, (255, 255, 255), (400, 25), 20)
        else:
            pg.draw.circle(screen, (0, 0, 0), (400, 25), 20)

        pg.display.update()  # 更新屏幕

    pg.quit()


if __name__ == "__main__":
    main()
