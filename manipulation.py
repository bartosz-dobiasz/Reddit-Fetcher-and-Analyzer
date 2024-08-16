import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import database #testy

# Load dataframe
def load(conn):
    query = "SELECT * FROM posts;"
    df = pd.read_sql_query(query,conn)
    conn.close()
    return df

def bar_chart_combined(df):
    plt.figure(figsize=(12, 8))

    # Group by subreddit and attribute, then sum the number of comments
    grouped = df.groupby(['subreddit', 'attribute'])['num_comments'].sum().reset_index()

    # Create a combined label for x-axis
    grouped['combined'] = grouped['subreddit'] + ' - ' + grouped['attribute']

    # Plotting
    bars = plt.bar(grouped['combined'], grouped['num_comments'], color='skyblue', edgecolor='black')

    # Add labels and title
    plt.xlabel('Subreddit and Attribute')
    plt.ylabel('Number of Comments')
    plt.title('Number of Comments by Subreddit and Post Type')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Save the figure
    plt.tight_layout()
    plt.savefig('graphs/bar_chart_combined.png')
    plt.close()  # Close the figure to free memory


#conn = database.create_connection()
#df = load(conn)
#bar_chart(df,subreddit_names)
