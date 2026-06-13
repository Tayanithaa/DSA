class Solution:
    def toHex(self, num: int) -> str:
  
        hexa = hex(num & 0xFFFFFFFF)
        hexadecimal = hexa[2:]
        out = f"{hexadecimal}"
        
        return out   