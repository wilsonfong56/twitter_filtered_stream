from twapi import api
import re 

def timeline_search(search_str: str, re_expression: str) -> 'list[str]':
    timeline = api.home_timeline()
    search_list = []

    for status in timeline:
        if search_str in status.text:
            terms = re.findall(re_expression, status.text.upper())
            search_list.extend(terms)
    return search_list