# Project Overview


### Description

This project is designed to interact with the Reddit API to collect and analyze post data, storing it in an SQLite database. The application features several components, each responsible for different tasks including database management, data fetching, databases, cloud computing and visualization.

### Components

#### `config.py`

This configuration file holds the credentials and settings necessary for interacting with both the Reddit API and the SQLite database:
- `REDDIT_CLIENT_ID`: The client ID for accessing the Reddit API.
- `REDDIT_CLIENT_SECRET`: The client secret for accessing the Reddit API.
- `REDDIT_USER_AGENT`: A user agent string that identifies the application to Reddit.
- `DATABASE_FILE`: The path to the SQLite database file.

#### `database.py`

This script provides functionality for managing the SQLite database:
- **Create a Database Connection**: `create_connection()` establishes a connection to the SQLite database specified in `config.py`.
- **Create a Table**: `create_table_posts(conn)` creates a table named `posts` if it does not already exist. This table is designed to store various attributes of Reddit posts, including title, URL, score, and more.
- **Convert Timestamps**: `convert_utc_to_local(utc_timestamp)` converts Unix timestamps into human-readable datetime strings.

#### `db_delete.py`

This script allows for the deletion of the SQLite database file if it exists:
- **Functionality**: The `dbdel()` function prompts the user to confirm if they want to delete the database. If confirmed, the database file is deleted. The script handles cases where the file might not exist and informs the user accordingly.

#### `fetch.py`

This script contains the `fetch_posts` function, which:
- **Input Parameters**:
  - `reddit`: An instance of the Reddit API client, created using `create_reddit_client`.
  - `conn`: A connection object to the SQLite database.
  - `subreddit_names`: A list of subreddit names from which to fetch posts.
  - `attribute`: The type of posts to fetch (e.g., `"top"`, `"hot"`, `"new"`, or `"rising"`).
  - `limit`: The number of posts to fetch from each subreddit.
- **Functionality**:
  - Validates the `attribute` parameter.
  - Fetches posts based on the specified attribute and limit.
  - Inserts the retrieved posts into the `posts` table in the database, handling duplicates and converting timestamps.

#### `reddit_client.py`

This script initializes and returns a Reddit client using the `praw` library:
- **Function**: The `create_reddit_client()` function sets up the Reddit client using credentials and configuration details from `config.py`. This client is used to interact with the Reddit API for fetching posts and accessing subreddit data.

#### `manipulation.py`

This script handles data loading and visualization:
- **`load(conn)`**: Loads all data from the `posts` table in the SQLite database into a pandas DataFrame and then closes the database connection.
- **`bar_chart_combined(df)`**: Generates a bar chart from the DataFrame. It groups the data by `subreddit` and `attribute`, sums the number of comments, and creates a combined x-axis label. The chart is styled and saved as an image file (`'graphs/bar_chart_combined.png'`).

### `main.py`

The `main.py` script orchestrates the overall workflow of the project:

1. **Database Setup**:
   - It starts by connecting to the Reddit API using the `create_reddit_client()` function from `reddit_client.py`.
   - Establishes a connection with the SQLite database using `create_connection()` from `database.py`.
   - Creates the `posts` table if it doesn't exist by calling `create_table_posts(conn)`.

2. **User Input**:
   - Prompts the user to enter subreddit names, which are then processed into a list.
   - Asks the user to choose a post type from a predefined list (`"top"`, `"hot"`, `"new"`, `"rising"`). It ensures the user input is valid before proceeding.
   - Requests the user to input the number of posts to fetch from each subreddit, validating that the input is a positive integer.

3. **Data Fetching**:
   - Calls the `fetch_posts()` function from `fetch.py` to retrieve posts from the specified subreddits and store them in the database.
   - If an error occurs during data fetching, it prints an error message and recursively calls `main()` to restart the process.

4. **Data Visualization**:
   - Loads the data from the database into a DataFrame using `manipulation.load(conn)`.
   - Generates a bar chart with `bar_chart_combined(df)` to visualize the number of comments grouped by subreddit and post type.

5. **Cleanup**:
   - Invokes `db_delete.dbdel()` to allow the user to delete the database if desired.
   - Closes the database connection to free up resources.

This script ensures a smooth workflow from data retrieval to visualization, with user-friendly prompts and robust error handling to manage different scenarios effectively.


