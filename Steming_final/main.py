


def stemmer(urdu_file,result_file):

    while (1):
        word = urdu_file.readline()
        word = word.replace(" ", "")  # Replace white spaces(" ") with this ("")
        word = word.strip()  # Remove white spaces from start and end of the word

        # ---Check end of File (if the length of word is zero Its mean there is no word read and it indicates the end of file)-----
        word_length = len(word)
        if (word_length==0):
            break
        # -----------------------------------END------------------------------------

        print("Word Read for stemming:", word)
        if (len(word) <= 3):
            print("Already Stem Word")
            print("------------------------------------------")

        # print("------------------------------------------")

        check=prefix_check(word,result_file)
        if(check!=1):
            print("No Prefix rule defined:")



    urdu_file.close()







def prefix_check(word,result_file):


    prefix_list = open("Prefix List.txt", "r", encoding="UTF-8")
    prefix = prefix_list.readline()
    prefix = prefix.replace(" ", "")
    prefix=prefix.strip()
    count = 0
    matched_prefix=" "

    while(len(prefix)!=0):

      for i in range(len(prefix)):
            if (prefix[i]==word[i]):
                count += 1
                matched_prefix = matched_prefix + word[i]
            else:
                count = 0
                matched_prefix = " "
                break




      if(count>0):
          # print("------------------------------------------")
          # print("Matched letters: ", count)
          print("Matched_prefix:", matched_prefix)
          result_file.write(matched_prefix + "\t")

          word_without_prefix = " "
          for i in range(count, len(word)):
              word_without_prefix = word_without_prefix + word[i]

          print("Word without prefix:", word_without_prefix)
          result_file.write(word_without_prefix+"\n")
          suffix_check(reverse_without_prefix_word(word_without_prefix),result_file)
          return 1
          break
      else:
           prefix = prefix_list.readline()
           prefix = prefix.strip()
           prefix = prefix.replace(" ", "")



def suffix_check(word,result_file):
    prefix_list = open("Suffix_List.txt", "r", encoding="UTF-8")
    prefix = prefix_list.readline()
    prefix = prefix.replace(" ", "")
    prefix = prefix.strip()
    prefix=reverse_without_prefix_word(prefix)
    count = 0
    matched_prefix = " "

    while (len(prefix) != 0):
        # print("Length of Prefix:",len(prefix))
        for i in range(len(prefix)):
            if (prefix[i] == word[i]):
                count += 1
                matched_prefix = matched_prefix + word[i]
            else:
                count = 0
                matched_prefix = " "
                break
#
        if (count > 0):
            # print("Matched letters: ", count)
            matched_prefix=reverse_without_prefix_word(matched_prefix)
            print("Matched_Suffix:", matched_prefix)
            # result_file.write(matched_prefix + "\t")

            word_without_prefix = " "
            for i in range(count, len(word)):
                word_without_prefix = word_without_prefix + word[i]


            word_without_prefix=reverse_without_prefix_word(word_without_prefix)
            print("Word without Suffix:", word_without_prefix)
            # result_file.write(word_without_prefix + "\t")

            break

        else:
            prefix = prefix_list.readline()
            prefix = prefix.strip()
            prefix = prefix.replace(" ", "")
            prefix = reverse_without_prefix_word(prefix)
    print("------------------------------------------")

def reverse_without_prefix_word(word_without_prefix):
    reverse_word = ""
    for j in range(len(word_without_prefix), 0, -1):
        reverse_word += word_without_prefix[j - 1]

    # print(reverse_word)
    return reverse_word





def main():
    urdu_file = open("Urdu File(test).txt", "r", encoding="UTF-8")  # Open file in read mode with encoding UTF-8
    result_file = open("Result file.txt", "a", encoding="UTF-8")    # Open file in write mode with encoding UTF-8
    stemmer(urdu_file,result_file)




main()