from random import random
from lxml import etree
from lxml.etree import CDATA

##################################################
#### Change these names to whatever you like #####
#### Note: Moodle seems to be case sensitive #####
#### when it comes to problem category.      #####
##################################################

nameOfProblemCategory = "Compound Interest"
problemID = "Compound Interest Calculate Final "
fileName = "compoundFinal.xml"
numberOfProblems = 200

##################################################

## No need to change this ##
def createPreamble():
	quizcategory = etree.SubElement(quiz, "question", type="category")
	category = etree.SubElement(quizcategory, "category")
	categoryText = etree.SubElement(category, "text")
	categoryText.text = '$course$/' + nameOfProblemCategory
	quiz.append(etree.Comment("Questions start here."))
	return

## No need to change this ##
def algebraAnswer(grade, answer, feedback):
	answerElement = etree.Element("answer", fraction=str(grade), format="moodle_auto_format")
	txt = etree.SubElement(answerElement, "text")
	txt.text = str(answer)
	feedbackElement = etree.SubElement(answerElement, "feedback", format="html")
	txt = etree.SubElement(feedbackElement,"text")
	txt.text = feedback
	return answerElement

## No need to change this ##
def variable(varName, minimum, maximum):
	var = etree.Element("variable", name=varName)
	minElt = etree.SubElement(var, "min")
	minElt.text = str(minimum)
	maxElt = etree.SubElement(var, "max")
	maxElt.text = str(maximum)
	return var

def algebraQuestionText(amount, interest,  years):
	divider = etree.Element("div")

	########################################################################
	## Change the next few lines to whatever you want the question to be: ##
	########################################################################

	paragraph = etree.SubElement(divider, "p")
	problemText = "If I invest R" + str(amount) + " in a fund that receives "
	problemText = problemText + str(interest) + " percent interest per year, "
	problemText = problemText + "compounded monthly, "
	problemText = problemText + "calculate the value of the account after "
	problemText = problemText + str(years) + " years."
	paragraph.text =  problemText

	########################################################################

	return divider

def algebraQuestion(problemNumber):
	question = etree.SubElement(quiz, "question", type="algebra")
	name = etree.SubElement(question, "name")
	txt = etree.SubElement(name, "text")
	txt.text = problemID + str(problemNumber)
	questionText = etree.SubElement(question, "questiontext", format="html")
	txt = etree.SubElement(questionText, "text")

	########################################################################
	## At this point you may want to create variables and assign them    ###
	## random values to feed to the function algebraQuestionText()       ###
	## From these variables, you also calculate the correct answer       ###
	## and feed that into algebraAnswer() further down. You may also     ###
	## compute the value of common wrong answers and feed that into an   ###
	## additional algebraAnswer(), but with the first argument equal to  ###
	## 0 (or whatever partial credit) and the third the feedback for     ###
	## that type of mistake.                                             ###
	########################################################################

	amount = 1000*int(5*random()+1) # A random multiple of 1000 between 1000 and 5000.
	interest = int(13*random()+4) # Random integer between 4 and 16.
	years = 2 + int(4*random()) # Random integer between 2 and 5
	contentStr = etree.tostring(
		algebraQuestionText(amount, interest, years),
		pretty_print=True)
	answerToQuestion = amount*(1+interest/1200)**(12*years)
	txt.text = CDATA(contentStr)

	########################################################################
	## In my experience it is best to evaluate using "eval". It uses the ###
	## idea that if two functions are different, then by evaluating them ###
	## at a number of different random inputs, they will likely differ   ###
	## by at least 0.001 in at least one of those inputs.                ###
	########################################################################
	## The tolerance can be set to be more or less tolerant, by making   ###
	## the 0.001 smaller or larger. But, with floating point operations  ###
	## it is not suggested that you make it 0 - that is likely to lead   ###
	## to a lot of false negatives. In my experience 0.001 and at least  ###
	## 3 or as many as 10 work well. If the answer is a number, not a    ###
	## function, then of course 1 check is enough.                       ###
	########################################################################
	## The variables that are evaluated need to be specified. If the     ###
	## answer is a function of x, then specify the variable x, as well   ###
	## as a minimum and maximum value for x. It is important to specify  ###
	## an interval that does not contain a singularity, as equivalent    ###
	## functions may evaluate differently if evaluated close to a        ###
	## singularity. If the answer is a function in more than one         ###
	## variable, then specify each variable and its interval separately. ###
	########################################################################

	compare = etree.SubElement(question,"compareby")
	compare.text = "eval"
	tolerance = etree.SubElement(question,"tolerance")
	tolerance.text = "0.02"
	nchecks = etree.SubElement(question,"nchecks")
	nchecks.text = "5"

	########################################################################
	## Here you need to place your answer using the variables from       ###
	## earlier in the second argument.                                   ###
	########################################################################

	question.append(algebraAnswer(100,answerToQuestion,"Correct!"))

	########################################################################

	question.append(variable("x",0,3))
	quiz.append(etree.Comment("New question."))

	return

quiz = etree.Element("quiz")
createPreamble()
for i in range(numberOfProblems):
	algebraQuestion(i)
tree = etree.ElementTree(quiz)
tree.write(fileName, xml_declaration=True, encoding = 'UTF-8', pretty_print=True)

