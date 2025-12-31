import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện
st.set_page_config(page_title="Từ điển Đức-Việt Chuyên Sâu", page_icon="🇩🇪")

# Cấu hình Gemini API (Thay 'MÃ_API_CỦA_BẠN' bằng key bạn vừa lấy)
genai.configure(api_key=st.secrets["AIzaSyBlK6dy-OxAJsjt7zItZv-s-UJ8SUvSH-A"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇩🇪 Từ Điển Đức - Việt Chuyên Sâu")
word = st.text_input("Nhập từ vựng hoặc cụm từ:", placeholder="Ví dụ: Fernweh, verschandeln...")

if word:
    with st.spinner('Đang phân tích chuyên sâu...'):
        # Prompt này giúp AI trả về kết quả chuẩn xác như ảnh mẫu
        prompt = f"""
        Bạn là một chuyên gia ngôn ngữ học tiếng Đức. Hãy tra từ hoặc cụm từ: "{word}"
        Hãy trả về kết quả theo cấu trúc chính xác sau:
        1) Nghĩa thông dụng nhất bằng tiếng Việt: [Giải thích nghĩa chính xác]
           - Beispiel: [Câu ví dụ tiếng Đức hay] ([Dịch ví dụ sang tiếng Việt])
        2) Gợi ý dạng từ gần giống hoặc cấu tạo từ:
           - [Phân tích chi tiết: Nếu là danh từ hãy cho biết giống (der/die/das), nếu là động từ hãy cho biết cách chia hoặc tiền tố tách, nếu là từ ghép hãy phân tích các từ thành phần]
        """
        
        try:
            response = model.generate_content(prompt)
            result = response.text
            
            # Hiển thị kết quả theo phong cách chuyên nghiệp
            st.markdown("### Kết quả tra cứu:")
            st.info(result)
            
            # Link nghe phát âm luôn cần thiết
            yg_url = f"https://youglish.com/pronounce/{word.lower()}/german"
            st.markdown(f"**3) Nghe thử từ này:** [Click để nghe trên YouGlish]({yg_url})")
            
        except Exception as e:
            st.error("Có lỗi xảy ra khi kết nối với bộ não AI. Hãy kiểm tra API Key!")
