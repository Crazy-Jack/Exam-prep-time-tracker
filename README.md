# <h1 align="center">Exam Prep Time Tracker</h1>
<b><p align="center"> FOR exam prep for CS61A at Cal </p></b>
<b>&nbsp;  &nbsp;  &nbsp;  &nbsp;  This is a program to help people keep track of how much time they spent on each question when they prepared an exam. Good Luck to the Finals! :D </b></br>

<p>&nbsp;  &nbsp;  &nbsp;  &nbsp;  Main funtion:</p> 


<ul>
  <li>Use terminal launch the python3 program: python3 -i timer.py</li>
  * `python3 - timer.py`
  <li>Use Exam(semester, year, numbers-of-total-questions) to construct an instance of exam. for example asign it with name `fall_2017`. After hit `enter`, you can provide points for each question. </li>
  ```python
  >>> fall_spring = Exam('fall', 2017, 7) # 7 means there are 7 questions in fall 2017.
  ```
  <li>Use fall_2017.start(question_number) to start a timing for a question.</li>
  ```python
  >>> fall_2017.start(1)
  ```
  <li>Use fall_2017.end(question_number) to end a timing for a question.</li>
  ```python
  >>> fall_2017.end(1)
  ```
  <li>You can see you record in the `record.txt` file in the same folder you launch python file.</li>
  
 
  ![Record file](https://github.com/Crazy-Jack/Exam-prep-time-tracker/blob/master/Screen%20Shot%200030-05-01%20at%2004.49.13.png?raw=true)
  </br>
  <li>Program will calculate your average time and estimated score base on your mean score/mins. </li>
</ul>



