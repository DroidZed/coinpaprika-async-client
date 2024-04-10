from dataclasses import dataclass

@dataclass
class CurrentMonthUsage:
    requests_made: int
    requests_left: int
    def __init__(self, requests_made, requests_left) -> None: ...

@dataclass
class APIUsage:
    message: str
    current_month: CurrentMonthUsage
    def __init__(self, message, current_month) -> None: ...

@dataclass
class KeyInfo:
    plan: str
    plan_started_at: str
    plan_status: str
    portal_url: str
    usage: APIUsage
    def __init__(
        self, plan, plan_started_at, plan_status, portal_url, usage
    ) -> None: ...
