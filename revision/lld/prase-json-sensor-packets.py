import  json
import zlib

def parse_packet(raw: bytes) -> dict:
    packet = json.loads(raw)
    payload = packet["payload"]
    expected_checksum = packet["checksum"]

    actual_checksum = zlib.crc32(
        json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    )
    if actual_checksum != expected_checksum:
        raise ValueError("Checksum validation failed")
    return payload