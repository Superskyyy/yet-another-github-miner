from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from credentials import GITHUB_TOKEN


def get_commit_count(owner: str, repo: str) -> int:
    """
    Total commits of a target repo
    :param owner: e.g. apache
    :param repo: e.g. kafka
    :return: count
    """
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://api.github.com/graphql",
                                 headers={'Authorization': f'bearer {GITHUB_TOKEN}'}
                                 )

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        f"""
    {{ 
      {repo}: repository(owner: "{owner}", name: "{repo}") {{ 
        ...RepoFragment 
      }} 
    }} 
    
    fragment RepoFragment on Repository {{
      name 
      defaultBranchRef {{ 
        name 
        target {{ 
          ... on Commit {{ 
            id 
            history(first: 0) {{ 
              totalCount 
            }}
          }}
        }}
      }}
    }} 
    """
    )
    result = client.execute(query)

    return result[repo]['defaultBranchRef']['target']['history']['totalCount']
