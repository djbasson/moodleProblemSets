# Moodle Problem Sets

The two programs listed here contain Python code to create problems for a Moodle problem bank. The questions contain the same text, but the values in the questions are assigned randomly, thereby creating the possibility that students get "randomized" questions.

For now, they are meant only to deal with questions where randomness comes from choosing different values and where the answer is a number or series of numbers. For that reason the only questions types that are generated are the Algebra question type and the Cloze question type with numerical answers. In cases where the answer consists of one number or function, I recommend using the algebra question type and if the answer consists of various numbers (e.g. specifying the three coordinates of a vector), I recommend the Cloze question type. Both have some disadvantages, though.

## How to use the files

In both files, there are a few variables defined at the top that you can customize. They are
* nameOfProblemCategory : This is the category where Moodle will place these questions. You can incorporate subcategories like "/Category/Subcategory", or you could reorganise your categories in Moodle once everything is there. Note: It seems that Moodle is case sensitive and will create different categories for "category" and "Category"
* problemID : The name of the problem as it appears in the problem bank. A number will be appended to this string so that problems have different IDs in Moodle. Note: It seems that Moodle doesn't have a problem with multiple problems having the same ID, so this is mostly for the convenience of the instructor to easily find questions to troubleshoot or edit individually.
* fileName : This is the file in which the xml will be written. This is the file you need to import to Moodle to create the problem bank. This can be anything and is really just an intermediate step in the process. If you wish you can keep these files together in a file somewhere.
* numberOfProblems : How many random problems should the code generate. I recommend starting with 10 for debugging purposes and later going up to 200 (or approximately the class size if it is smaller than that).

### Algebra question type

Use the file [createXMLforAlgerbaType.py](https://github.com/djbasson/moodleProblemSets/blob/master/createXMLforAlgebraType.py). There are only three places you should look to change. The first is where the four variables mentioned above are defined. The second is in the function algebraQuestionText(). This functions tells Moodle what to write as the question text that students see. You may need to change the number of arguments in the function and in the places where the function is called. (Sorry, there is probably a clean solution for this, but I am not a professional programmer.) And the third is the function algebraQuestion() below the first comment block (in the 30 July 2020 version it is from lines 84 to 90). This is the code used to generate the values that are used in the question and to compute the correct answer. 

In this question students can answer with functions, but can also answer simply with a decimal number of fraction (fractions are not possible in Cloze questions - there they have to be decimal). This makes it a good candidate for something like asking derivatives of functions.

### Cloze question type

Use the file [createXMLforClozeType.py](https://github.com/djbasson/moodleProblemSets/blob/master/createXMLforClozeType.py). As with the algebra question type, change the four variables at the top to any values you want. Then, in the function clozeQuestion(), there are three comment boxes. You need to change the code below each of them to what you want. Unfortunately at this point, the function clozeAnswerElement() only allows one answer. 

In general cloze elements could accept alternative answers for partial credit or to give directed feedback to common mistakes. This is not implemented, but is possible and maybe even not so hard. The challenge is that for the type of questions I envisioned, a wrong answer will be a specific combination of answers to all the cloze questions on a page, but this cannot be detected by Moodle, since these question behave independently.

The main benefit is that if an answer needs to specify more than one number, then the Cloze question type can handle it.

## How to upload your xml file to Moodle

On the top right of screen, click the gear (settings) button. In the dropdown, select More..., then close to the bottom of the page, click Question Bank. At the top there will be four tabs, the third of which is Import. Click on it, select Moodle XML Format and upload your file, either by clicking Choose a file... and browsing for it, or by simply dragging it over from a window (this is what I do). Click the Import button at the bottom and if your code is correct the problems should populate the following screen.

## Extra tips

* Save the final version of the code you use to create the problems and create a separate copy for the next problem set. This way if you want to update your problems, you have a final version as a starting point. You or your students may discover a mistake or you may realise common errors that students make and add an alternative answer with directed feedback. (Feedback and alternative answers are not yet implemented in the Cloze question type version.)
* Always test your code. First create a file of 8 or 10 problems and work some of them out by hand to check whether your code gives Moodle the correct answer.
* Do not use more than 200 problems in a category. At first, I created a loop that would run through all possibilities for a problem, but this created categories with thousands of problems, creating an unnecessarily large problem bank. In a bank of 200 problems very few students will get the same question and the ones who do are unlikely to be in contact.

## Further work

If you want to suggest improvements, additions or further examples, send me an e-mail. My Stellenbosch username is djbasson. 

Better yet, clone the repository, add them and send me a pull request!
