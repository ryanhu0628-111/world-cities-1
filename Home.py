"""Home.py — Streamlit multipage app entry (home page)

This file is intended to live at the repository root and serve as the main
entry point for a Streamlit multipage app. The actual app page is located
in pages/app.py (which you've already added). This Home page shows a title,
welcome text, and a button that navigates to the app page.
"""

import streamlit as st

st.set_page_config(page_title="World Cities — Home", page_icon="🏠")

st.title("World Cities")
st.header("Welcome")
st.write(
    "Welcome to the World Cities app. Use this home page to get oriented before opening the main app page.")

st.write("Click the button below to open the main app (pages/app.py).")

# A simple HTML link styled as a button that navigates to the app page.
# Many Streamlit deployments accept a `?page=...` query parameter to switch pages.
# If your page has a different name in the UI, adjust the `app_href` accordingly.
app_href = "/?page=app"

st.markdown(
    f'<a href="{app_href}"><button style="padding:8px 16px; font-size:16px;">Open App</button></a>',
    unsafe_allow_html=True,
)

st.write(
    "If the button doesn't navigate in your environment, open the sidebar and choose the 'app' page, or visit `/?page=app` directly in the browser.")
