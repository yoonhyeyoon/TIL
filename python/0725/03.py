# id의 맨끝자리가 숫자인 지 판별하기

def is_id_valid(user_data):
    for key, value in user_data.items():
        if key == 'id':
            try:
                int(value[-1])
                return True
            except ValueError:
                return False