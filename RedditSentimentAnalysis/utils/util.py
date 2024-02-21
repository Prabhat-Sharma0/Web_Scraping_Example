import json

import pandas as pd

from twitterDatafetcher.twitter_data_fetcher import getting_reddit_data_from_api


def input_values_for_reddit(file):
    data_from_json = json.load(open(file))
    main_data = {}
    for i in data_from_json['inputData'][0]:
        # new_data = data_from_json['inputData'][0][i].replace('\n', "' OR '")
        new_data = data_from_json['inputData'][0][i].split('\n')
        main_data[i] = new_data

    return main_data


def fetching_reddit_data(input_json):
    all_reddit_data = {}
    for data in input_json:
        tags = input_json[data]
        reddit_count = 100
        print(f'Tags for fetching the data for subreddit "{data}" is: "{tags}"')

        # fetching data for each subreddit value with its tags
        reddit_for_type = getting_reddit_data_from_api(data, tags, reddit_count)
        all_reddit_data[data] = reddit_for_type

        print(f'Reddit posts for type "{data}" has been fetched.') if not reddit_for_type else print(
            f'Reddit posts for type "{data}" not found!!!!!!!!')

    return all_reddit_data


def uploading_reddit_data_to_csv(all_tweets):
    all_df = pd.DataFrame()
    # columns = ['Subreddit', 'Title', 'URL', 'Score', 'NumComments', 'Author', 'CreationTime', 'Body', 'Subreddit', 'Reddit_Title', 'CommentAuthor', 'Comment']
    for data in all_tweets:
        value_df = pd.DataFrame(all_tweets[data])
        if all_df.empty:
            all_df = value_df
        else:
            all_df = pd.concat([all_df, value_df], ignore_index=True)

    # loading data into csv file for further use.
    all_df.to_csv('resources/output.csv', index=False)

    return all_df
