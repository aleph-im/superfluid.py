from typing import Dict

from web3 import Web3

from host import Host
from constants import CFA_V1_ABI, CFA_V1_FORWARDER_ABI, RPC_FOR_MUMBAI, CFA_V1_ADDRESS, CFA_V1_FORWARDER_ADDRESS, HOST_ADDRESS
from _types_ import GetFlowParams
from errors import SFError


class CFA_V1:
    web3 = None
    host = None
    contract = None
    forwarder = None

    def __init__(self, rpc: str, host_address: str, cfa_v1_address: str, cfa_v1_forwarder: str) -> None:
        web3 = Web3(Web3.HTTPProvider(rpc))
        self.host = Host(host_address)
        self.contract = web3.eth.contract(
            address=cfa_v1_address, abi=CFA_V1_ABI)
        self.forwarder = web3.eth.contract(
            address=cfa_v1_forwarder, abi=CFA_V1_FORWARDER_ABI)

    def get_flow(self, params: GetFlowParams) -> Dict[str, int]:
        """
            Get the details of a flow.
            @param params the holds the super token, sender, and receiver
            @returns  Dict[str, int] Web3 Flow info object
        """
        try:
            transaction_response = self.contract.functions.getFlow(
                params.super_token, params.sender, params.receiver).call()
            flow_data = {
                "timestamp": transaction_response[0],
                "flowRate": transaction_response[1],
                "deposit": transaction_response[2],
                "owedDeposit": transaction_response[3]
            }
            return flow_data
        except Exception as e:
            raise SFError(e)


# cfaV1Instance = CFA_V1(RPC_FOR_MUMBAI, HOST_ADDRESS, CFA_V1_ADDRESS,
#                        CFA_V1_FORWARDER_ADDRESS)
# super_token = "0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f"
# sender = "0x74CDF863b00789c29734F8dFd9F83423Bc55E4cE"
# receiver = "0x322E25a131102Ee4B520277c4b007Ad3F22d2F7a"

# get_flow_params = GetFlowParams(super_token, sender, receiver)
# response = cfaV1Instance.get_flow(get_flow_params)
# print(response.get("flowRate"))
