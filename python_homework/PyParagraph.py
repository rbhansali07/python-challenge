import os
import re

file_path = os.path.join("Resources", "paragraph_1.txt")
with open (file_path, "r") as myfile:
        paragraph=myfile.read()
        #repalce new line to form one paragraph
        paragraph = paragraph.replace('\n', " ")
        #create a list of words
        word = paragraph.split(" ") 
        word_count = len(word)
        ltr_count = 0
        #count letters by looping over all words to skip white spaces
        for x in range(len(word)):
            ltr_count += len(word[x])
        #use regular expression to splie paragraph by finding . or ? or !
        sentence = re.split("(?<=[.!?]) +", str(paragraph))
        sentence_count = len(sentence)
        avg_sent_lth = round(word_count/sentence_count,1)
        avg_ltr_cnt = round(ltr_count/word_count,1)
output = []
output.append("Paragraph Analysis")
output.append("-----------------")
output.append(f'Approximate Word Count: {word_count}')
output.append(f'Approximate Sentence Count: {sentence_count}')
output.append(f'Average Letter Count: {avg_ltr_cnt}')
output.append(f'Average Sentence Length: {avg_sent_lth}')
output = '\n'.join(output)
print(output)
with open('Output/PyParagraph_output.txt', 'w') as txtfile:
    txtfile.write(str(output))
             
