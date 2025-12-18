import streamlit as st
import csv
from io import StringIO
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Upload a CSV profile it export JSON + Markdown")
st.sidebar.header("Inputs")
source = st.sidebar.selectbox("Data source", ["Upload"])
st.write("Selected:", source)   

uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.checkbox("Show preview", value=True)

if uploaded is not None:
    text = uploaded.getvalue().decode('utf-8-sig')
    rows = list(csv.DictReader(StringIO(text)))

    if st.button('Generate report'):
        st.session_state['report'] =  profile_rows(rows)
report = st.session_state.get("report")
if report is not None:
    st.write("Rows:", report["n_rows"])
    st.write("Cols:", report["n_cols"])

    st.write("File name: ",uploaded.name)
    
    if show_preview:
        st.write(rows[:5])

    st.subheader("Markdown preview")
    st.markdown(render_markdown(report))
    

else:
    st.info("Upload a CSV to begin.")


st.download_button("Get JSON", data=json_text, file_name="report.json")
st.download_button("Get Markdown", data=md_text, file_name="report.md")

# cols = st.columns(2)
# cols[0].metric("Rows", len(rows))
# cols[1].metric("Columns", len(rows[0].keys()))