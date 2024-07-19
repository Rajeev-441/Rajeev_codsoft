import tkinter as tk
from tkinter import messagebox
import pandas as pd
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Function to retrieve data from the database
def retrieve_data():
    conn = sqlite3.connect('movie_ratings.db')
    df = pd.read_sql_query("SELECT * FROM ratings", conn)
    conn.close()
    return df

# Function to recommend movies based on user preferences
def recommend(user):
    df = retrieve_data()
    # Normalize the data
    scaler = StandardScaler()
    ratings = df.drop('user', axis=1)
    normalized_ratings = scaler.fit_transform(ratings.T).T

    # Compute cosine similarity
    user_similarity = cosine_similarity(normalized_ratings)

    # Find the index of the given user
    user_index = df[df['user'] == user].index[0]

    # Calculate the weighted sum of ratings for each movie
    similar_users = user_similarity[user_index]
    weighted_sum = sum(similar_users[i] * normalized_ratings[i] for i in range(len(similar_users)))

    # Sort movies by weighted sum and return the top 3 recommendations
    recommendations = pd.Series(weighted_sum, index=ratings.columns).sort_values(ascending=False)
    return recommendations.index[:3]

# Function to handle recommendation button click
def recommend_movies():
    user = user_entry.get().strip()
    df = retrieve_data()
    if user in df['user'].values:
        recommendations = recommend(user)
        messagebox.showinfo("Recommendations", f"Top 3 recommended movies for {user}: {', '.join(recommendations)}")
    else:
        messagebox.showwarning("Invalid User", "User not found in the database.")

# Set up the main application window
root = tk.Tk()
root.title("Movie Recommendation System")

# User input
user_label = tk.Label(root, text="Enter User:")
user_label.pack(pady=5)
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

# Recommendation button
recommend_button = tk.Button(root, text="Recommend Movies", command=recommend_movies)
recommend_button.pack(pady=20)

# Start the application
root.mainloop()
