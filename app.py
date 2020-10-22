print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel after the examinations?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling. Life is good!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("Get some sleep")
      counter += 1
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("Relax after the stressful examinations")
      counter += 1
    if each_word == "dead tired":
      feelings_list.append("dead tired")
      encouragement_list.append("Just find something fun to do")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("talk to your friends")
      counter += 1  
   if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("calm down.  it is over and there is no point crying over spilt milk")
      counter += 1      
   if each_word == "annoyed":
      feelings_list.append("annoyed")
      encouragement_list.append("stop what you are doing and take a deep breath")
      counter += 1  
   if each_word == "proud":
      feelings_list.append("proud")
      encouragement_list.append("good job! keep up the good work!")
      counter += 1   
   if each_word == "awkward":
      feelings_list.append("awkward")
      encouragement_list.append("it's alright! everyone has their moments, maybe you can try a different approach?")
      counter += 1  
      
    if counter == 0:

      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember to "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
