import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("🎬 Phim Nổi Tiếng")

# Thông tin sinh viên
st.write("*2121050918 - Bùi Quang Hùng*")

# Link website
st.write("### Liên kết đến trang: [Nhấn vào đây](https://2121050918buiquanghungapp.streamlit.app/)")

# Đọc dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

# Loại bỏ các giá trị thiếu
movies_data = movies_data.dropna(subset=['year', 'score', 'genre', 'budget', 'gross'])

# Chuyển cột year thành số nguyên
movies_data['year'] = movies_data['year'].astype(int)

# Bộ lọc
st.sidebar.header("🔍 Bộ Lọc")
genres = st.sidebar.multiselect("Chọn Thể Loại", options=sorted(movies_data['genre'].unique()), default=movies_data['genre'].unique()[:2])
score_range = st.sidebar.slider("Chọn Phạm Vi Điểm IMDb", float(movies_data['score'].min()), float(movies_data['score'].max()), (4.0, 9.0))
year_range = st.sidebar.slider("Chọn Phạm Vi Năm Phát Hành", int(movies_data['year'].min()), int(movies_data['year'].max()), (1980, 2020))

# Lọc dữ liệu
filtered_df = movies_data[
    (movies_data['genre'].isin(genres)) &
    (movies_data['score'].between(score_range[0], score_range[1])) &
    (movies_data['year'].between(year_range[0], year_range[1]))
]

# Hiển thị số lượng phim đã lọc
st.write(f"**Tổng Số Phim Được Tìm Thấy**: {len(filtered_df)}")

# Biểu đồ ngân sách trung bình theo thể loại
st.write("### Ngân Sách Trung Bình Theo Thể Loại")
avg_budget = filtered_df.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig1 = plt.figure(figsize=(10, 6))
plt.bar(genre, avg_bud, color='blue')
plt.xlabel('Thể Loại')
plt.ylabel('Ngân Sách Trung Bình (USD)')
plt.title('Ngân Sách Trung Bình Của Phim Theo Thể Loại')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Biểu đồ doanh thu trung bình theo thể loại
st.write("### Doanh Thu Trung Bình Theo Thể Loại")
avg_gross = filtered_df.groupby('genre')['gross'].mean().round()
avg_gross = avg_gross.reset_index()
genre_gross = avg_gross['genre']
avg_gross_val = avg_gross['gross']

fig2 = plt.figure(figsize=(10, 6))
plt.bar(genre_gross, avg_gross_val, color='green')
plt.xlabel('Thể Loại')
plt.ylabel('Doanh Thu Trung Bình (USD)')
plt.title('Doanh Thu Trung Bình Của Phim Theo Thể Loại')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Top 5 phim nổi tiếng theo điểm số
st.write("### Top 5 Phim Có Điểm Số Cao Nhất")
top_5_movies = filtered_df.nlargest(5, 'score')[['name', 'score', 'year', 'gross']]
st.table(top_5_movies)

# Hiển thị bảng dữ liệu đã lọc
st.subheader("Danh Sách Phim Đã Lọc")
st.dataframe(filtered_df[['name', 'genre', 'score', 'budget', 'gross', 'year']], use_container_width=True)
