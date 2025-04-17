import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Famous Movie")
st.write("*2121050918 - Bùi Quang Hùng*")

# Link website
st.write("### Link đến trang demo có bình luận: [Click here](https://2121050918buiquanghungapp.streamlit.app/)")

# Đọc dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

# Loại bỏ các giá trị thiếu
movies_data = movies_data.dropna()

# Bộ lọc
st.sidebar.header("🔍 Filters")
genres = st.sidebar.multiselect("Select Genres", options=sorted(movies_data['genre'].unique()), default=movies_data['genre'].unique()[:2])
score_range = st.sidebar.slider("Select IMDb Score Range", float(movies_data['score'].min()), float(movies_data['score'].max()), (4.0, 9.0))

# Lọc dữ liệu
filtered_df = movies_data[(movies_data['genre'].isin(genres)) & (movies_data['score'].between(score_range[0], score_range[1]))]

# Hiển thị số lượng phim đã lọc
st.write(f"**Total Movies Found**: {len(filtered_df)}")

# Biểu đồ ngân sách trung bình theo thể loại
st.write("### Average Movie Budget, Grouped by Genre")
avg_budget = filtered_df.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize=(10, 6))
plt.bar(genre, avg_bud, color='blue')
plt.xlabel('Genre')
plt.ylabel('Average Budget (USD)')
plt.title('Average Budget of Movies by Genre')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Filtered Movies")
st.dataframe(filtered_df[['name', 'genre', 'score', 'budget']], use_container_width=True)
