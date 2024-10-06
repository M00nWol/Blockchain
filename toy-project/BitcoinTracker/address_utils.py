# address_utils.py
import re
import requests

def fetch_address_data(address):
    url = f"https://blockchain.info/rawaddr/{address}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err} - URL: {url}')
    except Exception as err:
        print(f'Other error occured: {err}')

def calculate_address_balance(address_data):
    balance = address_data.get('final_balance', 0) / 1e8    # 잔액을 BTC로 변환
    return balance

def is_valid_btc_address(address):
    # 간단한 비트코인 주소 유효성 검사 (비트코인 주소 형식 확인)
    pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
    return pattern.match(address) is not None

if __name__ == "__main__":
    # 테스트용 코드
    address = input("Enter a Bitcoin address: ")
    if is_valid_btc_address(address):
        print(f"The address {address} is valid.")
        address_data = fetch_address_data(address)
        if address_data:
            balance = calculate_address_balance(address_data)
            print(f"Address Balance: {balance} BTC")
    else:
        print(f"The address {address} is invalid.")