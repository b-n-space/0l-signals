from typing import List

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()


class ChartData(BaseModel):
    labels: List[str]
    data: List[float]


class VoteOption(BaseModel):
    option: str
    count: int
    weight: int


class VotesSummary(BaseModel):
    total_votes: int
    total_weight: int
    options: List[VoteOption]


class Proposal(BaseModel):
    proposal_id: int
    title: str
    description: str
    votes: ChartData
    votes_summary: VotesSummary


@app.get("/")
async def serve_root():
    return FileResponse("web/index.html")


@app.get("/proposal/{proposal_id}")
async def proposal(proposal_id: int):
    return FileResponse("web/proposal.html")


@app.get("/proposals/{proposal_id}", response_model=Proposal)
async def get_proposal(proposal_id: int):
    # In a real-world scenario, you would fetch the proposal data from a database
    # based on the proposal_id.
    return get_proposal_from_rpc(proposal_id)


@app.get("/proposals", response_model=List[Proposal])
async def get_proposals():
    # In a real-world scenario, you would fetch the list of proposals from a database.
    proposals = [get_proposal_from_rpc(1), get_proposal_from_rpc(2)]
    return proposals


# Mount the static files middleware to serve files from the /web directory
app.mount("/web", StaticFiles(directory="web"), name="web")

def get_proposal_from_rpc(proposal_id):
    return Proposal(
        proposal_id=proposal_id,
        title="Example Proposal",
        description="This is an example proposal.",
        votes=ChartData(
            labels=["Wallet 1", "Wallet 2", "Wallet 3", "Wallet 4", "Wallet 5", "Wallet 6"],
            data=[250, 250, 250, 250, 100, 1],
        ),
        votes_summary=VotesSummary(
            total_votes=6,
            total_weight=1101,
            options=[
                VoteOption(option="Yes", count=4, weight=601),
                VoteOption(option="No", count=2, weight=500),
            ],
        ),
    )
