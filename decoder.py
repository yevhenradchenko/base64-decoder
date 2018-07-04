from tkinter import *
import json
import base64


def select_all(event):
    text_field_1.tag_add(SEL, '1.0', END)
    text_field_1.mark_set(INSERT, '1.0')
    text_field_1.see(INSERT)

    text_field_2.tag_add(SEL, '1.0', END)
    text_field_2.mark_set(INSERT, '1.0')
    text_field_2.see(INSERT)

    return 'break'


def get_decode_data():
    encode_data = text_field_1.get('1.0', END)
    decode_data = base64.b64decode(encode_data).decode('UTF-8')
    parsed = json.loads(decode_data)
    text_field_2.insert('1.0', json.dumps(parsed, indent=4, sort_keys=True), END)


root = Tk()

root.title('SSL / Base64 to JSON decoder')

frame = Frame(root)

label_1 = Label(root, text='Enter SSL / Base64 format data: ')
text_field_1 = Text(root, height=30, width=90, background='gray89')

label_2 = Label(root, text='JSON view:')
text_field_2 = Text(root, height=30, width=90, background='gray89')

label_1.grid(row=0, column=0)
text_field_1.grid(row=1, column=0, sticky=W)

label_2.grid(row=0, column=1)
text_field_2.grid(row=1, column=1, sticky=E)

# checkbox = Checkbutton(root, text='Save to JSON file')
# checkbox.grid(columnspan=2)

decodeButton = Button(root, text='Decode', command=get_decode_data)
decodeButton.grid(columnspan=2)

text_field_1.bind('<Control-Key-a>', select_all)
text_field_1.bind('<Control-Key-A>', select_all)
text_field_1.bind('<Command-Key-a>', select_all)
text_field_1.bind('<Command-Key-A>', select_all)

text_field_2.bind('<Control-Key-a>', select_all)
text_field_2.bind('<Control-Key-A>', select_all)
text_field_2.bind('<Command-Key-a>', select_all)
text_field_2.bind('<Command-Key-A>', select_all)

frame.grid()
root.mainloop()

