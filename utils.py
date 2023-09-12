class Utils:
  
  @staticmethod 
  def reversed(num: int):
    return int(str(num)[::-1])

  @staticmethod
  def formatter(num: int):
    binary = bin(num)
    octal = oct(num)
    return binary, octal

