import json
import hashlib #for hashfunction


transactions = [ "[3, 4, 5, 6]", "[4, 5, 6, 7]", "[5, 6, 7, 8]", "[6, 7, 8, 9]", "[7, 8, 9, 10]", "[8, 9, 10, 11]", "[9, 10, 11, 12]", "[10, 11, 12, 13]", "[11, 12, 13, 14]", "[12, 13, 14, 15]"]

### Block의 구성 요소 : Block number / Previous Hash / Transaction / Hash / Nonce

block = []

def new_block(i):
    file_name = str(i) + ".json"

    if i==0:
        genesis_block = {
            "Block number" : 0,
            "Previous Hash" : None,
            "Hash" : "Genesis",
            "Nonce" : 0,
            "Transaction" : transactions[0]
        }
        block.append(genesis_block)

    else:
        new_block = {
            "Block number" : i,
            "Previous Hash" : hash(block[i-1]),
            "Hash" : "Genesis",
            "Nonce" : 0,
            "Transaction" : transactions[i]
        }
        block.append(new_block)

    with open(file_name, 'w+') as f:
        json.dump(block[i], f, indent=4)

        
## 해시 암호화 함수
def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()   # hash 라이브러리로 sha256 사용
    return hashlib.sha256(block_string).hexdigest()    


for i in range(len(transactions)):
    print(i)
    print(transactions[i])
    new_block(i)


