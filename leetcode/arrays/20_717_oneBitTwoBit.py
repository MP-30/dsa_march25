bits = [1,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0]

def one_bit_two_bit(bits):
    new_bits = []
    if bits[-1] == 0:
        i = 0
        while i < len(bits):
            added_bit = 'D'
            if bits[i] == 0:
                added_bit = 'C'
                new_bits.append(added_bit)
                # print('C')
            elif bits[i] == 1 and bits[i+1] == 0:
                added_bit = 'A'
                new_bits.append(added_bit)
                # print('A')
            elif bits[i] == 1 and bits[i+1] == 1:
                added_bit = 'B'
                new_bits.append(added_bit)
                # print('B')
            if added_bit == 'C':
                i+=1
            elif added_bit in  ('A','B'):
                i +=2
        if new_bits[-1] == 'C':
            return True
        else: return False
    else: return False
    
print(one_bit_two_bit(bits))