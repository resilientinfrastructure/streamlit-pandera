import streamlit as st

from streamlit_pandera.validate_file import run_validate_file


st.set_page_config(
    page_title="Data Validator Home",
    page_icon="📊",
)
st.write("# Data Validation Tool! 📊")
standards = {
    "store_schema": ("https://raw.githubusercontent.com/resilientinfrastructure/standards/main/panderas_schema.yml")
}
run_validate_file(standards=standards)
