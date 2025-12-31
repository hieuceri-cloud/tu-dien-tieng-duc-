import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_glosbe_data(word):
    url = f"https://vi.glosbe.com/de/vi/{word.lower()}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200: return None
        soup = BeautifulSoup(response.text, 'html.parser')
        meaning = soup.find('h3', class_='translation__item__phrase')
        meaning_text = meaning.get_text(strip=True) if meaning else "Không tìm thấy nghĩa"
        example_de = soup.find('div', class_='dir-ltr')
        ex_de = example_de.get_text(strip=True) if example_de else "Chưa có ví dụ."
        return {"meaning": meaning_text, "example": ex_de}
    except:
        return None

st.set_page_config(page_title="Từ điển Đức-Việt", page_icon="🇩🇪")
st.title("🇩🇪 Từ điển Đức - Việt Thông Minh")

word = st.text_input("Nhập từ vựng cần tra (ví dụ: Fernweh, verschandeln):")

if word:
    with st.spinner('Đang tìm kiếm...'):
        data = get_glosbe_data(word)
        if data:
            st.success(f"**1) Nghĩa tiếng Việt:** {data['meaning']}")
            st.info(f"**2) Ví dụ:** {data['example']}")
            yg_url = f"https://youglish.com/pronounce/{word.lower()}/german"
            st.markdown(f"**3) Nghe phát âm:** [Bấm để nghe trên YouGlish]({yg_url})")
            st.components.v1.iframe(yg_url, height=500)
        else:
            st.error("Rất tiếc, không tìm thấy dữ liệu cho từ này.")
