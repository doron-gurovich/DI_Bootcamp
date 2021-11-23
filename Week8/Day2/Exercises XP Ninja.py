# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:16:29 2021

@author: 97250
"""

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    
    def call(self, other_phone):
        result_out = f"OUT: {self.phone_number} calling to {other_phone.phone_number}"
        result_in = f"IN: {self.phone_number} calling to {other_phone.phone_number}"
        
        self.call_history.append(result_out)
        other_phone.call_history.append(result_in)
        
        print("call ongoing:", result_out, "\n")
        
        return True
    
    def show_call_history(self):
        
        print(f"This is a call history of # {self.phone_number}")
        
        if not self.call_history:
            print("call history is empty so far ...")
            return False
        
        for s in self.call_history:
            print(s)
        
        return True

    def send_message(self, other_phone, content):
        result = f"message from {self.phone_number} to {other_phone.phone_number}. \nContent: {content}"
        
        self.messages.append({"To": other_phone.phone_number, "From": self.phone_number, "Content": content})
        other_phone.messages.append({"To": other_phone.phone_number, "From": self.phone_number, "Content": content})
        
        print(result, "\n")
        
        return True

    def show_incomming_messages(self):
        print(f"\nThis is an incomming message history of # {self.phone_number} \n")
        
        if not self.messages:
            print("messages history is empty so far ...")
            return False
        
        str_to_print = ""
        
        for m in self.messages:
            
            if m["To"] == self.phone_number:
                for k, v in m.items():
                    str_to_print = str(k) + ': ' + str(v)
                        
                    m_to_print = ''.join(str_to_print)
                    print(m_to_print)
                        
                    if m != self.messages[-1]:
                        print("\nThe next message:\n")
            
            
    
    def show_outgoing_messages(self):
        print(f"\nThis is an outgoing message history of # {self.phone_number} \n")
        
        if not self.messages:
            print("messages history is empty so far ...")
            return False
        
        str_to_print = ""
        
        for m in self.messages:
            
            if m["From"] == self.phone_number:
                for k, v in m.items():
                    str_to_print = str(k) + ': ' + str(v)
                        
                    m_to_print = ''.join(str_to_print)
                    print(m_to_print)

                    #if m != self.messages[-1]:
                    #    print("\nThe next message:\n")


    def show_messages_from(self):
        print(f"This is a message history of # {self.phone_number} \n")
        
        if not self.messages:
            print("messages history is empty so far ...")
            return False
        
        str_to_print = ""
        
        for m in self.messages:
            for k, v in m.items():
                str_to_print = str(k) + ': ' + str(v)
                
                m_to_print = ''.join(str_to_print)
                print(m_to_print)
            
            if m != self.messages[-1]:
                print("\nThe next message:\n")
            
        return True

ph1 = Phone(1111)
ph2 = Phone(2222)
ph3 = Phone(3333)

ph1.send_message(ph2, "QW asdsd zxzx")
ph2.send_message(ph1, "fine with me")

ph1.show_messages_from()
ph1.show_outgoing_messages()
ph1.show_incomming_messages()