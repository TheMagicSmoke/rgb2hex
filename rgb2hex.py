import hexValues as hv # import the dictionary

# Outputs a reversed binary string after conversion from decimal
def decimalToBinaryReversed(decimal) :
    binaryString = ''

    if decimal in [1,0] : return str(decimal)
    # If decimal value is outside the rgb value range, approximate to the nearest boundary value
    if decimal < 0 : decimal = 0
    elif decimal > 255 : decimal = 255

    while decimal != 1 :
        remainder = decimal % 2
        binaryString = binaryString + str(remainder)
        decimal = decimal // 2

    binaryString = binaryString + '1'
    return binaryString

# Outputs hex string after conversion from binary
def binaryToHex(binaryString) :

    # The binary string is converted to a standard form of 8 bits (to represent 0 to 255)
    sizeOfString = len(binaryString)
    zeroesToPad = 8 - sizeOfString
    #depending on length of string, zeroes are padded to standardize it to 8 bits
    for i in range(zeroesToPad) : binaryString = binaryString + '0'
    binaryString = binaryString[::-1] # Because input binary string was already reversed

    # Each 4bit of the 8bit binary string gives a hex digit
    hexString = hv.hexDict[binaryString[:4]] + hv.hexDict[binaryString[4:]]
    return hexString # contains 2 hex digits representing 8bits or 1 byte

#Parent function to convert rgb values to hex
def rgbToHex(rgbCode) :
    hexcode = '#' #hex color code starts with #

#Pad hex code for each 8bit rgb value to give the final 6 digit hex value for the rgb code
    for color in rgbCode :
        hexcode = hexcode + binaryToHex(decimalToBinaryReversed(color))

    return hexcode #return the hexcode


# print(binaryToHex(decimalToBinaryReversed(255)))
