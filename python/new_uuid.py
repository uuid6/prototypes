import time
import random

sequenceCounter = 0
_last_timestamp = 0
_last_uuid_int = 0
_last_sequence = None
uuidVariant = '10'

def uuid1(clock_seq=None, devDebugs=False, returnType="hex"):
    """Generates a 128-bit version 1 UUID with 100-ns timestamp RFC 4122 Epoch and random node

    example: dc38cdf9-22fe-11eb-a595-05480e4ca6cb

    format: time_low|time_mid|version|time_high|variant|clock_seq_high|clock_seq_low|node

    Adapted from https://github.com/python/cpython/blob/3.9/Lib/uuid.py

    Test Decode here: https://www.uuidtools.com/decode

    :param clock_seq: Set value to define manually
    :param devDebugs: True, False
    :param returnType: bin, int, hex
    :return: bin, int, hex
    """

    global _last_timestamp
    version = "0001"

    nanoseconds = time.time_ns()
    # 0x01b21dd213814000 is the number of 100-ns intervals between the
    # UUID epoch 1582-10-15 00:00:00 and the Unix epoch 1970-01-01 00:00:00.
    timestamp = (nanoseconds // 100) + 0x01b21dd213814000

    if _last_timestamp is not None and timestamp <= _last_timestamp:
        timestamp = _last_timestamp + 1
    _last_timestamp = timestamp
    if clock_seq is None:
        clock_seq = random.getrandbits(14) # instead of stable storage

    time_low = timestamp & 0xffffffff
    time_mid = (timestamp >> 32) & 0xffff
    time_hi_version = (timestamp >> 48) & 0x0fff
    time_hi_version = int(version + f'{time_hi_version:012b}', 2)
    clock_seq_low = clock_seq & 0xff
    clock_seq_hi_variant = (clock_seq >> 8) & 0x3f
    clock_seq_hi_variant = int(uuidVariant + f'{clock_seq_hi_variant:08b}'[-6:], 2)
    node = random.getrandbits(48) # Instead of MAC

    UUIDv1_bin = "{0}{1}{2}{3}{4}{5}".format(f'{time_low:032b}',
                                            f'{time_mid:016b}',
                                            f'{time_hi_version:016b}',
                                            f'{clock_seq_hi_variant:08b}',
                                            f'{clock_seq_low:08b}',
                                            f'{node:048b}')

    UUIDv1_int = int(UUIDv1_bin, 2)
    UUIDv1_hex = hex(int(UUIDv1_bin, 2))[2:]
    UUIDv1_formatted = '-'.join([UUIDv1_hex[:8], UUIDv1_hex[8:12], UUIDv1_hex[12:16], UUIDv1_hex[16:20], UUIDv1_hex[20:32]])

    if devDebugs:
        print("UUIDv1 Con: {0}|{1}|{2}|{3}|{4}|{5}".format(f'{time_low:032b}',
                                                           f'{time_mid:016b}',
                                                           f'{time_hi_version:016b}',
                                                           f'{clock_seq_hi_variant:08b}',
                                                           f'{clock_seq_low:08b}',
                                                           f'{node:048b}'))
        print("UUIDv1 Bin: {0} (len: {1})".format(UUIDv1_bin, len(UUIDv1_bin)))
        print("UUIDv1 Int: {0}".format(UUIDv1_int))
        print("UUIDv1 Hex: " + UUIDv1_formatted)
        print("\n")

    return UUIDv1_formatted

def uuid6(clock_seq=None, devDebugs=False, returnType="hex"):
    """Generates a 128-bit version 6 UUID with 100-ns timestamp RFC 4122 Epoch without re-ordering bits

    example: 1eb22fe4-3f0c-62b1-a88c-8dc55231702f

    format: time_high|time_mid|version|time_low|variant|clock_seq_high|clock_seq_low|node

    :param clock_seq: Set value to define manually
    :param devDebugs: True, False
    :param returnType: bin, int, hex
    :return: bin, int, hex
    """

    global _last_timestamp
    version = "0110"

    nanoseconds = time.time_ns()
    # 0x01b21dd213814000 is the number of 100-ns intervals between the
    # UUID epoch 1582-10-15 00:00:00 and the Unix epoch 1970-01-01 00:00:00.
    timestamp = (nanoseconds // 100) + 0x01b21dd213814000

    if _last_timestamp is not None and timestamp <= _last_timestamp:
        timestamp = _last_timestamp + 1
    _last_timestamp = timestamp
    if clock_seq is None:
        clock_seq = random.getrandbits(14) # instead of stable storage

    # Start Changes
    new_time_high_mid = f'{timestamp:060b}'[:48] # most-sig 48 time
    new_time_low_version = version + f'{timestamp:060b}'[-12:] # most-sig version + least-sig 12 time
    # Convert to fit the old UUIDv1 variable naming
    time_low = int(new_time_high_mid[:32], 2)
    time_mid = int(new_time_high_mid[-16:], 2)
    time_hi_version = int(new_time_low_version, 2)
    # End Changes

    clock_seq_low = clock_seq & 0xff
    clock_seq_hi_variant = (clock_seq >> 8) & 0x3f
    clock_seq_hi_variant = int(uuidVariant + f'{clock_seq_hi_variant:08b}'[-6:], 2)
    node = random.getrandbits(48)

    UUIDv6_bin = "{0}{1}{2}{3}{4}{5}".format(f'{time_low:032b}',
                                             f'{time_mid:016b}',
                                             f'{time_hi_version:016b}',
                                             f'{clock_seq_hi_variant:08b}',
                                             f'{clock_seq_low:08b}',
                                             f'{node:048b}')
    UUIDv6_int = int(UUIDv6_bin, 2)
    UUIDv6_hex = hex(int(UUIDv6_bin, 2))[2:]
    UUIDv6_formatted = '-'.join([UUIDv6_hex[:8], UUIDv6_hex[8:12], UUIDv6_hex[12:16], UUIDv6_hex[16:20], UUIDv6_hex[20:32]])

    if devDebugs:
        print("UUIDv6 Con: {0}|{1}|{2}|{3}|{4}|{5}".format(f'{time_low:032b}',
                                                           f'{time_mid:016b}',
                                                           f'{time_hi_version:016b}',
                                                           f'{clock_seq_hi_variant:08b}',
                                                           f'{clock_seq_low:08b}',
                                                           f'{node:048b}'))
        print("UUIDv6 Bin: {0} (len: {1})".format(UUIDv6_bin, len(UUIDv6_bin)))
        print("UUIDv6 Int: {0}".format(UUIDv6_int))
        print("UUIDv6 Hex: " + UUIDv6_formatted)
        print("\n")

    if returnType.lower() == "bin":
        return UUIDv6_bin
    if returnType.lower() == "int":
        return UUIDv6_int
    if returnType.lower() == "hex":
        return UUIDv6_formatted

def uuid8(epochType="unix", timestampLength=64, customNode=None, devDebugs=False, returnType="hex"):
    """ Generates a 128-bit version 8 UUID with variable length timestamp, sequence and node.

    example: 1645f70f-066f-8a82-8413-f05792814889

    format: time_high|version|time_or_sequence|variant|node

    :param epochType: Unix or Gregorian
    :param timestampLength: Integer 32, 48, 64 (really 60, 4 least significant bits will be cut off)
    :param customNode = Integer value
    :param devDebugs: True, False
    :param returnType: bin, int, hex
    :return: bin, int, hex
    """

    global _last_timestamp
    global _last_uuid_int
    global _last_sequence
    global sequenceCounter
    global uuidVariant
    uuidVersion = '1000' # ver 8

    if devDebugs == None:
        devDebugs = False

    ### Timestamp Work
    # These can likely be done better with bitwise operations
    # If 48 or 64 bit precision required need time_ns()
    epochTypes = ["unix", "gregorian"]
    if epochType.lower() not in epochTypes:
        raise ValueError("Epoch must either be Unix or Gregorian")

    timestampLengths = [32, 48, 64]
    if timestampLength not in timestampLengths:
        raise ValueError('timestampLength integer must be a value of 32, 48, 64')

    if timestampLength == 32:  # Padded to 64 bits
        timestamp = int(time.time())
        if epochType.lower() == "gregorian":
            raise ValueError('gregorian epoch cannot be used with 32-bit timestamp, change to unix')
        binaryTimestamp = f'{timestamp:032b}' + f'{int(0):032b}'  # 64 1/0s
        time_high = binaryTimestamp[:48]  # Most significant 48
        time_low = binaryTimestamp[-16:]  # Least significant 16
        time_msb_low = time_low[:12]  # Most significant 12 of those 16
    elif timestampLength == 48:  # Trimmed to 48 bits
        timestamp = time.time_ns()
        if epochType.lower() == "gregorian":
            raise ValueError('gregorian epoch cannot be used with 48-bit timestamp, change to unix')
        binaryTimestamp = f'{timestamp:064b}'  # 64 1/0s
        time_high = binaryTimestamp[:48]  # Most significant 48
        time_msb_low = f'{int(0):012b}'  # 12 0s
    elif timestampLength == 64:  # Trimmed to 60 bits
        timestamp = time.time_ns()
        if epochType.lower() == "gregorian":
            # 0x01b21dd213814000 is the number of 100-ns intervals between the
            # UUID epoch 1582-10-15 00:00:00 and the Unix epoch 1970-01-01 00:00:00.
            timestamp = (timestamp // 100) + 0x01b21dd213814000
        binaryTimestamp = f'{timestamp:064b}'  # 64 1/0s
        time_high = binaryTimestamp[:48]  # Most significant 48
        time_low = binaryTimestamp[-16:]  # Least significant 16
        time_msb_low = time_low[:12]  # Most significant 12 of those 16

    if int(timestamp) < int(_last_timestamp) and _last_timestamp != 0:
        raise ValueError("Timestamp lower than previous known timestamp")

    if devDebugs == True:
        print("Curr Timestamp: {0}".format(int(timestamp)))
        print("Last Timestamp: {0}".format(int(_last_timestamp)))

    ### Sequence Work
    # Sequence starts at 0, increments if timestamp is the same the sequence increments by 1
    # Resets if timestamp int is larger than _last_timestamp used for UUID generation
    if timestamp <= _last_timestamp:
        sequenceCounter = int(sequenceCounter) + 1
        if devDebugs == True:
            print("Sequence: Incrementing Sequence to {0}".format(str(sequenceCounter)))
    if timestamp > _last_timestamp:
        sequenceCounter = 0
        # Bug:
        # When using 48-bit trimmed NS timestamp, if two sequence 0s happen to occur in a row, random is tiebreaker.
        # Relying on random can make the UUID integer smaller break sort on that UUID.
        # Quick Fix, just check if last sequence was the same, then increment
        if _last_sequence == 0 and timestampLength == 48:
            sequenceCounter = _last_sequence + 1
        if devDebugs == True:
            print("Sequence: Setting to {0}".format(str(sequenceCounter)))

    # 32 and 48 will use time_or_seq as sequence
    # 64 will use part of node as seq
    # 32 also require more sequence space per timestamp tick thus more bits
    if (timestampLength == 32) or (timestampLength == 48):
        sequenceCounterBin = f'{sequenceCounter:012b}'
    else:
        sequenceCounterBin = f'{sequenceCounter:08b}'

    # Set these two before moving on
    _last_timestamp = timestamp
    _last_sequence = int(sequenceCounter)

    ### Node Work
    if (timestampLength == 32) or (timestampLength == 48):
        time_or_seq = sequenceCounterBin # Set to sequence
        if customNode == None:
            randomInt = random.getrandbits(62)
            randomBinary = f'{randomInt:062b}'
            node = randomBinary
        else:
            node = f'{customNode:062b}'
    if timestampLength == 64:
        time_or_seq = time_msb_low
        if customNode == None:
            randomInt = random.getrandbits(54)
            randomBinary = f'{randomInt:054b}'
            node = sequenceCounterBin + randomBinary
        else:
            node = sequenceCounterBin + f'{customNode:054b}'


    ### Formatting Work
    # Bin merge and Int creation
    # UUIDv8_bin = time_high + uuidVersion + time_msb_low + uuidVariant + sequenceCounterBin + randomBinary
    UUIDv8_bin = time_high + uuidVersion + time_or_seq + uuidVariant + node
    UUIDv8_int = int(UUIDv8_bin, 2)
    if devDebugs == True: # Compare previous Int. Should always be higher
        if UUIDv8_int < _last_uuid_int  and _last_uuid_int != 0:
            print("Error: UUID went Backwards!")
            print("UUIDv8 Last: " + str(_last_uuid_int))
            print("UUIDv8 Curr: " + str(UUIDv8_int))
    _last_uuid_int = UUIDv8_int

    # Convert Hex to Int then splice in dashes
    UUIDv8_hex = hex(int(UUIDv8_bin, 2))[2:]
    UUIDv8_formatted = '-'.join([UUIDv8_hex[:8], UUIDv8_hex[8:12], UUIDv8_hex[12:16], UUIDv8_hex[16:20], UUIDv8_hex[20:32]])

    if devDebugs == True:
        print("UUIDv8 Con: {0}|{1}|{2}|{3}|{4}".format(time_high, uuidVersion, time_or_seq, uuidVariant, node))
        print("UUIDv8 Bin: {0} (len: {1})".format(UUIDv8_bin, len(UUIDv8_bin)))
        print("UUIDv8 Int: " + str(UUIDv8_int))
        print("UUIDv8 Hex: " + UUIDv8_formatted)
        print("\n")

    if returnType.lower() == "bin":
        return UUIDv8_bin
    if returnType.lower() == "int":
        return UUIDv8_int
    if returnType.lower() == "hex":
        return UUIDv8_formatted