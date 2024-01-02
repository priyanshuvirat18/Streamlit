import streamlit as st

st.title("WIDGETS")

if st.button("Subscribe"):
    st.write("Like the video")

name=st.text_input("Name")
st.write(name)

address=st.text_area("Enter address")
st.write(address)

st.date_input("Enter a data")

st.time_input("Enter time")

if st.checkbox("You accept the T&C", value=False):
    st.write("Thank you for accepting!")

v1=st.radio("Colour",["r","g","b"],index=0)
v2=st.selectbox("Colour",["r","g","b"],index=0)

st.write(v1)
st.write(v2)

v3=st.multiselect("Colour",["r","g","b"])
st.write(v3)

v4=st.slider("age",min_value=0,max_value=456,value=18,step=2)
st.write(v4)

st.number_input("age",min_value=0.0,max_value=456.0,value=18.0,step=2.0)

img = st.file_uploader("Upload file")
st.image(img)