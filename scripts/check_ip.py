import requests
RETRY_NUMBER = 5


if __name__ == '__main__':
    count = 0
    while count < RETRY_NUMBER:
        try:
            resp = requests.get("http://checkip.amazonaws.com/")
            print(resp.text.strip())
            break
        except Exception:
            count += 1
            continue
