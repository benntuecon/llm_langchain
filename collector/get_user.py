
from collector.utils import GithubUser
from config import GITHUB_PARAMS


def get_user():
    user = GithubUser(GITHUB_PARAMS['user'])
    return user
