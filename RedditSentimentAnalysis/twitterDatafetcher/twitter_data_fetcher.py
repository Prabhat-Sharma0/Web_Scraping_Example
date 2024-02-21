import praw


def getting_reddit_data_from_api(subreddit, tags, count):
    # Setting Reddit API credentials
    client_id = 'sWNDt6ADMihmO4aUgbq72A'
    client_secret = '0xPK5CVTzo6W4zlip2-2XOFWtVuQkA'
    user_agent = 'data_sentiment_analysis/1.0.0'

    # connecting to redit using praw lib
    reddit_api = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    # for sorting all the data in it.
    subreddit_data = []

    for tag in tags:
        results = reddit_api.subreddit(subreddit).search(f'title:{tag} OR selftext:{tag}', sort='new', limit=count)
        for result in results:

            # Fetching Comments from single reddit
            result.comments.replace_more(limit=None)
            comment_count = 0
            comment_data_list = []
            for comment in result.comments.list():
                if comment_count > 10:
                    break
                comment_data = {
                    'Subreddit': subreddit,
                    'Reddit_Title': result.title,
                    'CommentAuthor': str(comment.author),
                    'Comment': comment.body
                }
                comment_count += 1
                comment_data_list.append(comment_data)

            # adding relevant data for reddit
            reddit_data = {
                'Subreddit': subreddit,
                'Title': result.title,
                'URL': result.url,
                'Score': result.score,
                'No. of Comments': result.num_comments,
                'Author': str(result.author),
                'CreationTime': result.created_utc,
                'Body': result.selftext,
                'Comment Data': comment_data_list
            }

            # check if each data have comments more than 10 for better analysis
            if reddit_data['No. of Comments'] > 10:
                subreddit_data.append(reddit_data)

    return subreddit_data
