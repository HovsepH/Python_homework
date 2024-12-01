import requests
url= "https://jsonplaceholder.typicode.com/"


def make_get_request(url):
    return requests.get(url).json()

def filter_titles(post):
    words = post["title"].split()
    return len(words) >5

def filter_bodies(post):
    return post["body"].count('\n') >=3

def filter_response(post_list, filter_function):
    posts = filter(filter_function, post_list)
    return list(map(lambda p: p["title"], posts))

def create_post(url, post_data):
    return requests.post(url, post_data)

def pudate_post(url, new_post):
    return requests.put(url, new_post)

def delete_post(url):
    return requests.delete(url)


response = make_get_request(url+'posts/')
specific_titles = filter_response(response, filter_titles)
print(specific_titles)

specific_posts = filter_response(response, filter_bodies)
print(specific_posts)


data = {
    "title": "sit vel voluptatem et non libero",
    "body": """debitis excepturi ea perferendis harum libero optio
        eos accusamus cum fuga ut sapiente repudiandae
        et ut incidunt omnis molestiae
        nihil ut eum odit""",
    "userId": "510"
}

post_result = create_post(url+"posts/", data)
print(post_result.status_code)



new_post = {
    "title": "sit vel voluptatem et non libero",
    "body": """debitis excepturi ea perferendis harum libero optio
        eos accusamus cum fuga ut sapiente repudiandae
        et ut incidunt omnis molestiae
        nihil ut eum odit""",
    "userId": "510",
    "id": "1",
}

put_result = pudate_post(url+"posts/1", new_post)
print(put_result.status_code)

index = 2
delete_result = delete_post(url+ f"posts/{index}")
print(delete_result.status_code)