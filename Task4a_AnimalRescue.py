import pandas as pd
import matplotlib.pyplot as plt


def load_and_explore_data():
    df = pd.read_csv("task 4a anamals.csv")
    df = df.dropna()
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    print("\nFirst 5 rows of the dataset")
    print(df.head())

    print("\nColumn names")
    print(df.columns)

    print("\nDataset summary")
    print(df.info())

    return df


def average_interactions_per_day(df):
    avg_likes = df.groupby("Date")["Likes"].mean()
    avg_shares = df.groupby("Date")["Shares"].mean()
    avg_comments = df.groupby("Date")["Comments"].mean()

    print("\nAverage Likes per day")
    print(avg_likes)

    print("\nAverage Shares per day")
    print(avg_shares)

    print("\nAverage Comments per day")
    print(avg_comments)

    return avg_likes, avg_shares, avg_comments


def total_interactions_by_post_type(df):
    df["Total Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
    totals = df.groupby("Post Type")["Total Interactions"].sum()

    print("\nTotal interactions by post type")
    print(totals)

    return totals


def interactions_by_time_of_day(df):
    df["Total Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
    time_data = df.groupby("Time")["Total Interactions"].mean()

    print("\nAverage interactions by time of day")
    print(time_data)

    return time_data


def plot_average_likes(avg_likes):
    plt.figure()
    plt.plot(avg_likes.index, avg_likes.values, marker="o")
    plt.title("Average Likes Per Day")
    plt.xlabel("Date")
    plt.ylabel("Average Likes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_total_interactions_by_post_type(totals):
    plt.figure()
    totals.plot(kind="bar")
    plt.title("Total Interactions by Post Type")
    plt.xlabel("Post Type")
    plt.ylabel("Total Interactions")
    plt.tight_layout()
    plt.show()


def plot_interactions_by_time(time_data):
    plt.figure()
    time_data.plot(kind="bar")
    plt.title("Average Interactions by Time of Day")
    plt.xlabel("Time of Day")
    plt.ylabel("Average Interactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    df = load_and_explore_data()

    avg_likes, avg_shares, avg_comments = average_interactions_per_day(df)
    post_type_totals = total_interactions_by_post_type(df)
    time_data = interactions_by_time_of_day(df)

    plot_average_likes(avg_likes)
    plot_total_interactions_by_post_type(post_type_totals)
    plot_interactions_by_time(time_data)

    print("\nAnalysis complete")


main()
