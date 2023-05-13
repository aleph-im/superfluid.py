from typing import Optional

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
            * @param super_token the super token of the agreement
            * @param sender the sender of the flow
            * @param flow_operator the flow operator
        """
        self.super_token = normalize_address(super_token)
        self.flow_operator_id = to_bytes32(flow_operator_id)


class ShouldUseCallAgreement:

    should_use_call_agreement = False

    def __init__(self, should_use_call_agreement: bool) -> None:
        """
            * @param should_use_call_agreement whether or not to use the host contract
        """
        self.should_use_call_agreement = should_use_call_agreement


class ModifyFlowParams(ShouldUseCallAgreement):

    flow_rate = None
    receiver = None
    sender = None
    user_data = None
    super_token = None

    def __init__(self, should_use_call_agreement: bool, receiver: str, super_token: str, flow_rate: Optional[int] = 0, sender: Optional[str] = "", user_data: Optional[str] = "") -> None:
        """
            * @param receiver receiver of a flow
            * @param super_token the super token of the agreement
            * @param flow_rate(Optional) flow rate for the flow
            * @param sender(Optional) sender of the flow
            * @param user_data(Optional) user data for the flow
        """
        super().__init__(should_use_call_agreement)
        self.receiver = normalize_address(receiver)
        self.super_token = normalize_address(super_token)
        self.flow_rate = flow_rate
        self.sender = normalize_address(sender)
        self.user_data = user_data


class CreateFlowParams(ModifyFlowParams):

    flow_rate = None

    def __init__(self, should_use_call_agreement: bool, receiver: str, super_token: str, flow_rate: int, sender: Optional[str] = "", user_data: Optional[str] = "") -> None:
        """
            * @param flow_rate flow rate for the flow
        """
        super().__init__(should_use_call_agreement, receiver,
                         super_token, flow_rate, sender, user_data)
        self.flow_rate = flow_rate
