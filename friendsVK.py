#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This program creates statistics of friends on the site vk.com. The main function calc_age (uid) takes the user's
# nickname and returns a list of sets, in which the first value is the age, and the second is the number of friends
# with this age. In addition the program contains several functions for working with the api vk.com.

# D.Plotnikov 2021

import requests
import time

# settings
api = "https://api.vk.com/method/"
token = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
v = '5.71'


def get_id(uid):
    """getting the user id by username"""

    try:
        user_info = requests.get(
            f"{api}users.get?"
            f"v={v}&"
            f"access_token={token}"
            f"&user_ids={uid}")
        user_id = user_info.json()['response'][0]["id"]
        return user_id
    except:
        print("error of getting id")


def get_friendlist(id):
    """getting information about all open friends in dictionary format"""

    try:
        fields = "bdate"
        friends = requests.get(
            f"{api}friends.get?"
            f"v={v}&access_token={token}"
            f"&user_id={id}"
            f"&fields={fields}&")
        friendlist = friends.json()['response']['items']
        return friendlist
    except:
        print("error of getting friendlist")


def get_friends_ages(friendlist):
    """getting a list of your friends ' ages"""

    try:
        friends_ages = []
        for friend in friendlist:
            try:
                year = friend["bdate"].split(".")[2]
                age = int(time.ctime()[-4:]) - int(year)
                friends_ages.append(age)
            except:
                continue
        return friends_ages
    except:
        print("error of getting friends ages")


def calc_age(uid):
    """
    counting statistics of the ages of friends
    in the format [(age, amount of friends of this age)]
    """

    try:
        user_id = get_id(uid)
        user_friendlist = get_friendlist(user_id)
        friends_ages = get_friends_ages(user_friendlist)

        age_list = []
        ages = set(friends_ages)

        for age in ages:
            age_list.append((int(age), friends_ages.count(age)))
        age_list.sort(key=lambda x: (-x[1], x[0]))

        return age_list
    except:
        print("error of calc age")


