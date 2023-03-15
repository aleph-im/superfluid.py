from web3 import Web3

from host import Host
from constants import CFA_V1_ABI, CFA_V1_FORWARDER_ABI, RPC_FOR_MUMBAI
from _types_ import GetFlowParams

class CFA_V1:
    web3 = None
    host = None
    contract = None
    forwarder = None

    def __init__(self, rpc: str, host_address: str, cfa_v1_address: str, cfa_v1_forwarder: str) -> None:
        pass
        web3 = Web3(Web3.HTTPProvider(rpc))
        self.host = Host(host_address)
        self.contract = web3.eth.contract(address=cfa_v1_address, abi=CFA_V1_ABI)
        self.forwarder = web3.eth.contract(address=cfa_v1_forwarder, abi=CFA_V1_FORWARDER_ABI)

    def get_flow(self, params: GetFlowParams):
        pass


        