import struct


def conceal(msg):
    bs = msg.encode("utf")
    n = len(bs)
    if len(bs) > 6:
        raise ValueError()
    first = b"\x7f"
    second = (0xF8 ^ n).to_bytes(1, "big")
    padding = b"\x00" * (6 - n)
    payload = bs
    return struct.unpack(">d", first + second + padding + payload)[0]


def extract(msg):
    bs = struct.pack(">d", msg)
    n = bs[1] & 0x07
    return bs[-n:].decode("utf8")


if __name__ == "__main__":
    cases = ("secret", "😘", " ")
    for case in cases:
        x = conceal(case)
        assert isinstance(x, float)
        assert repr(x) == "nan"
        assert extract(x) == case
