import Parser
import ParserException
import Program

class Interpeter:

    #TODO
    def main(self):
        try:
            parse = Parser("test4.jl")
            pro = Program(parse)
            pro.parse()
        except:
            print('Parser Exception')
            #TODO: What's the right way to do this?


    if __name__ == '__main__':
        main()

