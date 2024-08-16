import reddit_client
import database
import fetch
import manipulation
import db_delete
# import os  # only for tests
# from config import DATABASE_FILE  # only for tests


def main():
    # os.remove(DATABASE_FILE)  # only for tests

    # Connect to redit API by praw

    reddit = reddit_client.create_reddit_client()

    # Establish or create connection with database

    conn = database.create_connection()

    # Create table if doesn't exist

    database.create_table_posts(conn)

    # User input on subreddits list
    subreddit_names = input("Enter subreddit names separated by commas: ").strip().split(',')
    subreddit_names = [name.strip() for name in subreddit_names]
    valid_attributes = ['top', 'hot', 'new', 'rising']

# Check users input for valid attributes
    while True:
        # Get a valid attribute from the user
        attribute = input(f"Choose post type ({', '.join(valid_attributes)}): ").strip().lower()
        if attribute in valid_attributes:
            break  # Exit the loop if a valid attribute is chosen
        else:
            print(f"Invalid choice. Please choose from: {', '.join(valid_attributes)}")

    while True:
        # Get a valid size limit from the user
        try:
            user_limit = int(input("Enter the number of posts: ").strip())
            if user_limit > 0:
                break  # Exit the loop if a valid positive integer is entered
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Load posts to the database
    try:
        fetch.fetch_posts(reddit, conn, subreddit_names, attribute=attribute, limit=user_limit)
        print("Data fetched")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("There is no /r sites")
        main()

    # Commit changes to db
    conn.commit()

    df = manipulation.load(conn)
    manipulation.bar_chart_combined(df)

    # db delete
    db_delete.dbdel()

    # close cursor and connection
    conn.close()


main()
