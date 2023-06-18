from dataclasses import dataclass


@dataclass(repr=True)
class CurrentMonthUsage:
    requests_made: int
    requests_left: int


@dataclass(repr=True)
class APIUsage:
    message: str
    current_month: CurrentMonthUsage


@dataclass(repr=True)
class KeyInfo:
    plan: str
    plan_started_at: str
    plan_status: str
    portal_url: str
    usage: APIUsage
