#!/usr/bin/python3
import requests as r
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = r.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = r.get(url)
    if response.status_code == 200:
        data = response.json()
        dic = [{'id': r['id'], 'title': r['title'], 'body': r['body']}
               for r in data]
        with open("posts.csv", 'w', newline='', encoding='utf-8') as file:
            headers = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(dic)
