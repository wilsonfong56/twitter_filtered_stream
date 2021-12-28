import twapi
import functions
import schedule
import time

def term_search_write(search_str: str, re_expression: str, file_name: str, conditional: "function") -> None:
    print("Working...")
    terms_list = functions.timeline_search(search_str, re_expression)
    file1 = open(file_name, 'a')
    for term in terms_list:
        if conditional(term):
            file1.write(term+"\n")
    file1.close()

def term_search_dict(terms_dict: dict, search_str: str, re_expression: str, conditional: "function") -> None:
    print("Working...")
    terms_list = functions.timeline_search(search_str, re_expression)
    for term in terms_list:
        if conditional(term):
            if term not in terms_dict:
                terms_dict[term] = 1
            else:
                terms_dict[term] += 1
    

def print_terms_from_file(file_name: str) -> None:
    terms_dict = {}
    f = open(file_name, "r")
    for term in f.readlines():
        if term.strip() not in terms_dict:
            terms_dict[term.strip()] = 1
        else:
            terms_dict[term.strip()] += 1
    for i in sorted(terms_dict.items(), key=lambda kv:(kv[1], kv[0]), reverse=True):
        print(i[0][1:] + " "*(6-len(i[0])) + "     " + str(i[1]))

if __name__ == "__main__":
    term_dict = {}
    schedule.every(5).minutes.do(term_search_dict, term_dict, "$", "[$][a-zA-Z]+", "tickers.txt", lambda x : len(x) < 7)
    #schedule.every(5).minutes.do(term_search_write, "$", "[$][a-zA-Z]+", "tickers.txt", lambda x : len(x) < 7)
    while True:
        schedule.run_pending()
        time.sleep(1)
    print_terms_from_file("tickers.txt")
