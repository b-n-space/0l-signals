from typing import List

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from proposals import Proposal, get_proposal_info

app = FastAPI()

# Mount the static files middleware to serve files from the /web directory
app.mount("/web", StaticFiles(directory="web"), name="web")


@app.get("/")
async def proposals():
    return FileResponse("web/index.html")


@app.get("/proposal/{proposal_id}")
async def proposal(proposal_id: int):
    # Todo (Nour): Pass id to the page so it fetches the correct proposal
    return FileResponse("web/proposal.html")


# Todo (Nour): Cache response
@app.get("/api/proposals/{proposal_id}", response_model=Proposal)
async def get_proposal(proposal_id: int):
    return get_proposal_info(proposal_id)


# Todo (Nour): Cache response
@app.get("/api/proposals", response_model=List[Proposal])
async def get_proposals():
    # Todo (Nour): Fetch proposals from a fixed location; repo, config file, etc
    proposals = [get_proposal_info(1), get_proposal_info(2)]
    return proposals
