# Moodle Problem Sets

The two programs listed here contain Python code to create problems for a Moodle problem bank. The questions contain the same text, but the values in the questions are assigned randomly, thereby creating the possibility that students get "randomized" questions.

For now, they are meant only to deal with questions where randomness comes from choosing different values and where the answer is a number or series of numbers. For that reason the only questions types that are generated are the Algebra question type and the Cloze question type with numerical answers. In cases where the answer consists of one number or function, I recommend using the algebra question type and if the answer consists of various numbers (e.g. specifying the three coordinates of a vector), I recommend the Cloze question type. Both have some disadvantages, though.

## Algebra question type

In this question students can answer with functions, but can also answer simply with a decimal number of fraction (fractions are not possible in Cloze questions - there they have to be decimal). This makes it a good candidate for something like asking derivatives of functions.

## Cloze question type

The main benefit is that if an answer needs to specify more than one number, then the Cloze question type can handle it.
