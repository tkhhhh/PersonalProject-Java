from demo.Detail import CharDeal
import sys


class Main(object):
    def DealMethod(self,input,output):
        CharDeals = CharDeal()
        FIn = open(input,encoding='utf-8')
        strling = FIn.read()
        lines = CharDeals.LineCount(strling)
        characters = CharDeals.CharCount(strling)
        total_num, new_wordlist, word_num = CharDeals.WordsCount(characters,strling)
        FOut = open(output,encoding='utf-8')
        FOut.write("characters:" + characters + "\n")
        FOut.write("words:" + total_num + "\n")
        FOut.write("lines:" + lines + "\n")
        for i in range(len(word_num)):
            FOut.write(new_wordlist[i] + word_num[i] + "\n")
        FIn.close()
        FOut.close()

if __name__ == "__main__":
    input = sys.argv[1]
    output = sys.argv[2]
    main = Main()
    main.DealMethod(input,output)