<h1 align="center">Exam Prep Time Tracker</h1>
<b><p align="center"> FOR exam prep for CS61A at Cal </p></b>
<b>&nbsp;  &nbsp;  &nbsp;  &nbsp;  This is a program to help people keep track of how much time they spent on each question when they prepared an exam. For convenience, just download the timer.py to your folder and interact with it in iterpretor. Good Luck to the Finals! :D </b></br>

<p>&nbsp;  &nbsp;  &nbsp;  &nbsp;  Main funtion:</p> 


<ul>
  <li>Use terminal launch the python3 program</li>
  <code>$ python3 - timer.py</code>
  </br>
  
  </br>
  <li>Use Exam(semester, year, numbers-of-total-questions) to construct an instance of exam. for example asign it with name fall_2017. After hit <code>enter</code>, you can provide points for each question. </li>
  <code> >>> fall_spring = Exam('fall', 2017, 7) # 7 means there are 7 questions in fall 2017. </code>
  </br>
  
  </br>
  <li>Use fall_2017.start(question_number) to start a timing for a question.</li>
  <code>>>> fall_2017.start(1)</code>
  </br>
  
  </br>
  <li>Use fall_2017.end(question_number) to end a timing for a question.</li>
  <code>>>> fall_2017.end(1)</code>
  </br>
  
  </br>
  <li>You can see you record in the <code> record.txt </code> file in the same folder you launch python file.</li></br>
  
  ![Record file](https://github.com/Crazy-Jack/Exam-prep-time-tracker/blob/master/Screen%20Shot%200030-05-01%20at%2004.49.13.png?raw=true)
  </br>
  
  </br>
  <li>Program will calculate your average time and estimated score base on your mean score/mins. </li>
</ul>



