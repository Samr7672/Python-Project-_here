import customtkinter as ctk

class tax_calculator:

 def __init__(self):
  
  self.window=ctk.CTk()
  self.window.title("Tax Calculator")
  self.window.geometry("280x200")
  self.window.resizable(False,False)

  self.padding={'padx':20,"pady":10}

  #income
  self.income_label=ctk.CTkLabel(self.window, text="income")
  self.income_label.grid(row=0,column=0, **self.padding)
  self.income_entry=ctk.CTkEntry(self.window)
  self.income_entry.grid(row=0,column=0, **self.padding)

# percent
  self.percent_label=ctk.CTkLabel(self.window, text="Percent")
  self.percent_label_label.grid(row=1,column=0, **self.padding)
  self.percent_entry=ctk.CTkEntry(self.window)
  self.percent_entry.grid(row=0,column=0, **self.padding)

# Tax
  self.tax_label=ctk.CTkLabel(self.window, text="Tax")
  self.tax_label.grid(row=2,column=0, **self.padding)
  self.tax_entry=ctk.CTkEntry(self.window)
  self.tax_entry.insert(0,'0')
  self.tax_entry.grid(row=0,column=0, **self.padding)
 # calculate
  self.income_label=ctk.CTkLabel(self.window, text="Calculate",command=self.calculate_tax)
  self.income_label.grid(row=3,column=1, **self.padding)
 
def calculate_tax(self):
 try:
  income=float(self.income_entry.get())
  percent=float(self.percent_entry.get())
  self.update_entry(f'${income*(percent/100):,2f}')
 except ValueError:
  self.update_entry("invalid Inputs")

def update_entry(self,text):
 self.tax_entry.delete(0,ctk.END)
 self.tax_entry.insert(0,text)

 def run(self):
  self.window.mainloop()

  if __name__=='__main__':
   tc=tax_calculator()
   tc.run()
  