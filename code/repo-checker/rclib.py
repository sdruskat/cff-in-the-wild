import requests

'''
Simple function which gets the contents from a file in a github repo, and returns None if 
it cannot be found.
'''
def get_file_from_repo(user, repo, file_name):
    repo_info = requests.get('https://api.github.com/repos/{}/{}'.format(user,repo))
    contents = repo_info.json()['contents_url']
    file_info = requests.get(contents.replace('{+path}','{}').format(file_name))
    download_url = file_info.json()['download_url']
    file_contents = requests.get(download_url).text
    return file_contents

