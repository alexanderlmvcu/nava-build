class Repository(object):
 def __init__(self, adapter=None):
   self.client = adapter()

 def find_all(self, selector):
   return self.client.find_all(selector)
 
 def find(self, selector):
   return self.client.find(selector)
 
 def create(self, wave):
   return self.client.create(wave)
  
 def update(self, selector, wave):
   return self.client.update(selector, wave)
  
 def delete(self, selector):
   return self.client.delete(selector)