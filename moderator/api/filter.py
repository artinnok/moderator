from datetime import datetime, timedelta


def filter_post_list(post_list):
    return (post['id'] for post in post_list
            if post['comments']['count'])


# TODO переписываем
def filter_comment_list(comment_list, public):
    out = []
    for comment in comment_list:
        if is_liked(comment, public.like) and is_past(comment, public.minute):
            out.append(comment['id'])
    return out


def flatten(comment_list):
    return (item for sub in comment_list for item in sub)


def is_liked(comment, count):
    return comment['likes']['count'] < count


def is_past(comment, minutes):
    return datetime.now() - datetime.fromtimestamp(comment['date']) >= timedelta(minutes=minutes)
