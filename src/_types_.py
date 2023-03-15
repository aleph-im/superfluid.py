class GetFlowParams:
    super_token = None
    sender = None
    receiver = None

    def __init__(self, super_token: str, sender: str, receiver: str) -> None:
        self.super_token = super_token
        self.sender = sender
        self.receiver = receiver