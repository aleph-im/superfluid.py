from typing import Optional

from web3 import Web3
from web3.exceptions import ContractCustomError

from constants import HOST_ABI
from operation import Operation


class Host:

    contract = None

    def __init__(self, rpc: str, host_address: str) -> None:
        web3 = Web3(Web3.HTTPProvider(rpc))
        self.contract = web3.eth.contract(
            address=host_address, abi=HOST_ABI)

    def call_agreement(self, agreement_address: str, calldata: str, user_data: Optional[str]) -> Operation:
        try:
            tx = self.contract.functions.callAgreement(
                agreement_address, calldata, user_data).build_transaction()
            print(tx)
        except ContractCustomError as e:
            print(e)

    def call_app_action() -> Operation:
        pass
