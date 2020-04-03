
class QuizManager:

    def __init__(self,text):
        self.text=text
        self.yes = None
        self.no = None


q1 = Quiz("하루에 한개이상 SNS에 접속한다 ")
q2 = Quiz("먹는걸 좋아한다")
q3 = Quiz('힙하다는 얘기를 자주듣는다')
q4 = Quiz('q1 yes yes')
q5 = Quiz('q1 yes yes yes')

q1.yes= q2
q1.no=q3
q2.yes = q4
q4.yes = q5

self.start_quiz = q1

current = q1


    def getFirstQuit(self):
        return self.start_quiz

class QuizUI:

    def __init__(self):
        manager = QuizManager()
        

    def playShow(self,quiz):


        if quiz == None:
            print('end')
            return

        answer = input(quiz.text)

        if answer=='y':
            self.playShow(quiz.yes)

        elif answer=='n':

            self.playShow(quiz.no)