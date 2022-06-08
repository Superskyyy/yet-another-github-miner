from apis.github_api import get_file_commit
from apis.github_graphql import get_commit_count

# Just a sample until scraper works
if __name__ == '__main__':
    # repo_owner = 'pabgonza'
    # repo_name = 'udacity_mlops'
    # path = '/lesson2_ml_pipelines/lesson-5-final-pipeline-release-and-deploy/exercises/exercise_14/solution_pg/random_forest/MLproject'
    # # Execute the query on the transport
    # print(f"Criteria stats for project {repo_owner}:{repo_name}")
    # print(f"Repo commit total: {get_commit_count(owner=repo_owner, repo=repo_name)}")
    # print(f"MLProject file commit total: {get_file_commit(owner=repo_owner, repo=repo_name, file_path=path)}")


    from spider.miner_requests import scrape
    base_url = 'https://api.github.com/search/'
    rate_limit_api = 'https://api.github.com/rate_limit'
    args = '+in:file +size:1..150'
    scrape(base_url=base_url, type='code',args=args)