from pydantic import BaseModel, Field

class Prompt(BaseModel):
    id: str = Field(..., description="Unique identifier for the prompt")
    name: str = Field(..., description="The name of the prompt")
    description: str = Field(..., description="A detailed description of what the prompt does")
    role: str = Field(..., description="The role or context in which this prompt is used")
    prompt_string: str = Field(..., description="The actual prompt text/template") 