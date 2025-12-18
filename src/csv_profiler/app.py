import json
import streamlit as st
import csv
from io import StringIO
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown
from pathlib import Path

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Upload a CSV profile it export JSON + Markdown")
st.sidebar.header("Inputs")
source = st.sidebar.selectbox("Data source", ["Upload"])
st.write("Selected:", source)   

uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.checkbox("Show preview", value=True)

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

if st.button("Generate report"):
    st.session_state["report"] = profile_rows(rows)

report = st.session_state.get("report")
if report is not None:
    st.write("Rows:",report["n_rows"])
    st.write("Cols:",report["n_cols"])


    st.write("File name: ",uploaded.name)
    
    if show_preview:
        st.write(rows[:5])

    st.subheader("Markdown preview")
    st.markdown(render_markdown(report))
    
    json_text = json.dumps(report, indent=2, ensure_ascii=False)
    md_text = render_markdown(report)
    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report.json").write_text(json_text, encoding="utf-8")
    (out_dir / "report.md").write_text(md_text, encoding="utf-8")

    l, r = st.columns(2)
    st.download_button("Get JSON", data=json_text, file_name="report.json")
    st.download_button("Get Markdown", data=md_text, file_name="report.md")

else:
    st.info("Upload a CSV to begin.")



# rows = list(csv.DictReader(StringIO(text)))