import database


def fetch_posts(reddit, conn, subreddit_names, attribute="top", limit=10):

    c = conn.cursor()

    valid_attributes = ["top", "hot", "new", "rising"]

    if attribute not in valid_attributes:
        raise ValueError(f"Invalid attribute. Chose from {', '.join(valid_attributes)}")

    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        user_posts = getattr(subreddit, attribute)(limit=limit)

        # insert posts into db

        for post in user_posts:
            time = database.convert_utc_to_local(post.created_utc)
            c.execute('''
                INSERT OR IGNORE INTO posts (
                    title, selftext, url, permalink, id, score, num_comments,
                    created_utc, author, subreddit, is_video, link_flair_text, over_18, attribute
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
                post.title,
                post.selftext,
                post.url,
                post.permalink,
                post.id,
                post.score,
                post.num_comments,
                time,
                # Convert author to string if it's not None
                str(post.author) if post.author else None,
                post.subreddit.display_name,
                post.is_video,
                post.link_flair_text,
                post.over_18,
                attribute
            ))
    conn.commit()
    c.close()
