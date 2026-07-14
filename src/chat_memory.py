conversation_history = []


def initialize_resume_context(context):

    global conversation_history

    conversation_history = []

    context_message = f"""
The following information belongs to the current user.

Name:
{context.get("name","")}

Email:
{context.get("email","")}

Skills:
{", ".join(context.get("skills", []))}

Education:
{context.get("education", [])}

Projects:
{context.get("projects", [])}

Experience:
{context.get("experience", [])}

Resume Score:
{context.get("resume_score","")}

Skill Score:
{context.get("skill_score","")}

Semantic Score:
{context.get("semantic_score","")}

Matched Skills:
{", ".join(context.get("matched_skills", []))}

Missing Skills:
{", ".join(context.get("missing_skills", []))}

Predicted Career:
{context.get("predicted_career","")}

Recommended Jobs:
{context.get("recommended_jobs", [])}

Remember this information.
Use it whenever the user asks questions
about their resume.
"""

    conversation_history.append(
        {
            "role":"system",
            "content":context_message
        }
    )


def add_message(role, content):

    conversation_history.append(
        {
            "role":role,
            "content":content
        }
    )


def get_history():

    return conversation_history


def clear_history():

    conversation_history.clear()