from collections import Counter

#every node object will have two children, otherwise is a leave
class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def getChild(self):
        return self.left, self.right

def get_code(node, code = ''):   
    if type(node) is str:
        #stop!!!
        return {node : code}
    
    #get the children
    left, right = node.getChild()
    
    #recursive function
    huffman_code = dict()
    huffman_code.update(get_code(left, code+'0'))
    huffman_code.update(get_code(right, code+'1'))
    
    return huffman_code

def decode(huffman_code,new_message,temp_str,result):
    if len(new_message)<=0:
        if get_key(temp_str,huffman_code):
            result+= get_key(temp_str,huffman_code)
        print(f"after decoding: the message is:{result}")
        return result        
    else:
        s = new_message[0]    
        if get_key(temp_str,huffman_code)==None:
            temp_str+=s           
            if len(new_message)>=1:
                new_message = new_message[1:] 
                decode(huffman_code,new_message,temp_str,result)
            else:            
                return result
        else:            
            result+=get_key(temp_str,huffman_code)
            temp_str =""
            decode(huffman_code,new_message,temp_str,result)
            

         
    
def get_key(val,dict):
    for key, value in dict.items():
         if val == value:
             return key   

#calculate the total cost --> message + table
def calculateTotalCost(freqs,huffman_code):
    total = 0
    for key in list(freqs.keys()):
        total+=freqs[key]*len(huffman_code[key])+len(huffman_code[key])
    print(f"the total cost is(messsage+table):{total}")
    

def make_the_tree(freqs_sorted):
    
    #as long as freqs_sorted.length > 1
    while len(freqs_sorted) > 1:
        
        #combine the two smallest one
        key1, value1 =  freqs_sorted[0]
        key2, value2 =  freqs_sorted[1]
        
        #delete them
        freqs_sorted = freqs_sorted[2:]
        
        #add the new combination to freqs_sorted
        new_value = value1 + value2
        new_node  = Node(key1, key2)
        
        #add to freqs_sorted
        freqs_sorted.append((new_node, new_value))
                
        #sort again!!
        freqs_sorted = sorted(freqs_sorted, key=lambda item: item[1])
      
    return freqs_sorted[0][0]
    #return root node (so we can use this generating coding....)

def encode(huffman_code,message):
    if len(message)==0:
        return 
    new_message = ""
    for m in message:
        new_message+=huffman_code[m]
    
    return new_message

#input
message = 'AAABBBBBBEEEDABEEDCC'

#count the letters
#use Counter, then convert to dictionary
freqs = dict(Counter(message)) #{'A': 4, 'B': 7, 'E': 5, 'D': 2, 'C': 2}
# print(freqs['A'])  #4

#sort them from smallest to biggest
#{'C': 2, 'D': 2, 'A': 4, 'E': 5, 'A': 7}
freqs_sorted = sorted(freqs.items(), key=lambda item: item[1])

#make the tree by combining the smallest one, and delete those guys
root = make_the_tree(freqs_sorted)

#get the code
huffman_code = get_code(root)

new_message = encode(huffman_code,message)
print(f"after encoding,the message is:{new_message}")
#00000011111111111110101001000111010010011011
#print the code
print(huffman_code)
#{'A': '00', 'D': '010', 'C': '011', 'E': '10', 'B': '11'}

#task1: decode the encoded message to the original message
decode(huffman_code,new_message,"","")

#task2: calculate the total cost --> message + table
calculateTotalCost(freqs,huffman_code)
#the total cost is(messsage+table):56
