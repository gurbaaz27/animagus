import streamlit as st

from constants import OCTAVE

st.title("Animagus 🐺")
st.header("Easily shift the music notes by the offset that you need!")

opt = st.selectbox(
    "Please select your octave style from the following",
    list(OCTAVE.keys()),
)

for k, v in OCTAVE.items():
    if opt == k:
        st.success(f"The individual notes are { ' '.join(v)}")

        input = st.text_input(label="Please enter the space-separated notes here (use . for blank)")

        offset = st.number_input(
            label="Offset in notes you want", min_value=1, max_value=13
        )

        if input != "":
            output: str

            notes = input.split()

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
