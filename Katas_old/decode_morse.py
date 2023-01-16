MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
              '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
              '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
              '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

import re



# def decode_bits(bits):
#     bits = bits.strip('0')
#     if "0" not in bits:
#         return "."
#
#     signal_length = min(min(len(c) for c in re.findall(r'(1+)', bits.strip('0'))), min(len(c) for c in re.findall(r'(0+)', bits.strip('0'))))
#
#     bits = bits.strip('0')[::min(min(len(c) for c in re.findall(r'(1+)', bits.strip('0'))), min(len(c) for c in re.findall(r'(0+)', bits.strip('0'))))].replace("0000000", "   ").replace("000", " ").replace("111", "-").replace("1", ".").replace("0","")
#     return bits
decode_bits = lambda bits: "." if "0" not in bits.strip('0') else bits.strip('0')[::min(min(len(c) for c in re.findall(r'(1+)', bits.strip('0'))), min(len(c) for c in re.findall(r'(0+)', bits.strip('0'))))].replace("0000000", "   ").replace("000", " ").replace("111", "-").replace("1", ".").replace("0","")

decode_morse = lambda code: " ".join("".join(MORSE_CODE[c] for c in w.split(" ")) for w in code.strip().split('   '))

bits = '10001'
code = '. .'
print(decode_bits(bits) == code)

zero_reg = r'(0+)'

a = min(len(c) for c in re.findall(zero_reg, bits.strip("0")))
bits = bits[::a].replace("0000000", "   ").replace("000", " ").replace("111", "-").replace("1", ".").replace("0", "")
