import streamlit as st

from constants import OCTAVE

st.title("Animagus 🐺")
st.header("Easily shift the music notes by the offset that you need!")

opt = st.selectbox(
    label="Please select your octave style from the following",
    options=list(OCTAVE.keys()),
)

expander = st.expander(label="Individual Notes")

if "options" not in st.session_state:
    st.session_state["options"] = ""


def clear_button_callback():
    st.session_state["options"] = ""


def button_callback(note):
    st.session_state["options"] = st.session_state["options"] + " " + note


placeholder = st.empty()

if st.button(label="Clear", key="clear", type="primary"):
    clear_button_callback()

for k, v in OCTAVE.items():
    if opt == k:
        with expander:
            expander.write(" ".join(v))

        # input = st.text_input(label="Please enter the space-separated notes here (use . for blank)")
        cols = st.columns([1, 1, 1])

        for idx, col in enumerate(cols):
            with col:
                for note in v[idx::3]:
                    if st.button(label=note, key=note):
                        button_callback(note)

        offset = st.number_input(
            label="Required offset in notes", min_value=1, max_value=13
        )

        notes = st.session_state["options"].split()

        if len(notes) != 0:
            for note in notes:
                if note == ".":
                    continue
                if note not in v:
                    st.error("Invalid notation entered.")
                    st.stop()

            v_len = len(v)

            for i in range(len(notes)):
                if notes[i] == ".":
                    continue
                notes[i] = v[(v.index(notes[i]) + offset) % v_len]

            output = " ".join(notes)
            st.success(f"Output notes are {output}")

            st.download_button(label="Download the output notes", data=output, file_name="output_notes.txt")

with placeholder:
    text = st.text_area(label="", max_chars=1000, key="options")
