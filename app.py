import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Service Center Finder",
    page_icon="🔧",
    layout="wide"
)

df = pd.read_excel("service_center.xlsx")

st.title("🔧 Service Center Finder")

brand = st.text_input("Brand")

city = st.text_input("City (Optional)")

if st.button("Search"):

    result = df[
        df["Brand"].str.lower().str.contains(
            brand.lower(),
            na=False
        )
    ]

    if city != "":
        result = result[
            result["Address"]
            .str.lower()
            .str.contains(
                city.lower(),
                na=False
            )
        ]

    st.write(f"Found {len(result)} service center(s).")

    if len(result) == 0:
        st.warning("No service center found.")

    else:

        for _, row in result.iterrows():

            with st.container():

                st.subheader(row["Service Center Name"])

                st.write(f"**Brand:** {row['Brand']}")

                st.write(f"**Contact Person:** {row['Contact Person']}")

                st.write(f"**📍 Address:** {row['Address']}")

                st.write(f"**📞 Contact Number:** {row['Contact Number']}")

                st.write(f"**✉ Email:** {row['Email Address']}")

                st.divider()