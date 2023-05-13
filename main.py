from typing import List

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from proposals import Proposal, get_proposal_info, fill_proposal_stats, get_all_proposals

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


@app.get("/api/proposals/{proposal_id}", response_model=Proposal)
async def get_proposal(proposal_id: int):
    proposal = get_proposal_info(proposal_id)
    fill_proposal_stats(proposal)
    return proposal


@app.get("/api/proposals", response_model=List[Proposal])
async def get_proposals():
    return get_all_proposals()
