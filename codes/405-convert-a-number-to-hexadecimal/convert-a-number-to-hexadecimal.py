class Solution:
    def toHex(self, num: int) -> str:
  
        hexa = hex(num & 0xFFFFFFFF)
        hexadcimal = hexa[2:]
        out = f"{hexadcimal}"
        
        return out   