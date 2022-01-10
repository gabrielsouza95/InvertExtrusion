
class InvertGCode:
    def __init__(self, file_name):
        self.inverted_file = open(f'{file_name}_inverted.gcode', 'w')
        self.inverted_file.close()
    
    def invert_file(self, file_name):
        self.passed_inicialization = False
        self.line_readed = 'a'
        self.inverted_file = open(f'{file_name}_inverted.gcode', 'a')
        with open(f'{file_name}.gcode', 'r') as original_code:
            while(self.line_readed):
                self.line_readed = original_code.readline()
                print(self.line_readed)
                self.line_no_comments = self.line_readed.split(';', maxsplit=1)
                self.line_no_comments[0] = self.line_no_comments[0].rstrip() #retira qualquer espaço em branco que possa ter sobrado na frente
                if(self.line_no_comments[0] == 'M107'): #se já passou da parte de configuração e vai entrar no gcode do objeto
                    self.passed_inicialization = True
                if(self.line_no_comments[0] and self.passed_inicialization):
                    self.inverted_file.writeline(self.invert_line(self.line_no_comments[0]))
        self.inverted_file.close()

    def invert_line(self, code_line):
        self.command_line = code_line.split('G1', maxsplit=1)
        if ( self.command_line[0] ): #checa se é linha de comando com extrusora
            self.extruder_line = self.command_line[0].split('E', maxsplit=1)
            if( self.extruder_line[0] ): #se tiver comando pra exturosa
                return f'{self.command_line[0]}-{self.command_line[1]}\n'
            else:
                return f'{self.command_line[0]}{self.command_line[1]}\n'

def main():
    import sys
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Entre com um valor inteiro positivo após o nome do programa, exemplo: 'python RecursiveFibonacci 1' ")
        return
    user_value = sys.argv[1]    
    user_inverted_file = InvertGCode(user_value)
    user_inverted_file.invert_file(user_value)
    print('Passou')

if __name__ == "__main__": 
    main()  