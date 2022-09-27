#Assignment:  

class HashTable:
    
    def __init__(self, m):
        self.m = m
        self.hashtable = self.create_hash_table()
        
    #Linear Probing   
    def liner_probing(self,val,line_hash_table):
        index = val % len(line_hash_table)       
        while True:    
            if line_hash_table[index] == "0":            
                line_hash_table[index] = val
                break
            else:
                index = (index+1)%len(line_hash_table)                
    #Linear Probing        
    def create_liner_probing(self):
        arr = [30,46,21,8,44,97,14,210,66]
        line_hash_table = ["0"]*15        
        for i in range(len(arr)):
            self.liner_probing(arr[i],line_hash_table)
        print(f"liner probing:{line_hash_table}")
    
    def create_hash_table(self):
        return [ [] for _ in range(self.m) ]
    
    def _prehash(self, key):
        #challenge: handle negative keys and string
        if (type(key) == str):
            key = hash(key)  #returns a number for you
            
        if ((type(key) == int) | (type(key) == float)):
            if (key < 0):
                key = hash(float(key)) * -1  #first convert to float, then hash it
        
        assert (key > 0) & (type(key) == int)
    
        return key
    
    def _hash(self, key):
        #get the position using division method
        index = key % self.m
        bucket = self.hashtable[index]
        return bucket
    
    def insert(self, key, val):
        
        key    = self._prehash(key)  #clean neg numbers or string
        bucket = self._hash(key)     #get the position of the hashtable
        
        found = False
        # #check whether the key duplicates
        # for i, (bkey, bval) in enumerate(bucket):
        #     if bkey == key:
        #         found = True
        #         pos_dup = i
        #         break
        found, pos_dup, _ = self.search(key)
                
        #if the key duplicates, only update the value
        if(found):
            bucket[pos_dup] = (key, val)
        else: #if the key does not exist, append and #if something is there already, append
            bucket.append((key, val))
            
        print(self.hashtable)
    
    def search(self, key):
        #if you finish this, 
        key = self._prehash(key)
        
        #perform the division method
        bucket = self._hash(key)     #get the position of the hashtable

        found  = False
        answer = -9999
        pos_dup = -9999
        #loop the bucket index
        for i, (bkey, bval) in enumerate(bucket):
            if bkey == key:
                found   = True
                pos_dup = i
                answer  = bval
                break
                
        return found, pos_dup, answer  
    
    def delete(self, key):
        #implement this too
        found,_,val = ht.search(key)
        if found:          
            bucket = self._hash(key)  
            bucket.remove((key,val))
            print(f"atfer deleting,the hashtable is {ht.hashtable}")           
        else:
            print(f"this key is not in the hashtable:{ht.hashtable}")
        
    
ht = HashTable(11)
ht.insert(1, 'Chaky')
ht.insert(2, 'Peter')
ht.insert(2, 'oliii')
ht.insert(3, 'John')
ht.insert(12, 'Matthew')  #this should be in the same bucket with 'Chaky'


found, _, val = ht.search(12)
print(found, val)
ht.delete(3)
ht.delete(5)
#Linear Probing
ht.create_liner_probing()
