from typing import List, Optional

from pydantic import BaseModel


class Votes(BaseModel):
    labels: List[str]
    data: List[float]


class VoteOption(BaseModel):
    address: str
    option: str
    count: int
    weight: int


class VotesSummary(BaseModel):
    total_votes: int
    total_weight: int
    options: List[VoteOption]


class Proposal(BaseModel):
    id: int
    title: str
    address: str
    description: str
    votes: Optional[Votes]
    votes_summary: Optional[VotesSummary]


def get_proposal_info(proposal_id):
    # Todo (Nour): Fetch proposal text using its id. Assuming we used a git repository, the id would be the filename.
    proposal = Proposal(
        id=proposal_id,
        title="Example Proposal",
        address="123abc456efg",
        description="This is an example proposal.",
        options=[VoteOption]
    )
    fill_proposal_stats(proposal)
    return proposal


def fill_proposal_stats(proposal):
    # Todo (Nour): Fetch proposal stats from RPC or explorer

    # Todo (Nour): Do we need this? how to use it on the chart? skip for now
    proposal.votes = Votes(
        labels=["Wallet 1", "Wallet 2", "Wallet 3", "Wallet 4", "Wallet 5", "Wallet 6"],
        data=[250, 250, 250, 250, 100, 1],
    )

    # Todo (Nour): calculations, for each option
    # - using options address, find all txns sent to it
    # - collect distinct list of voters, the number of voters would be the option's `count`
    # - For each voter, find their first txn and its epoch
    # - vote weight = current epoch - first txn epoch
    # - the some of weights would be the option's `weight`

    # Todo (Nour): Utilise cache; wallets can be keys and the epoch of their first txn would be the values
    # This way we can calculate the weight quickly
    proposal.votes_summary = VotesSummary(
        total_votes=6,
        total_weight=1101,
        options=[
            VoteOption(option="Yes", count=4, weight=601, address="111111"),
            VoteOption(option="No", count=2, weight=500, address="222222"),
        ],
    )
