from trezor import wire
from trezor.messages import MessageType

from apps.common import HARDENED


def boot():
    ns = [
        ["secp256k1", HARDENED | 44, HARDENED | 128],
        ["ed25519", HARDENED | 44, HARDENED | 128],
    ]
    wire.add(MessageType.MoneroGetAddress, __name__, "get_address", ns)
    wire.add(MessageType.MoneroGetWatchKey, __name__, "get_watch_only", ns)
    wire.add(MessageType.MoneroTransactionInitRequest, __name__, "sign_tx", ns)
    wire.add(
        MessageType.MoneroKeyImageExportInitRequest, __name__, "key_image_sync", ns
    )

    if __debug__ and hasattr(MessageType, "DebugMoneroDiagRequest"):
        wire.add(MessageType.DebugMoneroDiagRequest, __name__, "diag")
