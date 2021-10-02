import requests


def get_file_commit(owner: str, repo: str, file_path: str = 'MLProject') -> int:
    """
    :param owner: e.g. apache
    :param repo: e.g. kafka
    :param file_path: e.g. in_repo_path_to_MLProject_file
    :return: count: int
    """
    res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits?path={file_path}')
    return len(res.json())  # len = count of commits


if __name__ == '__main__':
    repo_owner = 'apache'
    repo_name = 'skywalking'
    get_file_commit(owner=repo_owner, repo=repo_name, file_path="MLProject")
