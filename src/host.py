from typing import Optional, Type

from web3 import Web3
from web3.types import TxParams
from web3.middleware import geth_poa_middleware

from constants import HOST_ABI
from operation import Operation
from __types__ import BatchOperationType


class Host:

    contract = None

    def __init__(self, rpc: str, host_address: str) -> None:
        web3 = Web3(Web3.HTTPProvider(rpc))
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = web3.eth.contract(
            address=host_address, abi=HOST_ABI)

    def call_agreement(self, agreement_address: str, calldata: str, user_data: str) -> Operation:
        try:
            tx: TxParams = self.contract.functions.callAgreement(
                agreement_address, calldata, user_data).build_transaction({
                    "from": "0xE895C0Cfb0f3CcE6844E9082989AC2Aa2ba8B253"
                })
            return Operation(tx, BatchOperationType.SUPERFLUID_CALL_AGREEMENT)
        except Exception as e:
            raise e

    def call_app_action() -> Operation:
        pass
