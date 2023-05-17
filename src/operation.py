from typing import Optional

from web3.types import TxParams

from __types__ import BatchOperationType


class Operation:

    txn: TxParams = None
    type: BatchOperationType = None
    forwarder_txn: TxParams = None

    def __init__(self, txn: TxParams, type: BatchOperationType, forwarder_txn: Optional[TxParams] = None) -> None:
        self.txn = txn
        self.type = type
        self.forwarder_txn = forwarder_txn

    def exec() -> None:
        pass
