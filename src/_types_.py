from web3 import Web3

from utils import normalize_address, to_bytes32


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


class GetAccountFlowInfoParams:
    super_token = None
    account = None

    def __init__(self, super_token: str, account: str) -> None:
        """
            * @param super_token the superToken of the agreement
            * @param account the account to get its info
        """
        self.super_token = normalize_address(super_token)
        self.account = normalize_address(account)


class GetFlowOperatorDataParams:
    super_token = None
    sender = None
    flow_operator = None

    def __init__(self, super_token: str, sender: str, flow_operator: str) -> None:
        """
            * @param super_token the superToken of the agreement
            * @param sender the sender of the flow
            * @param flow_operator the flow operator
        """
        self.super_token = normalize_address(super_token)
        self.sender = normalize_address(sender)
        self.flow_operator = normalize_address(flow_operator)


class GetFlowOperatorDataParamsByID:
    super_token = None
    flow_operator_id = None

    def __init__(self, super_token: str, flow_operator_id: str) -> None:
        """
            * @param super_token the superToken of the agreement
            * @param sender the sender of the flow
            * @param flow_operator the flow operator
        """
        self.super_token = normalize_address(super_token)
        self.flow_operator_id = to_bytes32(flow_operator_id)
        print(self.flow_operator_id)
