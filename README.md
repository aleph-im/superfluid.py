<h1 align="center">Welcome to Superfluid Python SDK(Unofficial) 👋
</h1>
<div align="center">
<img  width="300" padding="0 0 10px" alt="Superfluid logo" src="https://github.com/superfluid-finance/protocol-monorepo/raw/dev/sf-logo.png" />
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/Superfluid_HQ/" target="blank">
    <img alt="Twitter: Superfluid_HQ" src="https://img.shields.io/twitter/follow/Superfluid_HQ.svg?style=social" />
  </a>
</p>
</div>

### 🏠 [Homepage](https://superfluid.finance)

### ✨ [Superfluid App](https://app.superfluid.finance/)

### 📖 [Docs](https://docs.superfluid.finance)

</br>

# Introduction

superfluid.py is an application framework for interacting with the Superfluid Protocol without the Python Programming Language.

# Features

* Minimal Framework initialization (`rpc` and `chain id`)
* New Operation syntax for transactions
* Create/Update/Delete Agreement Operations (Constant Flow Agreement and Instant Distribution Agreement(In development))

# Notable Used Technologies

* Python
* Web3.py

# Installation

```bash
pip install superfluid
```

# Usage

```python
from superfluid import CFA_V1

rpc: str = "YOUR PREFERRED RPC"
chain_id: int = "CHAIN ID"

///////////////////////////////////////////////////////
//////// CONSTANT FLOW AGREEMENT OPERATIONS ///////////
///////////////////////////////////////////////////////

cfaV1Instance = CFA_V1(rpc, chain_id)

super_token: str = "SUPER TOKEN ADDRESS"
sender: str = "SENDER ADDRESS"
receiver: str = "RECEIVER ADDRESS"
flow_rate: int = "FLOW RATE"

PRIVATE_KEY: str = "YOUR PRIVATE KEY"
OPERATOR_PRIVATE_KEY: str = "OPERATOR PRIVATE KEY"

create_flow_operation = cfaV1Instance.create_flow(
    sender, receiver, super_token, flow_rate)
transaction_hash = create_flow_operation.exec(PRIVATE_KEY)

update_flow_operation = cfaV1Instance.update_flow(
    sender, receiver, super_token, flow_rate)
transaction_hash = update_flow_operation.exec(PRIVATE_KEY)

delete_flow_operation = cfaV1Instance.delete_flow(
    sender, receiver, super_token)
transaction_hash = delete_flow_operation.exec(PRIVATE_KEY)

flow_operator: str = "OPERATOR ADDRESS"
flow_rate_allowance_delta: int = "FLOW RATE ALLOWANCE DELTA"

flow_rate_allowance_operation = cfaV1Instance.increase_flow_rate_allowance(
    super_token, flow_operator, flow_rate_allowance_delta)
transaction_hash = flow_rate_allowance_operation.exec(PRIVATE_KEY)

flow_rate_allowance_operation = cfaV1Instance.decrease_flow_rate_allowance(
    super_token, flow_operator, flow_rate_allowance_delta)
transaction_hash = flow_rate_allowance_operation.exec(PRIVATE_KEY)

permission: int = "VALID PERMISSION"

update_flow_operator_permissions_operation = cfaV1Instance.update_flow_operator_permissions(
    super_token, flow_operator, permission, flow_rate_allowance_delta)
transaction_hash = update_flow_operator_permissions_operation.exec(PRIVATE_KEY)

authorize_flow_operator_with_full_control_operation = cfaV1Instance.authorize_flow_operator_with_full_control(
    super_token, flow_operator)
transaction_hash = authorize_flow_operator_with_full_control_operation.exec(
    PRIVATE_KEY)

revoke_flow_operator_with_full_control_operation = cfaV1Instance.revoke_flow_operator_with_full_control(
    super_token, flow_operator)
transaction_hash = revoke_flow_operator_with_full_control_operation.exec(
    PRIVATE_KEY)

create_flow_operator_operation = cfaV1Instance.create_flow_by_operator(
    sender, receiver, super_token, flow_rate)
transaction_hash = create_flow_operator_operation.exec(OPERATOR_PRIVATE_KEY)

update_flow_operator_operation = cfaV1Instance.update_flow_by_operator(
    sender, receiver, super_token, flow_rate)
transaction_hash = update_flow_operator_operation.exec(OPERATOR_PRIVATE_KEY)

delete_flow_operator_operation = cfaV1Instance.delete_flow_by_operator(
    sender, receiver, super_token)
transaction_hash = delete_flow_operator_operation.exec(OPERATOR_PRIVATE_KEY)
```
