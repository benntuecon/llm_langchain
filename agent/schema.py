from pydantic import BaseModel


class JobDescriptionInput(BaseModel):
    positions: str
    tech_stacks: list[str]
    summary_for_tech_stack: str
    soft_skill: list[str]
    other_properties: list[str]


class RepoSummary(BaseModel):
    ...
