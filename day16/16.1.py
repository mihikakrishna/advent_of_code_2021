class Packet:
    def __init__(self,bitString):
        self.VID , self.TID = self.find_VID_TID(bitString)
        self.type = "literal" if self.TID == 4 else "operator"
        self.LTID = -1
        if self.type == "operator" : self.LTID = int(bitString[6])
        self.packets = []
    
    def find_VID_TID(self, bitString):
        VID = int(bitString[0:3],2)
        TID = int(bitString[3:6],2)
        return VID,TID

def parse_literal(bitString):
    literal_string = ""
    lead_bit = 6
    while(bitString[lead_bit] != '0'):
        literal_string += bitString[lead_bit+1:lead_bit+5]
        lead_bit += 5
    literal_string += bitString[lead_bit+1:lead_bit+5]
    # literal_string = int(literal_string,2)
    # packet_string = bitString[0:lead_bit+5]
    
    # remaining bitString
    return bitString[lead_bit+5:]

def parse_operator(VID_list, bitString):
    packet = Packet(bitString)
    print(packet.LTID)
    if packet.LTID == 0: 
        num_bits = int(bitString[7:22],2)
        print(num_bits)
        sub_packet_str = bitString[22:22+num_bits+1]
        print(sub_packet_str)
        while(len(sub_packet_str) > 6):
            sub_packet = Packet(sub_packet_str)
            VID_list.append(sub_packet.VID)
            if sub_packet.TID == 4: 
                sub_packet_str = parse_literal(sub_packet_str)
            else:
                parse_operator(VID_list,sub_packet_str)

    print(VID_list)
    # else:
    #     num_packets = int(bitString[7:18],2)
      

def hex_to_bin(bitString):
    hex_map = {'0' : '0000','1' : '0001','2' : '0010','3' : '0011','4' : '0100','5' : '0101','6' : '0110','7' : '0111','8' : '1000','9' : '1001',
    'A' : '1010','B' : '1011','C' : '1100','D' : '1101','E' : '1110','F' : '1111'}
    newString = ''
    for char in bitString: newString += hex_map[char]
    return(newString)


# def dfs(input,bitString):
#     stack = []
#     stack.append(bitString)
#     while(stack):
#         currString = stack.pop()
#         stack.append

def solution():
    f = open("day16/16.txt","r")
    input = hex_to_bin(f.readline())


    packets = []

# def find_packets(type,bitString):
#         # parse literal
#     if type == "literal":
#         literal_string = ""
#         lead_bit = 6
         
#         while(bitString[lead_bit] != '0'):
#             literal_string += bitString[lead_bit+1:lead_bit+5]
#             lead_bit += 5
#         literal_string += bitString[lead_bit+1:lead_bit+5]
#         literal_string = int(literal_string,2)
#         print(literal_string)
#         return bitString[lead_bit+5:]
#     return 0
# print(find_packets("literal","110100101111111000101000"))