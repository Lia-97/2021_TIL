# 재귀함수를 이용해 10진수를 2진수로 변환하는 함수 만들기

def dec_to_bin(n):
    # 빈 결과값을 만든다.
    result = ''
    # 인자 n 이 1/2 라면 반환값을 반환하고 함수가 종료된다.
    if n == 1/2:
        return dec_to_bin(n // 2) + result 
    # 인자 n이 홀수라면
    elif n % 2 == 1:
        # result 문자열에 1을 더한다
        result = '1' + result
    # 인자 n이 짝수라면
    elif n % 2 == 0:
        # result 문자열에 0을 더한다.
        result = '0' + result
    
        
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'