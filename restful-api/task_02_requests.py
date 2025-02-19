#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""


import requests
import csv


def fetch_and_print_posts():
    """Function that fetches all post from JSONPlaceholder"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        print("Status code: {}".format(r.status_code))
        posts = r.json()
        for post in posts:
            print(post['title'])

    else:
        print("Failed to fetch posts. Status code: {}".format(r.status_code))


def fetch_and_save_posts():
    """Function that fetches all post from JSONPlaceholder"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        data_to_save = [{'id': post['id'], 'title': post['title'],
                         'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data_to_save)
    else:
        print("Failed to fetch posts. Status code: {}".format(r.status_code))
