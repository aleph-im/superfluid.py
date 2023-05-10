from utils import normalize_address


class GetFlowParams:
    super_token = None
    sender = None
    receiver = None

    def __init__(self, super_token: str, sender: str, receiver: str) -> None:
        """
            * @param super_token the superToken of the agreement
            * @param sender the sender of the flow
            * @param receiver the receiver of the flow
        """
        self.super_token = normalize_address(super_token)
        self.sender = normalize_address(sender)
        self.receiver = normalize_address(receiver)
