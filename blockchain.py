import hashlib
import time
#Simple block class which stores info
class Block:
  def __init__(self,index,timestamp,data,previoushash=''):
    self.index= index
    self.timestamp = timestamp
    self.data = data
    self.hash = ''
    self.previoushash = previoushash
    self.nonce = 0
  def generateHash(self):
    return hashlib.sha256(str(str(self.index)+str(self.timestamp)+str(self.data)+str(self.previoushash)).encode('utf-8')).hexdigest()
  def set_hash(self):
    self.hash = self.generateHash()
  def mine_block(self,difficulty):
    while self.hash[0:difficulty] != '0'*difficulty:
      self.nonce+=1
      self.hash = self.generateHash()
    print(self.nonce,self.hash)
#Blockchain class which uses blocks to build the chain
class BlockChain:
  def __init__(self):
    self.difficulty = 1
    genesis_block = Block(1,time.time(),'0.0004555',0)
    genesis_block.set_hash()
    genesis_block.mine_block(self.difficulty)
    self.blocks = [genesis_block]
    print(len(self.blocks))
    self.index = 2
    
  def get_latest_block(self):
    return self.blocks[len(self.blocks)-1]
  def add_block(self,data):
    new_block = Block(self.index,time.time(),'0.03456',self.get_latest_block().hash)
    new_block.set_hash()
    new_block.mine_block(self.difficulty)
    self.blocks.append(new_block)
    self.index+=1
  def verify_blockchain(self):
    i = 1
    while i<len(self.blocks):
      if self.blocks[i].hash != self.blocks[i].generateHash():
        print('current',i,self.blocks[i].hash,self.blocks[i].generateHash())
        return False
      if self.blocks[i].previoushash != self.blocks[i-1].hash:
        print('prev',i,self.blocks[i].previoushash,self.blocks[i-1].hash)
        return False
      i+=1
    return True
shivCoin = BlockChain()
shivCoin.add_block('Some fucked up data')
shivCoin.add_block('Even more fucked up data')
for a in shivCoin.blocks:
  print('hash',a.hash)
  print('previoushash',a.previoushash)
#Now let me verify the BlockChain
print(shivCoin.verify_blockchain())
#Now let me change data of one of the blocks and then verify the BlockChain
print('Changing data.....')
shivCoin.blocks[1].data = 'I don\'t know'
print(shivCoin.verify_blockchain())
