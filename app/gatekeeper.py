from pydantic import BaseModel, Field


class Job(BaseModel):
    job_id: str
    technician_notes: str
    invoice_items: list[str] = Field(default_factory=list)


TERMS = {
    "capacitor": ("capacitor", "cap replacement"),
    "refrigerant": ("refrigerant", "r-410a", "r410a", "r-454b"),
    "contactor": ("contactor",),
}


def review_job(job: Job) -> dict:
    notes = job.technician_notes.lower()
    billed = " ".join(job.invoice_items).lower()

    possible_omissions = []

    for item, keywords in TERMS.items():
        mentioned = any(word in notes for word in keywords)
        invoiced = any(word in billed for word in keywords)

        if mentioned and not invoiced:
            possible_omissions.append(item)

    return {
        "job_id": job.job_id,
        "status": "review_needed" if possible_omissions else "no_rule_flags",
        "possible_omissions": possible_omissions,
        "requires_human_approval": True,
    }
