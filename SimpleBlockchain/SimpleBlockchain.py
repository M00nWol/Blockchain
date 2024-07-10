import datetime
import hashlib
import json

class Blockchain:

    def __init__(self):
        self.chain = []
        # 가장 처음 블록인 제네시스(genesis) 블록을 생성
        self.create_block(proof = 1, previous_hash = '0')

    # create_block() : json으로 구조화된 block을 생성하고 chain에 더해줌
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block
    
    # get_previous_block() : chain 리스트에 있는 가장 마지막 블록을 리턴
    def get_previous_block(self):
        return self.chain[-1]
    
    # proof_of_work() : 이전 proof 값을 받고 previous_proof와의 연산 해시 값이 특정 조건을 만족하는 new_proof를 찾아 리턴함
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation.startswith('0000'):
                check_proof = True
            else:
                new_proof += 1

        return new_proof
    
    # hash() : dictionary 형태의 block을 받아서 json으로 dump하고 인코딩하여 해시값을 얻어 리턴함
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
# 블록체인 채굴하기
def main():
    blockchain = Blockchain()
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    print(blockchain.chain)

if __name__ == "__main__":
    main()