import random
suits = ["clubs", "diamonds", "hearts", "spades"] # list các suits
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "jack", "queen", "king", "ace"] # list các faces
keep_going = True  # Boolean variable
while keep_going:  # mới đầu keep_going là True
    my_face = random.choice(faces) # bạn chọn một face ngẫu nhiên
    my_suit = random.choice(suits) # bạn chọn một suit ngẫu nhiên
    your_face = random.choice(faces) # computer chọn một face ngẫu nhiên
    your_suit = random.choice(suits) # computer chọn một suit ngẫu nhiên
    print("I have the", my_face, "of", my_suit)
    print("You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print("I win!")  # tôi thắng
    elif faces.index(my_face) < faces.index(your_face): # elif : else if
        print("You win!")  # bạn thắng
    else:
        print("It's a tie!")  # huề
    answer = input("Hit [Enter] to keep going, any key to exit: ") # muốn tiếp tục đánh bài thì nhấn nút ENTER, trái lại thì bấm bất cứ nút nào trên bàn phím
    keep_going = (answer == "") # bấm ENTER thì keep_going vẫn là True nên vòng loop WHILE vẫn tiếp tục. Trái lại nó không True tức là FALSE thì máy ngưng