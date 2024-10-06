import requests

def fetch_transaction_data(tx_id):
    # BlockCypher API URL
    url = f'https://blockchain.info/rawtx/{tx_id}'

    try:
        # API 요청
        response = requests.get(url)
        response.raise_for_status()  # 오류가 있으면 예외 발생
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err} - URL: {url}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# 예시 트랜잭션 ID
tx_id = '0d378f65ffe80e044712ffedae5a9563d9a74308ab13790cf43df05405b77a5b'
tx_data = fetch_transaction_data(tx_id)

# 결과 확인
if tx_data:
    print(tx_data)

if __name__ == '__main__':
    fetch_transaction_data(tx_id)
