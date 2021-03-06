import time as t
import datetime as dt

class question:
    """questions class containing start and end time with points/mins counted.

    >>> import datetime as dt
    >>> a = dt.datetime(2018, 5, 8, 19, 0, 0, 0)
    >>> b = dt.datetime(2018, 5, 8, 19, 15, 0, 0)
    >>> c = dt.datetime(2018, 5, 8, 19, 0, 30, 0)
    >>> hard = question('spring', 2018, 1, 8)
    >>> hard.start(a)
    >>> hard.end(b)
    >>> hard.start_time
    datetime.datetime(2018, 5, 8, 19, 0)
    >>> delta = hard.span_mins
    >>> delta
    15
    >>> hard.point_per_min
    0.5333333333333333
    """
    def __init__(self, semester, year, number, points):
        assert all(map(lambda x: type(x) is int, [year, number, points])), 'Year, Number, Points SHOULD be int'
        assert type(semester) is str
        self.semester = semester.upper()
        self.year = int(year)
        self.number = number
        self.points = points
        self.finished_status = False
        self.start_time = "Not yet! Be quick!"
        self.end_time = "Haven't started."

    def start(self, start_time=dt.datetime.now()):
        self.start_time = start_time

    def end(self, end_time=dt.datetime.now()):
        self.end_time = end_time
        self.finished_status = True

    @property
    def span_mins(self):
        if not self.finished_status:
            return "Not Finished"
        delta = self.end_time - self.start_time
        return int(delta.total_seconds()/60)

    @property
    def point_per_min(self):
        if not self.is_finished():
            return "Not Finished"
        if self.span_mins == 0:
            return self.points
        return self.points / self.span_mins

    def is_finished(self):
        return self.finished_status

    def __repr__(self):
        return '{0} {1}: Question No. {2}'.format(self.semester, self.year, self.number)


