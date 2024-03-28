#import pymysql
#from config_bd import *
from tkinter.messagebox import showinfo 
def start(*args):
    global rank_list,count_examples,time,mistakes
    """Needing variables"""

    count_examples = args[0]
    time = args[1]
    mistakes = args[2]
    return calculate_the_rank()



def calculate_the_rank():
    """Calculate percent of mistakes"""

    mst = 0
    for i in mistakes:
        if not i:   mst+=1
    percent = len(mistakes)/mst*100 #Number of errors in percents

    constrain = lambda val, min_val, max_val:   min(max_val, max(min_val, val))
    
    rank_list = ["Noob","Beginner","Intermediate","Professional","Professor"]
    percent = sum(mistakes)/count_examples #Number of correct answers
    end_rank = rank_list[constrain(int(round(count_examples/time * percent**2 * 4)),0,4)]
    showinfo("Результат",end_rank)
    return end_rank
    
def save_to_bd():
    ...
if __name__ == "__main__":
    app = rank()
    print(app.save_to_bd("str"))
