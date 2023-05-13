from pydantic import BaseModel
from typing import List, Optional


class Event(BaseModel):
    type: str
    sender: str
    receiver: str
    timestamp: int
    sequence: int
    version: int
    amount: int = 0


class VoteOption(BaseModel):
    address: str
    option: str
    count: int = 0
    weight: int = 0

    def reset_stats(self):
        self.weight = 0
        self.count = 0


class Txn(BaseModel):
    timestamp: int
    hash: str
    block: int
    sender: str
    recipient: str
    amount: float


class Vote(BaseModel):
    option: VoteOption
    event: Event
    weight: int = 0


class VotesSummary(BaseModel):
    total_votes: int
    total_weight: int


class Proposal(BaseModel):
    id: int
    title: str
    subtitle: str
    address: str
    description: str
    options: List[VoteOption]
    votes: Optional[List[Vote]]
    votes_summary: Optional[VotesSummary]
