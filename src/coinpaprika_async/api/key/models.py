from dataclasses import dataclass


@dataclass
class CurrentMonthUsage:
    requests_made: int
    requests_left: int


@dataclass
class APIUsage:
    message: str
    current_month: CurrentMonthUsage


@dataclass
class KeyInfo:
    plan: str
    plan_started_at: str
    plan_status: str
    portal_url: str
    usage: APIUsage
