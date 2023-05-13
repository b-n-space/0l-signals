import json
from datetime import datetime
from functools import cache

import requests

from models import *

# TODO (Nour): Hardcoded in-memory db
# Todo (Nour): Fetch proposal text using its id. Assuming we used a git repository, the id would be the filename.
# Todo (Nour): Fetch proposals from a fixed location; repo, config file, etc
with open("proposals.json") as f:
    PROPOSALS = json.load(f)
    PROPOSALS = {p["id"]: Proposal(**p) for p in PROPOSALS}

EVENTS: {str: Event} = {}


def get_all_proposals():
    return list(PROPOSALS.values())


def get_proposal_info(proposal_id):
    proposal = PROPOSALS[proposal_id]
    return proposal


FIRST_EPOCH = datetime(2021, 11, 15)


@cache
def get_current_epoch():
    res = requests.get("https://0lexplorer.io/api/webmonitor/vitals")
    return res.json()["chain_view"]["epoch"]


def _get_epoch(timestamp: int):
    return (datetime.fromtimestamp(timestamp) - FIRST_EPOCH).days


def fill_proposal_stats(proposal: Proposal):
    """
    Sets votes and votes_summary of the given proposal.
    Since proposal is loaded from memory, these values show on main screen without needing to recalculate them
    only when visiting proposal page we call fill_proposal_stats
    """
    current_epoch = get_current_epoch()

    # find all txns (events) sent to option addresses
    options_map: {str: VoteOption} = {}
    events: [Event] = []
    for option in proposal.options:
        # Not sure whether we need to load more than 1k events
        # skip first event sent to option address
        events.extend(get_events(option.address, limit=1000, load_from_cache=False)[1:])
        option.reset_stats()  # Reset option stats as it is loaded from memory
        options_map[option.address.upper()] = option

    # collect distinct list of voters
    votes: {str: Vote} = {}
    for event in events:
        votes.setdefault(event.sender, Vote(event=event, option=options_map[event.receiver]))

    # For each voter, find their first event and its epoch to calculate their vote weight
    for voter, vote in votes.items():
        # vote weight = current epoch - first txn epoch, clamped at current_epoch // 2
        first_event = get_first_event(voter)
        if not first_event:
            # Exclude the vote
            votes[voter] = None
            print("no first event, removing vote", proposal.id, vote)
            continue
        weight = current_epoch - _get_epoch(first_event.timestamp)
        weight = max(min(weight, current_epoch // 2), 0)
        vote.weight = weight
        # the number of voters would be the option's `count`
        options_map[vote.option.address].count += 1
        # the sum of weights would be the option's `weight`
        options_map[vote.option.address].weight += weight

    # Remove excluded votes
    votes = {k: v for k, v in votes.items() if v}

    proposal.votes = list(votes.values())
    proposal.votes_summary = VotesSummary(
        total_votes=len(votes),
        total_weight=sum([o.weight for o in proposal.options]),
    )


@cache
def get_first_event(address: str) -> Event:
    """
    Find first proper event; mining reward
    """
    events = get_events(address)
    for e in events:
        if e.sender == "00000000000000000000000000000000" and e.type == "receivedpayment":
            return e


def get_events(address: str, limit=10, load_from_cache=True) -> List[Event]:
    """
    Retrieve events of given address and cache the result
    """
    if load_from_cache:
        events = EVENTS.get(address)
        if events:
            return events
    res = requests.get(f"https://0l.interblockcha.in/api/proxy/node/events?address={address}&start=0&limit={limit}")
    events = [
        Event(
            timestamp=e["timestamp_usecs"] // 1000_000,
            sequence=e["sequence_number"],
            version=e["transaction_version"],
            type=e["data"]["type"],
            sender=e["data"]["sender"].upper(),
            receiver=e["data"]["receiver"].upper(),
            amount=e["data"]["amount"]["amount"] / 1000_000,
        ) for e in res.json()["result"]
    ]
    EVENTS[address] = events
    return events
