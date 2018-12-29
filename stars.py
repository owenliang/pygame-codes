# -*- coding: utf-8 -*-
import pygame
import random
import math


def init_game():
    # 初始化pygame各个模块
    pygame.init()

    # 设置800 * 600分辨率
    global screen
    screen = pygame.display.set_mode((800, 600))

    # 帧率控制
    global clock
    clock = pygame.time.Clock()

    # 随机数种子
    random.seed()


def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # 一个白色的点
        self.image = pygame.Surface((1, 1))
        self.image.set_at((0, 0), (250, 240, 200))

        self.rect = None
        self.x_speed = None
        self.y_speed = None

        self.reset()

    def reset(self):
        # 矩形
        self.rect = self.image.get_rect()
        # 放到屏幕中心
        self.rect.center = screen.get_rect().center

        # 随机的速度, 0.1~1.5
        self.x_speed = (random.randint(1, 15) / 10) * (-1 if random.random() < 0.5 else 1)
        self.y_speed = (random.randint(1, 15) / 10) * (-1 if random.random() < 0.5 else 1)
        # 从中心附近开始向外迸发
        self.rect.x += self.x_speed * 10
        self.rect.y += self.y_speed * 10

    def move(self):
        # 加速
        self.x_speed *= 1.03
        self.y_speed *= 1.03
        # 移动
        new_rect = self.rect.move(int(self.x_speed), int(self.y_speed))
        self.rect = new_rect
        # 判断离开屏幕
        if self.rect.left <= 0 or self.rect.right >= screen.get_rect().right or self.rect.top <= 0 or self.rect.bottom >= screen.get_rect().bottom:
            self.reset()

    def update(self):
        self.move()


def init_sprite():
    # 一组流星
    global stars
    stars = pygame.sprite.Group()

    # 创建若干流星
    for x in range(0, 100):
        stars.add(Star())

    # 把星星画到screen上
    stars.draw(screen)


def init_background():
    global bg
    # 创建背景surface
    bg = pygame.Surface(screen.get_rect().size)
    # 填充黑色
    bg.fill((0, 0, 0))
    # 画到屏幕上
    bg.blit(screen, (0, 0))


def main():
    # 初始化游戏
    init_game()
    # 初始化背景
    init_background()
    # 初始化小精灵
    init_sprite()

    while True:
        # 控制帧率
        clock.tick(60)
        # 处理事件
        if not handle_event():
            break
        # 在screen中用背景擦除精灵
        stars.clear(screen, bg)
        # 计算精灵的新位置
        stars.update()
        # 绘制精灵
        stars.draw(screen)
        # 刷新screen
        pygame.display.flip()


# 程序入口
if __name__ == '__main__':
    main()
