import twapi
import functions
import schedule
import time

def main():
    print("Working...")
    ticker_list = functions.timeline_search("$", "[$][a-zA-Z]+")
    file1 = open("tickers.txt", 'a')
    for ticker in ticker_list:
        if len(ticker) < 7:
            file1.write(ticker+"\n")
    file1.close()

def run(f):
    schedule.every(5).minutes.do(f)
    while True:
        schedule.run_pending()
        time.sleep(1)

def print_tickers_dict(file_name):
    tickers_dict = {}
    f = open(file_name, "r")
    for ticker in f.readlines():
        if ticker.strip() not in tickers_dict:
            tickers_dict[ticker.strip()] = 1
        else:
            tickers_dict[ticker.strip()] += 1
    for i in sorted(tickers_dict.items(), key=lambda kv:(kv[1], kv[0]), reverse=True):
        print(i[0][1:] + " "*(6-len(i[0])) + "     " + str(i[1]))

if __name__ == "__main__":
    #run(main)
    print_tickers_dict("tickers.txt")
