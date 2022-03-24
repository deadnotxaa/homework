# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    with open("text.txt", "r") as file:
        text = file.read().split()
        maxword = ""
        counter = 0

        for word in text:
            if len(word) > len(maxword):
                maxword = word

        for word in text:
            if word == maxword:
                counter += 1

        print(maxword, counter)