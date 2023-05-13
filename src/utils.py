from eth_utils import is_address
from web3 import Web3

from errors import InvalidAddressError


def to_bytes32(string):
    encoded_string = string.encode('utf-8')
    if len(encoded_string) > 32:
        raise ValueError("Input string is too long for bytes32")
    padding_length = 32 - len(encoded_string)
    padded_string = encoded_string + b'\x00' * padding_length
    return padded_string


def normalize_address(address: str) -> str:
    if is_address(address):
        return Web3.to_checksum_address(address)
    elif address == "":
        return ""
    else:
        raise InvalidAddressError("f{address} is invalid")
