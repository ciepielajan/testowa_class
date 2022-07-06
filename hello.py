class Hello():
  def __init__(self, message:str="Hello World"):
    self.message_row = message
    self.message_lower = self.get_lower_text()
    
  def get_lower_text(self) -> str:
    return self.message_row.lower()
    
