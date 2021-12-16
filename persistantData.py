import pickle
import tkinter as tk

class Person:
    def __init__(self, name):
        self.name = name
        # self.age = age

    def newPerson(self, userNameInput):
        with open('people_data.pkl', 'wb') as output:
            person = Person(userNameInput)
            pickle.dump(person, output, pickle.HIGHEST_PROTOCOL)


# with open('people_data.pkl', 'wb') as output:
#     person1 = Person('Jon', 40)
#     pickle.dump(person1, output, pickle.HIGHEST_PROTOCOL)

#     person2 = Person('John', 41)
#     pickle.dump(person2, output, pickle.HIGHEST_PROTOCOL)

# del person1
# del person2

        with open('people_data.pkl', 'rb') as input: 
            person1 = pickle.load(input)
            print(person1.name)
            print(person1.age)

            person2 = pickle.load(input)
            print(person2.name)
            print(person2.age)

def main(event):
    a = Person.newPerson(entry.get())
    print(entry.get())

window = tk.Tk()
tk.Label(window, text="Your name?:").pack()
entry = tk.Entry(window)
entry.bind("<Return>", main)
entry.pack()
result = tk.Label(window).pack()
window.mainloop()
