from utils.util import fetching_reddit_data, input_values_for_reddit, uploading_reddit_data_to_csv

if __name__ == '__main__':
    # loading relevant data values from json
    input_json = input_values_for_reddit('resources/data.json')

    # fetching data for those inputs from api calling
    data_for_all_tweets = fetching_reddit_data(input_json)

    # saving then into the csv file.
    uploading_reddit_data_to_csv(data_for_all_tweets)
