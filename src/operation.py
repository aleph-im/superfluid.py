from typing import Optional

from web3.types import TxParams
from web3 import Web3
from eth_typing import HexStr
from eth_account import Account

from __types__ import BatchOperationType


class Operation:

    txn: TxParams = None
    type: BatchOperationType = None
    forwarder_txn: TxParams = None

    def __init__(self, txn: TxParams, type: BatchOperationType, forwarder_txn: Optional[TxParams] = None) -> None:
        self.txn = txn
        self.type = type
        self.forwarder_txn = forwarder_txn

    def exec(self, rpc: str, private_key: str) -> HexStr:
        populated_transaction = self._get_populated_transaction_request(
            rpc, private_key)
        web3 = Web3(Web3.HTTPProvider(rpc))
        signed_txn = web3.eth.account.sign_transaction(
            populated_transaction, private_key=private_key)
        transaction_hash = web3.eth.send_raw_transaction(
            signed_txn.rawTransaction)
        return transaction_hash.hex()

    def _get_populated_transaction_request(self, rpc: str, private_key: str) -> TxParams:
        populated_transaction = self.forwarder_txn if self.forwarder_txn is not None else self.txn
        address = Account.from_key(private_key).address
        web3 = Web3(Web3.HTTPProvider(rpc))
        nonce = web3.eth.get_transaction_count(address)
        populated_transaction["nonce"] = nonce
        return populated_transaction
