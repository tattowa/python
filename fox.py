import sys
import pygame
fox = Actor("fox")
# Actor で画像ファイル名を宣言し、変数foxに代入


def draw():
    # 画面に絵を描く（表示）draw()という関数を定義
    screen.clear()
    # 画面表示をきれいに　今はこういうものがある程度で
    fox.draw()
    # 変数foxに入れられたファイル画像を呼び出し表示


def replace_fox():
    # 絵の位置を置き換える関数　replace_foxという関数を定義
    fox.x = 400
    # x座標の位置
    fox.y = 500
    # y座標の位置


replace_fox()
