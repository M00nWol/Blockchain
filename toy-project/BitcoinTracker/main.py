# main.py
from fetch_tx_data import fetch_transaction_data
from parse_tx_data import parse_transaction_data

def main():
    tx_id = '0d378f65ffe80e044712ffedae5a9563d9a74308ab13790cf43df05405b77a5b'

    # 트랜잭션 데이터 가져오기
    tx_data = fetch_transaction_data(tx_id)

    if tx_data:
        # 트랜잭션 데이터 파식
        parsed_data = parse_transaction_data(tx_data)

        # 결과 출력
        print(f"Transaction Time: {parsed_data['time']}")
        print("Senders: ")
        for sender, amount in parsed_data['senders']:
            print(f"    Address: {sender}, Amount: {amount} BTC")

        print("Receivers: ")
        for receiver, amount in parsed_data['receivers']:
            print(f"    Address: {receiver}, Amount: {amount} BTC")

if __name__ == "__main__":
    main()