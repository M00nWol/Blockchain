# main.py
from fetch_tx_data import fetch_transaction_data
from parse_tx_data import parse_transaction_data,get_confirmations
from address_utils import fetch_address_data, calculate_address_balance

def main():
    tx_id = '0d378f65ffe80e044712ffedae5a9563d9a74308ab13790cf43df05405b77a5b'

    # 트랜잭션 데이터 가져오기
    tx_data = fetch_transaction_data(tx_id)

    if tx_data:
        # 트랜잭션 데이터 파식
        parsed_data = parse_transaction_data(tx_data)

        confirmations = get_confirmations(tx_data)

        # 결과 출력
        print(f"Transaction ID : {tx_id}")
        print(f"Transaction Time: {parsed_data['time']}")
        print(f"Confirmations: {confirmations}")
        print("Senders:")
        for sender, amount in parsed_data['senders']:
            print(f"  Address: {sender}, Amount: {amount} BTC")

        print("Receivers:")
        for receiver, amount in parsed_data['receivers']:
            print(f"  Address: {receiver}, Amount: {amount} BTC")


     # 비트코인 주소 입력 및 유효성 검사
    address = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'

    # 주소 데이터 가져오기 및 잔액 확인
    address_data = fetch_address_data(address)
    if address_data:
        balance = calculate_address_balance(address_data)
        print(f"Address : {address}")
        print(f"Address Balance: {balance} BTC")


if __name__ == "__main__":
    main()