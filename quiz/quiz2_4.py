'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''
import money as money
import self as self

class Multi_card:
    def __init__(self):
        self.card = 0
        print('카드가 발급 되었습니다.')

    # 충전기능
    def charge(self, money):
        self.card += money
        print('{}이 충전되었습니다.'.format(self.card))

    # 소비기능
    def consume(self,money,place):
        if self.card >= money:
            if place =='영화관':
                Movie_Card.consume(self,money,place)
            elif place =='마트':
                Mart_Card.consume(self,money,place)
            elif place =='교통':
                Trans_Card.consume(self,money,place)
            else:
                self.card -= money
                print('{}에서 {}원을 사용했습니다.'.format(place, money))
        else:
            print('잔액이 부족합니다.')
    # 잔액
    def print(self):
        print('잔액이 {}입니다'.format(self.card))

#영화관 20%할인
class Movie_Card(Multi_card):
    def consume(self,money,place):
        if place == '영화관':
            money =money * 0.8
            self.card -= money
            print('{}에서 {}원을 사용했습니다.'.format(place, money))
        else:
            print('영화관이 아닙니다.')

# 마트 10%할인
class Mart_Card(Multi_card):
    def consume(self,money,place):
        if place == '마트':
            money = money * 0.9
            self.card -= money
            print('{}에서 {}원을 사용했습니다.'.format(place, money))
        else:
            print('마트가 아닙니다.')

# 교통 20%할인
class Trans_Card(Multi_card):
    def consume(self,money,place):
        if place == '교통':
            money = money * 0.9
            self.card -= money
            print('{}에서 {}원을 사용했습니다.'.format(place, money))
        else:
            print('교통이 아닙니다.')


multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()
