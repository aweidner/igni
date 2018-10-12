import requests

GITIGNORE_API = 'https://www.gitignore.io/api'
GITIGNORE_LIST_SEPERATOR = ','
LIST_REQUEST = 'list'
COMPLETION_SEPERATOR = ' '

def call_gitignore(*arguments):
    comma_deliniated_arguments = ",".join(arguments)
    return requests.get(f'{GITIGNORE_API}/{comma_deliniated_arguments}').text


def list_all():
    return call_gitignore(LIST_REQUEST)


def completion():
    word_list = list_all().replace(GITIGNORE_LIST_SEPERATOR, COMPLETION_SEPERATOR).replace("\n", COMPLETION_SEPERATOR)
    return f'#/usr/bin/env bash\ncomplete -W "{word_list}" igni' 
