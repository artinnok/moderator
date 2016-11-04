from datetime import datetime, timedelta


def filter_post_list(post_list):
    return (post['id'] for post in post_list
            if post['comments']['count'])


def filter_comment_list(comment_list):
    out = []
    for comment in comment_list:
        if is_liked(comment, 2) and is_past(comment, 5):
            out.append(comment['id'])
        elif is_liked(comment, 5) and is_past(comment, 10):
            out.append(comment['id'])
    return out


def flatten(comment_list):
    return (item for sub in comment_list for item in sub)


def is_liked(comment, count):
    return comment['likes']['count'] < count


def is_past(comment, minutes):
    return datetime.now() - datetime.fromtimestamp(comment['date']) >= timedelta(minutes=minutes)
