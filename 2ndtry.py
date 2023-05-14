import numbers
import customtkinter
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#def result():
   # label =customtkinter.CTkLabel(root,font=customtkinter.CTkFont('Arial',28), command=formula)
    #label.pack()

#def formula():
    #text=myentry1.get()
    #label =customtkinter.CTkLabel(master=frame,text=[text])
    #label.pack()

def generate_numbers():
        myentry1_1=(1 + int(myentry1.get()))
        numbers = sorted(random.sample(range(1, int(myentry1_1)), int(myentry2.get())))
        result_label.configure(text=" ".join(str(num) for num in numbers))
        

        
        #for num in numbers:
            
            #if num % 2 == 0:
                #result_label.configure(text="Even")
                
            
        #else:
            #result_label.configure(text="Odd")
            
        
    
root = customtkinter.CTk()


root.geometry("500x500")
root.title("Random number generator")
   

label =customtkinter.CTkLabel(root, text="Random Numbers Generator", font =customtkinter.CTkFont('Arial', 28))
label.pack(padx=20, pady=30)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


myentry1 = customtkinter.CTkEntry(master=frame, width=75, justify='center', font=customtkinter.CTkFont('Arial', 20))
label = customtkinter.CTkLabel(master=frame, text="Range", font =customtkinter.CTkFont('Arial',20))
label.pack()
myentry1.pack()

myentry2 = customtkinter.CTkEntry(master=frame, width=75,justify='center', font=customtkinter.CTkFont('Arial', 20))
label = customtkinter.CTkLabel(master=frame, text="Combination", font =customtkinter.CTkFont('Arial',20))
label.pack()
myentry2.pack()

button = customtkinter.CTkButton(master=frame, text="Generate", font=customtkinter.CTkFont('Arial', 30), command=generate_numbers)
button.pack(padx=10, pady=10)

result_label = customtkinter.CTkLabel(master=frame, text="", font =customtkinter.CTkFont('Arial', 40))
result_label.pack(pady=50)

Even_Odd_label= customtkinter.CTkLabel(master=frame, text="", font =customtkinter.CTkFont('Arial', 10))
Even_Odd_label.pack(pady=50)

root.mainloop()