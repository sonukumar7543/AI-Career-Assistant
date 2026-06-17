from src.semantic_matcher import similarity_score

print(
    similarity_score(
        "Machine Learning",
        "ML"
    )
)

print(
    similarity_score(
        "Python",
        "Java"
    )
)

print(
    similarity_score(
        "Deep Learning",
        "Neural Networks"
    )
)