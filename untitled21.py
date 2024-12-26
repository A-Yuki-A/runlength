# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TafCF5e3Jzcxi4-WYSNMJpyOjiG0PifD
"""

import streamlit as st

# ランレングス圧縮を行う関数
def run_length_encoding(input_str):
    encoded_str = ''
    count = 1
    encoded_data = []

    if len(input_str) == 0:
        return encoded_str, encoded_data

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            encoded_str += input_str[i - 1] + str(count)
            encoded_data.append((input_str[i - 1], count))
            count = 1

    encoded_str += input_str[-1] + str(count)
    encoded_data.append((input_str[-1], count))

    return encoded_str, encoded_data

# 圧縮率を求める関数
def calculate_compression_rate(input_str, encoded_str):
    original_size = len(input_str)
    compressed_size = len(encoded_str)
    compression_rate = (1 - compressed_size / original_size) * 100
    return original_size, compressed_size, compression_rate

# Streamlit アプリケーションの UI
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            font-size: 11px;
        }
        .stButton>button {
            font-size: 11px;
        }
        .stTextInput>div>input {
            font-size: 11px;
        }
        .stTextArea>div>textarea {
            font-size: 11px;
        }
        .stMarkdown {
            font-size: 11px;
        }
        .stHeader {
            font-size: 11px;
        }
    </style>
""", unsafe_allow_html=True)

st.title('📦 ランレングス圧縮')

# 入力例を追加
st.markdown("### 例: `AAABBBCCCDDD` のように、半角アルファベットを入力してください。")

# 入力
input_str = st.text_input('✏️ 半角アルファベットを入力してください:')

if input_str:
    # 圧縮処理
    encoded_str, encoded_data = run_length_encoding(input_str)
    original_size, compressed_size, compression_rate = calculate_compression_rate(input_str, encoded_str)

    # 元のデータ
    st.header('🗃️ 元のデータ')
    st.info(f'入力データ: **{input_str}**')
    st.write(f'元のデータのサイズ: **{original_size} バイト**')

    # 圧縮後のデータ
    st.header('🔧 圧縮後のデータ')
    st.success(f'ランレングス圧縮後のデータ: **{encoded_str}**')
    st.write(f'圧縮後のデータのサイズ: **{compressed_size} バイト**')

    # 圧縮率
    st.header('📉 圧縮率の結果')
    st.latex(r'''
    圧縮率 = \frac{{\text{{元のサイズ}} - \text{{圧縮後のサイズ}}}}{{\text{{元のサイズ}}}} \times 100
    ''')
    st.latex(rf'''
    圧縮率 = \frac{{{original_size} - {compressed_size}}}{{{original_size}}} \times 100 = {compression_rate:.2f}\%
    ''')
    st.warning(f'圧縮率: **{compression_rate:.2f}%**')

    # 圧縮後のデータ詳細
    st.header('🔍 圧縮後のデータ詳細')
    st.table([{'文字': char, '出現回数': count} for char, count in encoded_data])

    # 注意事項
    st.caption('※ 半角アルファベット以外の入力は無視されます。')

# 問題と選択肢
options = {
    "1. ABCDEFGH": "最適ではありません。異なる文字が多いため圧縮効果は低いです。",
    "2. ABABABAB": "最適ではありません。繰り返しのパターンがあるが、長さが少ないため圧縮効果が低いです。",
    "3. AAAABBBCCCC": "最適なデータです。繰り返しのパターンがあるので圧縮効果が高いです。",
    "4. ABCCBAABC": "最適ではありません。繰り返しが少なく、圧縮効果が低いです。"
}

# 選択肢を表示
choice = st.radio(
    "問題：圧縮に最適なデータを選んでください",
    list(options.keys())
)

# 送信ボタン
submit_button = st.button(label='送信')

# 正誤判定と解説
if submit_button:
    correct_answer = "3. AAAABBBCCCC"
    if choice == correct_answer:
        st.success(f'✅ 正解！圧縮に最適なデータは `{correct_answer}` です。')
    else:
        st.error(f'❌ 不正解！正解は `{correct_answer}` です。')

    # 解説
    st.subheader('🔍 解説')
    st.write(f"正解: `{correct_answer}`")

    st.write("""
    ランレングス圧縮は、データに繰り返しのパターンがある場合に非常に効果的です。特に、同じ文字が連続して現れる場合に最適です。

    - **最適なデータ**は、繰り返しの文字列（例：`AAAABBBCCCC`）です。このようなデータは圧縮されるサイズが小さくなり、圧縮率が非常に高くなります。
    - **圧縮効果が低いデータ**は、異なる文字が多く含まれるデータ（例：`ABABABAB` や `ABCCBAABC`）です。この場合、各文字が個別に現れるため、圧縮率は低くなります。
    """)

