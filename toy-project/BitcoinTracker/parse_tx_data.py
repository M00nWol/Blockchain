# parse_tx_data.py
from datetime import datetime, timezone

def parse_transaction_data(tx_data):
    # 트랜잭션 시간
    timestamp = tx_data.get('time')
    tx_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S') if timestamp else 'Unknown'

    # 보낸 주소와 금액
    inputs = tx_data.get('inputs', [])
    senders = [(inp['prev_out']['addr'], inp['prev_out']['value'] / 1e8) for inp in inputs if 'prev_out' in inp]

    # 받은 주소와 금액
    outputs = tx_data.get('out', [])
    receivers = [(out['addr'], out['value'] / 1e8) for out in outputs if 'addr' in out]

    return {
        'time': tx_time,
        'senders': senders,
        'receivers': receivers,
    }

if __name__ == "__main__":
    # 테스트용 코드
    sample_data = {
        'time': 1609459200,  # 2021-01-01 00:00:00 UTC
        'inputs': [{'prev_out': {'addr': 'sender_address', 'value': 100000000}}],
        'out': [{'addr': 'receiver_address', 'value': 100000000}]
    }
    parsed_data = parse_transaction_data(sample_data)
    print(parsed_data)
