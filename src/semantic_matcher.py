from sentence_transformers import SentenceTransformer
from sentence_transformers import util


# Load model once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def similarity_score(
    text1,
    text2
):
    """
    Calculate semantic similarity
    between two texts.
    """

    embedding1 = model.encode(
        text1,
        convert_to_tensor=True
    )

    embedding2 = model.encode(
        text2,
        convert_to_tensor=True
    )

    score = util.cos_sim(
        embedding1,
        embedding2
    )

    return float(score)