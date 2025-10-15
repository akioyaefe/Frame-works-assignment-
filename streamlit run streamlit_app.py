# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load the dataset
# -------------------------------
df = pd.read_csv('students.csv')

# -------------------------------
# 2. App Title
# -------------------------------
st.title("E-Learning Student Performance Dashboard")
st.write("Explore student performance in online courses using interactive visualizations.")

# -------------------------------
# 3. Show Raw Data (optional)
# -------------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# -------------------------------
# 4. Filter by Course
# -------------------------------
courses = df['Course'].unique()
selected_course = st.selectbox("Select a course", courses)
course_df = df[df['Course'] == selected_course]

# -------------------------------
# 5. Display Average Score
# -------------------------------
st.subheader(f"Average Score for {selected_course}")
avg_score = course_df['Score'].mean()
st.write(f"{avg_score:.2f}")

# -------------------------------
# 6. Score Distribution
# -------------------------------
st.subheader(f"Score Distribution for {selected_course}")
fig, ax = plt.subplots()
sns.histplot(course_df['Score'], bins=5, kde=True, ax=ax)
st.pyplot(fig)

# -------------------------------
# 7. Study Hours vs Score
# -------------------------------
st.subheader(f"Study Hours vs Score for {selected_course}")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=course_df,
    x='Study_Hours',
    y='Score',
    hue='Completed',
    s=100,
    ax=ax2
)
st.pyplot(fig2)
