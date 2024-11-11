

# # # print("hello")

# # # def print_hello():
# # #     print("hello")

# # # print_hello() 
# # # print_hello() 
# # # print_hello() 

# # # # print("hello",end="$")

# # # cities=["delhi","b","c","d"]
# # # heroes=["z","x","v","n","g"]

# # # def print_len(list):
# # #     print(len(list))

# # # print_len(cities)
# # # print_len(heroes)

# # # # def print_list(list):
# # # #     for item in list:
# # # #         print(item,end=" ")

# # # # print_list(heroes)
                       
# # #                         ##RECUSION:
# # # # def show(n):
# # # #     if (n==0):   #BASE CASE
# # # #         return 
# # # #     print(n)
# # # #     show(n-1)

# # # # show(5)

# # # ## factorial by recusion :
# # # # def fact(n):
# # # #     if (n==0 or n==1):  #BASE CASE
# # # #         return 1
# # # #     else:
# # # #         return n * fact(n-1)
    
# # # # print(fact(5))

# # # # #write a recursive function to print all element in a list:
# # # # def print_list(list,idx=0):
# # # #     if(idx==len(list)):
# # # #         return
# # # #     print(list[idx])
# # # #     print_list(list,idx+1)

# # # # fruits=["mango","a" ,"b" ,"c"]
# # # # print_list(fruits)


# # def pattern(n):

# #     if(n==0):
# #         return
# #     print("*" * n)
# #     pattern(n-1)

# # pattern(3)

# # # remove an from the list:  
# # def rem(l, word):
# #     n = []
# #     for item in l:
# #         if not(item ==word):
# #             n.append(item.strip(word))
# #     return n
# # l= ["Harry","Rohan", "Shubham","an"]
# # print(rem(l,"an"))


# # def mult(n):
# #     for i in range(1,11):
# #         print(f"{n} X {i} = { n*i }")

# # mult(5)
#                 #  OOPS :
# # class Employee:
# #     language="Py" # This is a class attribute
# #     salary=1200000

# # harry=Employee()

# # harry.name = "Harry" # This is an instance attribute 
# # print(harry.name, harry.language, harry.salary)

# # rohan= Employee()
# # rohan.name = "Rohan Roro Robinson"

# # print(rohan.name, rohan.salary, rohan.language)

# # Here name is instance attribute and salary and language attributes as they directly belong to the class
                    

# # # #                         #FILE :
# # # # #TYPE OF FILE:
# # # ## 1.TEXT FILES : .txt, .docx , .log etc.  ---> for text
# # # ## 2.BINARY FILES: .mp4, .mov, .png ,.jpeg etc ---> for vedioes

# # def goodDay (name, ending):
# #     print("Good Day,"+name)
# #     print(ending)
# #     return "ok"

# # a=goodDay("Harry", "Thank you")
# # print(a)

























































# #                         #OOPS:
# # import tkinter as tk
# from tkinter import messagebox

# # Questions for different age groups
# age_group_questions = {
#     "Primary": [
#         {
#             "question": "What is 2 + 2?",
#             "options": ["3", "4", "5", "6"],
#             "answer": "4"
#         },
#         {
#             "question": "What color is the sky?",
#             "options": ["Green", "Blue", "Red", "Yellow"],
#             "answer": "Blue"
#         }
#     ],
#     "Secondary": [
#         {
#             "question": "What is the chemical symbol for water?",
#             "options": ["H2O", "O2", "CO2", "HO"],
#             "answer": "H2O"
#         },
#         {
#             "question": "What is 15 * 4?",
#             "options": ["60", "45", "70", "50"],
#             "answer": "60"
#         }
#     ],
#     "Senior Secondary": [
#         {
#             "question": "What is the unit of electric current?",
#             "options": ["Ohm", "Ampere", "Volt", "Watt"],
#             "answer": "Ampere"
#         },
#         {
#             "question": "Which part of the cell is known as the powerhouse?",
#             "options": ["Nucleus", "Ribosome", "Mitochondria", "Endoplasmic Reticulum"],
#             "answer": "Mitochondria"
#         }
#     ]
# }

# class QuizApp:
#     def _init_(self, root):
#         self.root = root
#         self.root.title("Quiz App")
#         self.root.geometry("500x400")
        
#         self.question_index = 0
#         self.score = 0
#         self.selected_age_group = None

#         self.display_age_group_selection()
    
#     def display_age_group_selection(self):
#         # Clear previous widgets
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Display age group selection buttons
#         age_label = tk.Label(self.root, text="Select Age Group:", font=("Arial", 16))
#         age_label.pack(pady=20)

#         for age_group in age_group_questions.keys():
#             age_button = tk.Button(self.root, text=age_group, font=("Arial", 14), command=lambda ag=age_group: self.start_quiz(ag))
#             age_button.pack(pady=10)

#     def start_quiz(self, age_group):
#         self.selected_age_group = age_group
#         self.question_index = 0
#         self.score = 0
#         self.display_question()

#     def display_question(self):
#         # Clear previous widgets
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Get the current question and options for the selected age group
#         question_data = age_group_questions[self.selected_age_group][self.question_index]
#         question_text = question_data["question"]
#         options = question_data["options"]

#         # Display the question
#         question_label = tk.Label(self.root, text=question_text, font=("Arial", 14), wraplength=450)
#         question_label.pack(pady=20)
        
#         # Display the options as radio buttons
#         self.answer_var = tk.StringVar()
#         for option in options:
#             option_radio = tk.Radiobutton(
#                 self.root, text=option, variable=self.answer_var, value=option, font=("Arial", 12)
#             )
#             option_radio.pack(anchor="w")
        
#         # Next button
#         next_button = tk.Button(self.root, text="Next", command=self.check_answer)
#         next_button.pack(pady=20)
    
#     def check_answer(self):
#         selected_answer = self.answer_var.get()
#         correct_answer = age_group_questions[self.selected_age_group][self.question_index]["answer"]

#         # Check if the answer is correct
#         if selected_answer == correct_answer:
#             self.score += 1
#             messagebox.showinfo("Correct!", "That's the correct answer!")
#         else:
#             messagebox.showerror("Incorrect", f"The correct answer was: {correct_answer}")
        
#         # Move to the next question
#         self.question_index += 1
#         if self.question_index < len(age_group_questions[self.selected_age_group]):
#             self.display_question()
#         else:
#             self.show_final_score()

#     def show_final_score(self):
#         # Display the final score
#         for widget in self.root.winfo_children():
#             widget.destroy()
        
#         final_score_label = tk.Label(
#             self.root, text=f"Quiz Complete! Your score: {self.score}/{len(age_group_questions[self.selected_age_group])}", font=("Arial", 16)
#         )
#         final_score_label.pack(pady=50)
        
#         # Restart and Exit buttons
#         restart_button = tk.Button(self.root, text="Restart", command=self.display_age_group_selection)
#         restart_button.pack(pady=10)
        
#         quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
#         quit_button.pack(pady=10)

# # Run the app
# root = tk.Tk()
# app = QuizApp(root)
# root.mainloop()


