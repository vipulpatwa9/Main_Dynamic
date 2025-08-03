import streamlit as st

# --- Constants ---
v1 = 70123
v2 = 33
v3 = 3
v4 = 28786
VALID_ID = "Admin"
VALID_PASSWORD = "9229"

# --- Password Generator Logic ---
def generate_password(a: int, b: int, mode: str) -> int:
    result = 0
    x = a + b + v1
    buffer = [
        (x & 0xFF000000) >> 24,
        (x & 0x00FF0000) >> 16,
        (x & 0x0000FF00) >> 8,
        (x & 0x000000FF)
    ]
    for val in buffer:
        result += val

    if mode == "2-digit":
        x = v2 * b
        result ^= x
        x = v3 * b
        result += x
    elif mode == "3-digit":
        x = (v2 + 3) * b
        result ^= x
        x = (v3 + 1) * b
        result += x

    result ^= v4
    return result

# --- Login Logic ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Secure Login")

    login_id = st.text_input("Login ID")
    password = st.text_input("Password", type="password", max_chars=6)

    if st.button("Login"):
        if login_id == VALID_ID and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid Login ID or Password")

# --- Main App (After Login) ---
else:
    st.title("🔧 Dynamic Lock Generator")

    machine_no = st.number_input("Enter Machine Number", step=1, format="%d")
    counter_no = st.number_input("Enter Counter Number", step=1, format="%d")

    if st.button(" 2-Digit "):
        result = generate_password(machine_no, counter_no, mode="2-digit")
        st.success(f"2-digit Lock Code: {result}")

    if st.button("3-Digit "):
        result = generate_password(machine_no, counter_no, mode="3-digit")
        st.success(f"3-digit Lock Code: {result}")

    if st.button("Logout 🔓"):
        st.session_state.logged_in = False
        st.rerun()