class Exam:
    """ Exam class for a particular exam.
    >>> q1 = question('spring', 2017, 1, 10)
    >>> q2 = question('spring', 2017, 2, 10)
    >>> q3 = question('spring', 2017, 3, 10)
    >>> exam = make_exam(q1, q2, q3)
    >>> spring_2017 = Exam('spring', 2017, 3, exam)
    >>> spring_2017
    spring 2017. Progress: total 3 questions, 0 finished, 3 to go!
    >>> spring_2017.questions
    {1: spring 2017: Question No. 1, 2: spring 2017: Question No. 2, 3: spring 2017: Question No. 3}
    >>> spring_2017.questions_left
    {1: spring 2017: Question No. 1, 2: spring 2017: Question No. 2, 3: spring 2017: Question No. 3}
    >>> spring_2017.questions_finished
    {}
    >>> import datetime as dt
    >>> start_time_q1 = dt.datetime(2018, 5, 8, 19, 0, 0, 0)
    >>> end_time_q1 = dt.datetime(2018, 5, 8, 19, 15, 0, 0)
    >>> spring_2017.start(1, start_time_q1)
    >>> spring_2017.questions_finished
    {}
    >>> spring_2017.end(1, end_time_q1)
    >>> spring_2017.questions_finished
    {1: spring 2017: Question No. 1}
    >>> spring_2017.questions_left
    {2: spring 2017: Question No. 2, 3: spring 2017: Question No. 3}
    >>> spring_2017.is_exam_finished()
    False
    >>> start_time_q2 = dt.datetime(2018, 5, 8, 19, 15, 0, 0)
    >>> end_time_q2 = dt.datetime(2018, 5, 8, 19, 30, 0, 0)
    >>> spring_2017.start(2, start_time_q2)
    >>> spring_2017.end(2, end_time_q2)
    >>> start_time_q3 = dt.datetime(2018, 5, 8, 19, 30, 0, 0)
    >>> end_time_q3 = dt.datetime(2018, 5, 8, 19, 45, 0, 0)
    >>> spring_2017.start(3, start_time_q3)
    >>> spring_2017.end(3, end_time_q3)
    >>> spring_2017.is_exam_finished()
    True
    """

    def __init__(self, semester, year, total_questions_number, make_exam=False):
        assert type(year) is int, 'Year SHOULD be int'
        assert type(semester) is str, 'Semester should be str'
        self.year = year
        self.semester = semester.upper()
        self.questions = {}
        if make_exam:
            self.questions.update(make_exam)
        else:
            for i in range(total_questions_number):
                p = input("Points of No. {0} question: ".format(i+1))
                while p is '':
                    p = input('Wrong input.' + '\n' + 'Points of No. {0} question: '.format(i+1))
                question_points = int(p)
                this_question = question(self.semester, self.year, i + 1, question_points)
                self.questions.update({i+1:this_question})
        with open('record.txt', 'a') as f:
            f.write('-'* 40 +' Welcome to CS61A final prep! :D ' + '-'*40 + '\n')
            f.write('###' + ' Initializing {0} {1}.......'.format(self.year, self.semester) + '\n')

    @property
    def questions_finished(self):
        return {i:value for i, value in self.questions.items() if self.questions[i].is_finished()}

    @property
    def questions_left(self):
        """ Return questions that haven't been solved."""
        return {i:value for i, value in self.questions.items() if i not in self.questions_finished}

    def __repr__(self):
        if len(self.questions_left) == 0:
            return '{0} {1}. Progress: total {2} questions, All finished!'.format(self.semester, self.year, len(self.questions))
        return '{0} {1}. Progress: total {2} questions, {3} finished, {4} to go!'.format(self.semester, self.year, len(self.questions), len(self.questions_finished), len(self.questions_left))

    def start(self, number, start_time=dt.datetime.now()):
        question.start(self.questions[number], start_time)
        with open('record.txt','a') as f:
            f.write('\n'*2 + str(self.questions[number]) + '\n' + 'Start @ ' + start_time.strftime('%Y-%b-%d %H:%M') + '\n')

    def end(self, number, end_time=dt.datetime.now()):
        #??self.questions[number].end(end_time)
        question.end(self.questions[number], end_time)
        with open('record.txt','a') as f:
            f.write('End   @ ' + end_time.strftime('%Y-%b-%d %H:%M') + '\n' + 'Time_spent: ' + str(self.span_mins(number)) + ' mins' + '\n' + 'Points earned per mins: ' + str(self.point_per_min(number)) + ' points/min ' + '\n')
            f.write(str(self) + '\n'*2 )
            if self.is_exam_finished():
                f.write('Congrates, you have finished this exam!' + '\n' + 'The overall performance is as follows: ' + '\n'*2)
                self.overall_eval(f)

    def span_mins(self, number):
        return self.questions[number].span_mins

    def point_per_min(self, number):
        return self.questions[number].point_per_min


    def is_question_finished(self, number):
        return self.questions[number].is_finished()

    def is_exam_finished(self):
        return all([self.is_question_finished(index) for index, value in self.questions.items()])

    def overall_hours(self, want_hours=True):
        time_mins = sum([self.span_mins(i) for i in self.questions])
        if want_hours:
            return time_mins / 60
        return time_mins

    def overall_ppm(self):
        if self.questions is {}:
            return "Sorry, no question here."
        return sum([self.point_per_min(i) for i in self.questions]) / len(self.questions)

    def estimate_score(self, time_amount=180):
        if self.questions is {}:
            return "Sorry, No question here."
        return self.overall_ppm() * time_amount

    def overall_eval(self, f):
        if not self.is_exam_finished():
            f.write('Warning, you haven\'t finish your mock exam.' + '\n')
        if self.questions is {}:
            f.write("Sorry, there's no question here!")
        f.write('Overall Performance' + '\n')
        f.write('Time span: ' + str(self.overall_hours()) + '\n')
        f.write('Point per mins: ' + str(self.overall_ppm()) + '\n')
        f.write('Estimate final: ' + str(self.estimate_score()) + '\n'*2)


# Make exam for test.
def make_exam(*args):
    questions = {}
    for i, arg in enumerate([*args]):
        assert isinstance(arg, question), 'input of make_exam must be questions'
        questions.update({i+1:arg})
    return questions


