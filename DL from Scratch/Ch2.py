##퍼셉트론 구현하기
#AND 논리 회로 구현해보기
def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1 * w1 + x2 * w2
  if tmp <= theta:
    retuen 0
  elif tmp > theta:
    return 1

#입력 신호 넣어보기
AND(0, 0)
AND(1, 0)
AND(0, 1)
AND(1, 1)