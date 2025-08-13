import gradio as gr

def create_gradio_interface(find_similar_func, embedding_func):
    iface = gr.Interface(
        fn=lambda text: find_similar_func(text, embedding_func),
        inputs=gr.Textbox(
            lines=8,
            placeholder="Introduzca su abstract aquí:",
            label="Abstract"
        ),
        outputs=gr.Textbox(
            lines=15,
            label="Papers similares"
        ),
        title="Buscador de papers por similitud de abstract",
        description="Introduzca un abstract para encontrar los 10 papers más similares en arXiv usando pgvector.",
        examples=[
            ["""                A fully differential calculation in perturbative quantum chromodynamics is
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
selection of events.
            """],
        ],
        theme=gr.themes.Soft()
    )
    return iface