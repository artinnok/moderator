def filter_post_list(post_list):
    return [post['id'] for post in post_list
            if post['comments']['count']]


def filter_comment_list(comment_list):
    comment_list = [item['response']['items'][0] for item in comment_list]
    return [comment['id'] for comment in comment_list if comment['likes']['count'] < 5]
