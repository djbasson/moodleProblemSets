from random import random
from lxml import etree
from lxml.etree import CDATA

##################################################
#### Change these names to whatever you like #####
#### Note: Moodle seems to be case sensitive #####
#### when it comes to problem category.      #####
##################################################

nameOfProblemCategory = "Compound Interest "
problemID = "Compound Interest Calculate Final (CLOZE) "
fileName = "compoundFinalCloze.xml"
numberOfProblems = 8

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
def variable(varName, minimum, maximum):
	var = etree.Element("variable", name=varName)
	minElt = etree.SubElement(var, "min")
	minElt.text = str(minimum)
	maxElt = etree.SubElement(var, "max")
	maxElt.text = str(maximum)
	return var

## This gives the text for an answer to a CLOZE question ##
## I have forced this to be NUMERICAL, since that is     ##
## what this program is for, but if you have need for    ##
## different types, you could add a question_type        ##
## argument for this function.                           ##
def clozeAnswerElement(marks, answer, tolerance):
	# At first I added spaces, but it seems Moodle doesn't
	# want any spaces in the output of this function.
	out = "{" + str(marks) + ":NUMERICAL:="
	out = out + str(answer) + ":"
	out = out + str(tolerance) + "}"
	return out

def clozeQuestion(problemNumber):
	question = etree.SubElement(quiz, "question", type="cloze")
	name = etree.SubElement(question, "name")
	txt = etree.SubElement(name, "text")
	txt.text = problemID + str(problemNumber)
	questionText = etree.SubElement(question, "questiontext", format="html")
	txt = etree.SubElement(questionText, "text")
	cdatadiv = etree.Element("div")

	#############################################################################
	## The following lines determine the values that are used in the question: ##
	#############################################################################

	amount = 1000*int(5*random()+1) # A random multiple of 1000 between 1000 and 5000.
	interest = int(13*random()+4) # Random integer between 4 and 16.
	years = 2 + int(4*random()) # Random integer between 2 and 5

	#########################################################################
	## The following lines create the text for the question:               ##
	#########################################################################

	par = etree.SubElement(cdatadiv, "p")
	par.text = "If I invest R" + str(amount) + " in a fund that receives "
	par.text = par.text + str(interest) + " percent interest per year, "
	par.text = par.text + "compounded monthly, "
	par.text = par.text + "calculate the value of the account after "
	par.text = par.text + str(years) + " years."

	################################################################################
	## Lastly, these lines create the Cloze answer boxes with the data they need: ##
	################################################################################

	par = etree.SubElement(cdatadiv, "p")  # Start a new paragraph
	par.text = clozeAnswerElement(1, amount*(1+interest/1200)**(12*years), 0.02)

	########################################################################

	contentStr = etree.tostring(cdatadiv, pretty_print=True)
	txt.text = CDATA(contentStr)
	quiz.append(etree.Comment("New question."))

	return

quiz = etree.Element("quiz")
createPreamble()
for i in range(numberOfProblems):
	clozeQuestion(i)
tree = etree.ElementTree(quiz)
tree.write(fileName, xml_declaration=True, encoding = 'UTF-8', pretty_print=True)


# Checks if the vectors that form the elements of the list L are linearly independent.
