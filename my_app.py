import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Phim Nổi Tiếng")
st.write("*2121050918 - Bùi Quang Hùng*")

# Link website
st.write("### Liên kết đến trang: [Nhấn vào đây](https://2121050918buiquanghungapp.streamlit.app/)")

movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

# Loạigiá trị thiếu
movies_data = movies_data.dropna()

# Bộ lọc
st.sidebar.header("Bộ Lọc")
genres = st.sidebar.multiselect("Chọn Thể Loại", options=sorted(movies_data['genre'].unique()), default=movies_data['genre'].unique()[:2])
score_range = st.sidebar.slider("Chọn Phạm Vi Điểm IMDb", float(movies_data['score'].min()), float(movies_data['score'].max()), (4.0, 9.0))

# Lọc dữ liệu
filtered_df = movies_data[(movies_data['genre'].isin(genres)) & (movies_data['score'].between(score_range[0], score_range[1]))]
st.write(f"**Tổng Số Phim Được Tìm Thấy**: {len(filtered_df)}")

# Biểu đồ ngân sách trung bình theo thể loại
st.write("### Ngân Sách Trung Bình Theo Thể Loại")
avg_budget = filtered_df.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize=(10, 6))
plt.bar(genre, avg_bud, color='blue')
plt.xlabel('Thể Loại')
plt.ylabel('Ngân Sách Trung Bình (USD)')
plt.title('Ngân Sách Trung Bình Của Phim Theo Thể Loại')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Danh Sách Phim Đã Lọc")
st.dataframe(filtered_df[['name', 'genre', 'score', 'budget']], use_container_width=True)
