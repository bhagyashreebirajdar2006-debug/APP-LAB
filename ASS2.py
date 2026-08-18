# Decorator to format the medical report
def format_report(func):
    def wrapper(self):
        print("\n===================================")
        print(" MEDICAL REPORT")
        print("===================================")
        func(self)
        print("===================================")
    return wrapper


class MedicalReport:

    template = "General Medical Report"

    # Magic Method
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.diagnosis = ""
        self.format = "Normal"

    # Class Method
    @classmethod
    def set_template(cls, temp):
        cls.template = temp

    def add_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis

    def set_format(self, style):
        self.format = style

    # Decorator Applied
    @format_report
    def display(self):
        print("Template :", MedicalReport.template)
        print("Patient Name :", self.patient_name)
        print("Report Format :", self.format)
        print("\nDiagnosis")
        print("---------")
        print(self.diagnosis)
        print("\nStatus : Medical Report Generated Successfully")

    # Magic Method
    def __str__(self):
        return "Medical Report Object Created"


# Driver Code
patient = input("Enter Patient Name: ")
template = input("Enter Report Template: ")
style = input("Enter Report Format: ")
diagnosis = input("Enter Diagnosis: ")

m1 = MedicalReport(patient)

MedicalReport.set_template(template)
m1.set_format(style)
m1.add_diagnosis(diagnosis)

print(m1)
m1.display()
