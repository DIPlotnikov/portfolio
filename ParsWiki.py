#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This program is for collecting metrics from a wiki page. It takes the page url and returns statistics in the form
# of a list: the number of images with the specified parameters (side greater than 200 pixels); the number of titles
# starting with a certain letter; the longest sequence of links standing behind each other; the number of lists not
# nested in other lists.

# D.Plotnikov 2021


from bs4 import BeautifulSoup
import requests


def parse(url):

    contents = requests.get(url).content
    soup = BeautifulSoup(contents, 'lxml')
    body = soup.find("div", id="bodyContent")

    def imgs(targetsoup):
        """
        the function returns the amount of images on a page with a width greater than 199 pixels.
        """
        images = targetsoup.findAll("img")
        count = 0
        for img in images:
            try:
                if int(img.attrs["width"]) >= 200:
                    count += 1
            except:
                continue
        return count

    def headers(targetsoup):
        """
        the function returns the amount of headers that meet the requirements.
        """
        headlines = ["h1", "h2", "h3", "h4", "h5", "h6"]
        requirements = ["E", "T", "C"]

        tags = targetsoup.findAll(headlines)
        return len(list(tag for tag in tags if tag.text[0] in requirements))

    def linkslen(targetsoup):
        """
        The function returns the length of the largest sequence of links (the "a" tag).
        """
        tags = targetsoup.findAll("a")
        maxseq = -1
        for tag in tags:
            count = 1
            seq = tag.find_next_siblings()
            for tag in seq:
                if tag.name == "a":
                    count += 1
                else:
                    break
            maxseq = max(maxseq, count)
        return maxseq

    def lists(targetsoup):
        """
        The function returns the number of lists that are not nested in other lists.
        """
        headers = ["ol", "ul"]
        tags = targetsoup.findAll(headers)
        count = 0
        for tag in tags:
            if not tag.find_parent(headers):
                count += 1
        return count

    return [imgs(body), headers(body), linkslen(body), lists(body)]


print(parse(" https://en.wikipedia.org/wiki/Stone_Age"))