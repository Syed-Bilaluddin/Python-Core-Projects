import datetime
class NoteClass:
    def __init__(self, id, text, date_time = None):
        self.text = text
        if date_time is None:
            self.date_time = datetime.datetime.now()
        else:
            self.date_time = date_time
        self.id = id
     
notes = []
try:
    with open("notes.txt", "r") as file:
        for f in file:
            data = f.strip().split("|")
            id = data[0].strip()
            note_text = data[1].strip()
            date_time = data[2].strip()
            note = NoteClass(id, note_text, date_time)
            notes.append(note)
except FileNotFoundError:
    pass
while True:
        print("===NOTES APPLICATION===")
        print("1. Add notes")
        print("2. Views Notes")
        print("3. Search Notes")
        print("4. Delete Notes")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                text = input("Enter note text: ")
                print(text)
                new_id = len(notes) + 1
                note = NoteClass(new_id, text)
                notes.append(note)
            case 2:
                for n in notes:
                    print(f"ID: {n.id}, {n.text}, {n.date_time}")       
            case 3:
                search = input("Enter your search keyword: ")
                print(search)
                for n in notes:
                    if search.lower() in n.text.lower():
                        print(f"ID: {n.id}, {n.text}, {n.date_time}")
            case 4:
                deleteID = input("Enter Note ID to delete: ")
                for n in notes:
                    if deleteID == n.id:
                        notes.remove(n)
                        print(f"ID: {n.id}, {n.text}, {n.date_time} deleted.")
                        break
            case 5:
                with open("notes.txt", "w") as file:
                    for n in notes:
                        file.write(f"{n.id} | {n.text} | {n.date_time} \n")
                break