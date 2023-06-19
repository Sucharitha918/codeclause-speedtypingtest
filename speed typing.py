import time

def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence:")
    print(text)
    input("Press Enter when you are ready to start.")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    speed = words_typed / elapsed_time
    speed_per_minute = speed * 60
    
    
