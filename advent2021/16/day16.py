import math

global bitstream, log_indent
with open('input.txt', 'r') as input_file:
    line = [line.strip() for line in input_file.readlines() if len(line) > 1][0]

bitstream = list(''.join([format(int(c, 16), '0>4b') for c in list(line)]))
log_indent = 0


def version_total(packet):
    # log(f"getting value {packet[0][1]} from packet {packet}")
    s = 0
    s += packet[0][1]
    if type(packet[0][0]) == list:
        for p in packet[0][0]:
            s += version_total(p)
    return s


def log(string):
    global log_indent
    print("\t"*log_indent + string)


def read_bits(n):
    global bitstream, log_indent
    log_indent += 1
    log(f"reading {n} bits from {''.join(bitstream)}")
    b = bitstream[:n]
    log(f"read {''.join(b)}")
    del bitstream[:n]
    log_indent -= 1
    return ''.join(b), n


def read_int(n):
    global log_indent
    log_indent += 1
    log(f"reading {n} bit int")
    log_indent -= 1
    return int(read_bits(n)[0], 2), n


def read_literal():
    global log_indent
    log_indent += 1
    log(f"reading literal")
    literal_bits = ''
    n_bits_read = 0

    while True:
        digit_bits = read_bits(5)[0]
        literal_bits += digit_bits[1:]
        n_bits_read += 5
        if digit_bits[0] == '0':
            break

    log_indent -= 1
    return int(literal_bits, 2), n_bits_read


def read_subpackets_by_length():
    global log_indent
    log_indent += 1
    log("reading subpackets by length")
    n_bits_read = 0
    subpackets = []
    log("reading subpacket bit length")
    subpackets_bit_length = read_int(15)[0]
    n_bits_read += 15
    subpacket_length_read = 0
    while subpacket_length_read < subpackets_bit_length:
        log("reading subpacket")
        subpacket, n_read = read_packet()
        n_bits_read += n_read
        subpacket_length_read += n_read
        subpackets.append((subpacket, n_read))
    log_indent -= 1
    return subpackets, n_bits_read


def read_subpackets_by_count():
    global log_indent
    log_indent += 1
    log("reading subpackets by count")
    n_bits_read = 0
    subpackets = []
    log("reading subpacket count")
    subpacket_count = read_int(11)[0]
    n_bits_read += 11
    for n in range(subpacket_count):
        log(f"reading subpacket {n} of {subpacket_count}")
        subpacket, n_read = read_packet()
        subpackets.append((subpacket, n_read))
        n_bits_read += n_read

    log_indent -= 1
    return subpackets, n_bits_read


def read_packet():
    global log_indent
    log_indent += 1
    log("reading packet")
    n_bits_read = 0
    log("reading version")
    version = read_int(3)[0]
    log("reading type_id")
    type_id = read_int(3)[0]
    n_bits_read += 6
    if type_id == 4:
        log("reading literal")
        value, n_read = read_literal()
        n_bits_read += n_read
    else: # Operation packet with subpackets
        log("reading subpacket length type")
        length_type = read_bits(1)
        n_bits_read += 1
        if length_type[0] == '0':
            subpackets, n_read = read_subpackets_by_length()
        else:
            subpackets, n_read = read_subpackets_by_count()
        n_bits_read += n_read
        value = subpackets

    log_indent -= 1
    return (value, version, type_id), n_bits_read


p = read_packet()
print(p)
print(f"version total: {version_total(p)}")

