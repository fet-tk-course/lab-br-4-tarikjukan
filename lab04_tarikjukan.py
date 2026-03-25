#Ime: Tarik Jukan
#Datum: 25.03.2026
# Lab 4 --- Python za FastAPI

student = {"ime":"Tarik","godina": 3, "email": "tarik.jukan@untz.ba", "pol": "musko"}

print (student)
print (student["ime"])
student["aktivan"] = True

studenti = [
{"ime": "Amina", "godina": 3, "pol": "zensko", "aktivan": True},
{"ime": "Emir", "godina": 2, "pol": "musko", "aktivan": False},
{"ime": "Tarik", "godina": 3, "pol": "musko", "aktivan": True},
{"ime": "Lejla", "godina": 1, "pol": "zensko", "aktivan": False}
]

def get_student_info(name: str, year: int, email: str) -> dict:
    return {
        "name": name,
        "year": year,
        "email": email,
        "greeting": f"Zdravo {name}, vi ste {year} godina studija"
    }

info = get_student_info("Amina", 3, "amina@email.com")
print(info)

def ispisi_poziv(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam: {func.__name__}")
        # pozovite originalnu funkciju i vratite rezultat
        return func(*args, **kwargs)
    return wrapper

@ispisi_poziv
def info_o_studentu(ime: str, godina: int) -> dict:
    return {
        "ime": ime,
        "godina": godina,
        "poruka": f"Student {ime} je na {godina}. godini studija."
    }

rezultat = info_o_studentu("Ana", 3)
print(rezultat)

class Course:
    def __init__(self, name: str, code: str, credits: int, professor: str):
        self.name = name
        self.code = code
        self.credits = credits
        self.professor = professor

    def description(self):
        return f"{self.code} - {self.name} ({self.credits} kredita), profesor: {self.professor}"

# Kreiranje instanci i ispis opisa
course1 = Course("Razvoj telekomunikacijske programske podrške", "TK207", 6, "dr. Marko Marković")
course2 = Course("Osnove programiranja", "TK101", 7, "dr. Ana Anić")

print(course1.description())
print(course2.description())

students = [
    {"name": "Tarik", "year": 3, "email": "tarik.jukan@untz.ba"},
    {"name": "Amina", "year": 3, "email": "amina@untz.ba"},
    {"name": "Emir", "year": 2, "email": "emir@untz.ba"},
    {"name": "Lejla", "year": 1, "email": "lejla@untz.ba"}
]

def filter_by_year(students: list, year: int) -> list:
    return [student for student in students if student["year"] == year]

def print_registry(students: list) -> None:
    for student in students:
        print(f"{student['name']}, email: {student['email']}")

filter_by_year_result = filter_by_year(students, 3)
print("Studenti na 3. godini:")

print_registry(filter_by_year_result)

def sort_by_year(students: list) -> list:
    return sorted(students, key=lambda x: x["year"])

sorted_by_year_result = sort_by_year(students)
print("Studenti sortirani po godini:")
print_registry(sorted_by_year_result)