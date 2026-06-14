"""
    Generate learning recommendations
    from missing skills.
"""
from src.learning_resources import LEARNING_RESOURCES


def recommend_skills(missing_skills):

    recommendations = {}

    for skill in missing_skills:

        if skill in LEARNING_RESOURCES:

            recommendations[skill] = (
                LEARNING_RESOURCES[skill]
            )

        else:

            recommendations[skill] = {
                "difficulty": "Unknown",
                "resource": "Search online resources"
            }

    return recommendations