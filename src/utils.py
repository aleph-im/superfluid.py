from eth_utils import is_address
from web3 import Web3

from errors import InvalidAddressError


def normalize_address(address: str) -> str:
    if is_address(address):
        return Web3.to_checksum_address(address)
    else:
        raise InvalidAddressError("f{address} is invalid")
