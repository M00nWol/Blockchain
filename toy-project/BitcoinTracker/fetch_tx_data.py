# fetch_tx_data.py
import requests

def fetch_transaction_data(tx_id):
    url = f'https://blockchain.info/rawtx/{tx_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err} - URL: {url}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def fetch_current_block_height():
    url = 'https://blockchain.info/q/getblockcount'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return int(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

if __name__ == "__main__":
    # 예시 트랜잭션 ID
    tx_id = '0d378f65ffe80e044712ffedae5a9563d9a74308ab13790cf43df05405b77a5b'
    tx_data = fetch_transaction_data(tx_id)
    print(tx_data)  # 구조를 확인하기 위해 출력

    # 현재 블록 높이 가져오기
    current_block_height = fetch_current_block_height()
    print(f"Current Block Height: {current_block_height}")
