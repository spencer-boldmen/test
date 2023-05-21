def solve(st):
    chars = {char: abs(st.find(char) - st.rfind(char)) for char in st}
    return max(sorted(chars), key=lambda x: chars[x])