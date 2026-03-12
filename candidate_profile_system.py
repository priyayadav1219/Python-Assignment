class PersonalInfo:
    def __init__(self, name, dob, contact, email):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email

    def display_personal(self):
        print("Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Contact Number:", self.contact)
        print("Email:", self.email)


class Education(PersonalInfo):
    def __init__(self, name, dob, contact, email, degree, university, year, cgpa):
        PersonalInfo.__init__(self,name, dob, contact, email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("Degree:", self.degree)
        print("University:", self.university)
        print("Year of Graduation:", self.year)
        print("CGPA:", self.cgpa)


class Experience(Education):
    def __init__(self, name, dob, contact, email, degree, university, year, cgpa,
                 company, role, years_exp, skills):
        Education.__init__(self,name, dob, contact, email, degree, university, year, cgpa)
        self.company = company
        self.role = role
        self.years_exp = years_exp
        self.skills = skills

    def display_experience(self):
        print("Company Name:", self.company)
        print("Job Role:", self.role)
        print("Years of Experience:", self.years_exp)
        print("Skills:", self.skills)


class CandidateProfile(Experience):
    def display_profile(self):
        print("\n------ Candidate Profile -----")
        self.display_personal()
        print("\n-----Education Details----")
        self.display_education()
        print("\n----Work Experience----")
        self.display_experience()

    def check_eligibility(self):
        if self.years_exp > 5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")


# Candidate 1
c1 = CandidateProfile(
    "Nani", "05-06-1999", "8765567899", "nani05@gmail.com",
    "B.Tech", "Gitam University", 2018, 9.2,
    "Infosys", "Software Engineer", 6,
    "Python, Java"
)

# Candidate 2
c2 = CandidateProfile(
    "Lohith", "03-12-1999", "7656789874", "lohith35@gmail.com",
    "B.Sc Computer Science", "Delhi University", 2021, 8.9,
    "TCS", "Junior Developer", 2,
    "Python, SQL"
)

# Display Profiles
c1.display_profile()
c1.check_eligibility()

c2.display_profile()
c2.check_eligibility()
