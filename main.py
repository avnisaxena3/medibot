import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel
from tools import search_tool
from langchain_openai import ChatOpenAI

load_dotenv()

# ---------- Medical Response Format ----------
class MedicalResponse(BaseModel):
    condition: str
    probable_causes: list[str]
    recommended_drugs: list[str]
    precautions: list[str]
    when_to_visit_doctor: list[str]
    sources: list[str]
    disclaimer: str
    tools_used: list[str]


# ---------- LLM ----------
llm = ChatOpenAI(
    model_name=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0
)

# ---------- SYSTEM PROMPT ----------
SYSTEM_PROMPT = """
You are MedAssist — an AI medical chatbot.

Your output MUST be ONLY valid JSON in this exact format:

{
 "condition": "",
 "probable_causes": [],
 "recommended_drugs": [],
 "precautions": [],
 "when_to_visit_doctor": [],
 "sources": [],
 "disclaimer": "",
 "tools_used": []
}

RULES:
- Recommend ONLY OTC drugs (no antibiotics).
- Include a disclaimer always.
- Keep responses safe and simple.
- If using the search tool, list it in "tools_used".
"""

# ---------- MAIN FUNCTION ----------
def run_med_agent(query: str) -> dict:
    """
    Sends user symptom query to the model and returns structured JSON.
    """

    # --- Tool execution (simple logic for now) ---
    tool_output = search_tool.run(query)
    used_tools = ["search"] if "Search unavailable" not in tool_output else []

    # --- Ask the LLM to format everything into JSON ---
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"User Query: {query}\n\nTool Result: {tool_output}"
        }
    ]

    result = llm.invoke(messages)
    content = result.content

    # Try JSON decode
    try:
        data = json.loads(content)
        data["tools_used"] = used_tools
        return data
    except Exception:
        return {
            "error": "Model returned invalid JSON.",
            "raw_response": content
        }
