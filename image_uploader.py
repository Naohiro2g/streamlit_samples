import os
import streamlit as st
from PIL import Image


IMG_PATH = 'images'
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)

def main():
    st.markdown('# 画像を保存するデモ')
    file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])

    if not file:
        st.error(f'エラー')
    else:
        st.markdown(f'{file.name} をアップロードしました.')
        img_path = IMG_PATH + "/" + file.name
        img_path = os.path.join(IMG_PATH, file.name)
        # 画像を保存する
        with open(img_path, 'wb') as f:
            f.write(file.read())
        # 保存した画像を表示
        img = Image.open(img_path)
        st.image(img)

if __name__ == '__main__':
    main()
