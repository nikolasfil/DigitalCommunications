# from scipy import log2
import math


def compare(inp, d):
    flag = 0
    pointer = ""
    for j in range(len(d)):
        if inp == d[j]:
            flag = 1
            pointer = str(j)
    return str(flag) + pointer


def parsing(inpstr):
    dic = [""]  # empty substring
    prefix = ""
    pointer_bit_dec = [""]
    pfx = 0

    for i in range(len(inpstr)):
        sin = prefix + inpstr[i]
        prefix = ""

        result = compare(sin, dic)  # Comparing with the dictionary

        if result == "0":
            dic.append(sin)
            pointer_bit_dec.append(
                str(bin(pfx)) + sin[-1]
            )  # format: (pointer, extra bit)
        else:
            pfx = int(result[-1])  # Position in dictionary
            prefix = sin

            if i == len(inpstr) - 1:
                sufix = ""
                dic.append(sin + sufix)
                pointer_bit_dec.append(
                    str(bin(pfx)) + ""
                )  # format: (pointer, extra bit)

    return pointer_bit_dec


def encoding(pointerbit, indexbit):
    out_enc = []

    for i in range(len(pointerbit)):
        a = pointerbit[i]
        a = a[2:]

        if len(a) < indexbit + 1:
            b = a.zfill(indexbit + 1)
        else:
            b = a

        out_enc.append(b)

    return out_enc


def main():
    s = "1111100010101010101000110000000001010101000000001001111000010101111110000001010101100"

    pointer_bit = parsing(s)
    numseg = len(pointer_bit)
    index_bits = int(round(math.log(numseg, 2)))
    outstr = ""
    sout = encoding(pointer_bit, index_bits)
    outstr = outstr.join(sout)
    outstr = outstr[index_bits + 1 :]

    num_1 = 0
    num_0 = 0

    for i in range(len(outstr)):
        if outstr[i] == "1":
            num_1 = num_1 + 1
        if outstr[i] == "0":
            num_0 = num_0 + 1

    freq_1 = num_1 / len(outstr)
    freq_0 = num_0 / len(outstr)
    entropy = -((freq_1 * math.log(freq_1, 2)) + (freq_0 * math.log(freq_0, 2)))

    print("\n")
    print("=== Algorithm LOG ===\n")
    print("Number of words in the dictionary   = %d" % (len(pointer_bit)))
    print("Length of the input sequence        = %d bits" % (len(s)))
    print("Length of the output sequence       = %d bits" % (len(outstr)))
    print('Number of "1" bits                  = %d' % (num_1))
    print('Number of "0" bits                  = %d' % (num_0))
    print('Frequency of "1" bits               = %1.4f' % freq_1)
    print('Frequency of "0" bits               = %1.4f' % freq_0)
    print("Entropy from frequencies            = %1.4f bits\n" % entropy)
    print(outstr)


# Standard boilerplate to call the main() function.
if __name__ == "__main__":
    main()
