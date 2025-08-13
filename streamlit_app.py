import streamlit as st
from src.embedding import generate_embeddings
from src.database import find_most_similar


st.title("Buscador de papers por similitud de abstract")
st.write("Introduzca un abstract para encontrar los 10 papers más similares en arXiv usando pgvector.")


examples = {
    "Ejemplo 1": """A fully differential calculation in perturbative quantum chromodynamics is
presented for the production of massive photon pairs at hadron colliders. All
next-to-leading order perturbative contributions from quark-antiquark,
gluon-(anti)quark, and gluon-gluon subprocesses are included, as well as
all-orders resummation of initial-state gluon radiation valid at
next-to-next-to-leading logarithmic accuracy. The region of phase space is
specified in which the calculation is most reliable. Good agreement is
demonstrated with data from the Fermilab Tevatron, and predictions are made for
more detailed tests with CDF and DO data. Predictions are shown for
distributions of diphoton pairs produced at the energy of the Large Hadron
Collider (LHC). Distributions of the diphoton pairs from the decay of a Higgs
boson are contrasted with those produced from QCD processes at the LHC, showing
that enhanced sensitivity to the signal can be obtained with judicious
selection of events."""

}

selected_example = st.selectbox("Seleccione un ejemplo:", options=["Ninguno"] + list(examples.keys()))

if selected_example != "Ninguno":
    st.session_state.abstract_input = examples[selected_example]

# Campo de entrada, vinculado al estado de la sesión
abstract_input = st.text_area("Abstract", height=200, placeholder="Introduzca su abstract aquí:", key="abstract_input")

# Botón de búsqueda
if st.button("Buscar"):
    if abstract_input:
        results = find_most_similar(abstract_input, generate_embeddings)
        st.text_area("Papers similares", value=results, height=400)
    else:
        st.write("Por favor, introduzca un abstract.")