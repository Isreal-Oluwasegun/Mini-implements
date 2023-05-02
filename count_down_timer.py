import time

def count_down(input):
    while input:
        minute, second = divmod(input, 60)
        print("{:02d}:{:02d}".format(minute, second))
        time.sleep(1)
        input -= 1
    
    print("Count down completed")
    

    