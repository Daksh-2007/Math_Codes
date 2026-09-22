import streamlit as st

st.set_page_config(page_title="Cramer's Rule Calculator", page_icon="🧮", layout="centered")

# Custom CSS for input box sizing and tight spacing
st.markdown("""
    <style>
    /* Main container max width */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 650px !important;
    }

    /* Keep matrix row elements side-by-side */
    [data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: 8px !important;
        width: fit-content !important;
        margin: 0 auto !important;
    }

    /* Column container width */
    div[data-testid="stColumn"] {
        min-width: 0px !important;
        flex: 0 0 auto !important;
    }

    /* Number input dimensions */
    div[data-testid="stNumberInput"] {
        width: 60px !important;
        margin-bottom: 0px !important;
    }

    div[data-testid="stElementContainer"] {
        margin-bottom: 6px !important;
        display: flex;
        justify-content: center;
    }

    /* Input element interior styling */
    div[data-testid="stNumberInput"] input {
        padding: 4px 2px !important;
        height: 36px !important;
        font-size: 0.95rem !important;
        text-align: center !important;
        border-radius: 6px !important;
    }

    /* Hide step arrow controls */
    div[data-testid="stNumberInput"] button {
        display: none !important;
    }

    /* Section header styling */
    h3 {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.1rem !important;
        text-align: center !important;
    }

    hr {
        margin-top: 1.25rem !important;
        margin-bottom: 1.25rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Cramer's Rule Calculator", anchor=False)

def determinant(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

def var_matrix(matrix, B, col):
    var_M = [row[:] for row in matrix]
    for i in range(len(matrix)):
        var_M[i][col - 1] = B[i][0]
    return var_M

size = st.radio("Select System Size:", options=[2, 3], format_func=lambda x: f"{x}x{x} System", horizontal=True)

# Native Streamlit columns: Side-by-side on desktop, stacked on mobile
col_A, col_B = st.columns([2, 1])

A = []
with col_A:
    st.subheader("A", anchor=False)
    if size == 2:
        for i in range(2):
            c1, c2 = st.columns([1, 1])
            r1 = c1.number_input(f"A[{i}][0]", value=0, key=f"a_{i}_0", label_visibility="collapsed")
            r2 = c2.number_input(f"A[{i}][1]", value=0, key=f"a_{i}_1", label_visibility="collapsed")
            A.append([r1, r2])
    else:
        for i in range(3):
            c1, c2, c3 = st.columns([1, 1, 1])
            r1 = c1.number_input(f"A[{i}][0]", value=0, key=f"a_{i}_0", label_visibility="collapsed")
            r2 = c2.number_input(f"A[{i}][1]", value=0, key=f"a_{i}_1", label_visibility="collapsed")
            r3 = c3.number_input(f"A[{i}][2]", value=0, key=f"a_{i}_2", label_visibility="collapsed")
            A.append([r1, r2, r3])

B = []
with col_B:
    st.subheader("B", anchor=False)
    for i in range(size):
        cb = st.columns(1)[0]
        b_val = cb.number_input(f"B[{i}]", value=0, key=f"b_{i}", label_visibility="collapsed")
        B.append([b_val])

st.divider()

# Calculate Button
if st.button("Calculate", type="primary", use_container_width=True):
    det_A = determinant(A)
    
    st.markdown(f"### **$\det(A) = {det_A:.2f}$**")
    
    if det_A == 0:
        st.error("Cramer's Rule cannot be applied because det(A) = 0.")
    else:
        det_X = determinant(var_matrix(A, B, 1))
        x_ans = det_X / det_A
        st.write(f"$\det(x) = {det_X:.2f}$, &nbsp;&nbsp; **$x = {x_ans:.2f}$**")

        det_Y = determinant(var_matrix(A, B, 2))
        y_ans = det_Y / det_A
        st.write(f"$\det(y) = {det_Y:.2f}$, &nbsp;&nbsp; **$y = {y_ans:.2f}$**")

        if size == 3:
            det_Z = determinant(var_matrix(A, B, 3))
            z_ans = det_Z / det_A
            st.write(f"$\det(z) = {det_Z:.2f}$, &nbsp;&nbsp; **$z = {z_ans:.2f}$**")