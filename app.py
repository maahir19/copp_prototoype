import streamlit as st

st.set_page_config(page_title="Copp", page_icon="👟", layout="wide")

# Font styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.title{
font-size:60px;
font-weight:600;
text-align:center;
}

.subtitle{
text-align:center;
color:gray;
margin-bottom:40px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">Copp</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Premium Sneaker Collection</p>', unsafe_allow_html=True)

# Shoe Data
shoes = [
    {
        "name":"Nike Air Runner",
        "price":2999,
        "image":"https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    },
    {
        "name":"Adidas Ultra Boost",
        "price":4999,
        "image":"https://images.unsplash.com/photo-1600185365483-26d7a4cc7519"
    },
    {
        "name":"Puma Street Flex",
        "price":2499,
        "image":"https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77"
    },
    {
        "name":"Converse Classic",
        "price":1999,
        "image":"https://images.unsplash.com/photo-1519741497674-611481863552"
    }
]

st.write("## Featured Sneakers")

cols = st.columns(4)

cart_total = 0

for i, shoe in enumerate(shoes):

    with cols[i]:
        st.image(shoe["image"], use_container_width=True)
        st.write(f"### {shoe['name']}")
        st.write(f"₹ {shoe['price']}")

        qty = st.number_input(
            f"Quantity {i}",
            min_value=0,
            max_value=10,
            value=0,
            key=i
        )

        cart_total += qty * shoe["price"]

# Cart summary
st.write("---")
st.write("## 🛒 Cart Summary")

st.write(f"### Total Price: ₹ {cart_total}")

if cart_total > 0:
    st.success("Ready to checkout!")

# Sidebar
st.sidebar.title("About Copp")

st.sidebar.write("""
Copp is a modern sneaker brand prototype.

✔ Premium sneakers  
✔ Clean design  
✔ Fast shopping experience
""")

st.sidebar.write("📧 support@copp.com")