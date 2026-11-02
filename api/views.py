from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):
    def get(self,request):
        data={
            "ID":"100",
            "Name":"Rithu Mary Varghese",
            "Professional Title":"Python Backend Developer",
            "Bio":"I’m a BTech Computer Science graduate and a Python Full Stack Developer trainee with a strong interest in building practical and user-friendly web applications. I have experience with Python, Django, MySQL, HTML, CSS, and Git/GitHub. I’m passionate about learning new technologies, improving my skills, and creating solutions that solve real-world problems.",
            "Email ID":"rithumary001@gmail.com",
            "contact":"8891293880",
            "DOB":"9/12/2004",
            "GitHub URL":"https://github.com/rithumary",
            "Linkedln URL":"https://www.linkedin.com/in/rithu-mary-varghese"
        }
        return JsonResponse(data)
class EducationView(View):
    def get(self,request):
        data={
            "ID":100,
            "Institute":"Vidya Academy Of Science and Technology",
            "Degree":"BTech Computer Science",
            "University":"Ktu",
            "Location":"Thrissur",
            "Start Year":2022,
            "End Year":2026,
            "CGPA":7,
            "Description":"I completed my BTech in Computer Science and Engineering, where I developed a strong foundation in programming, computer science concepts, and software development. I am currently enhancing my skills through a Python Full Stack Development course."
        }
        return JsonResponse(data)
class ProjectView(View):
    def get(self,request):
        data=[{
            "id": 1,
            "title": "Dietiense",
            "short_description": "A diet and nutrition management platform.",
            "long_description": "Dietiense is a web application that helps users manage their diet, track healthy food choices, and maintain a better lifestyle.",
            "live_url": "https://dietiense.example.com",
            "github_url": "https://github.com/username/dietiense",
            "image_url": "https://example.com/images/dietiense.png",
            "featured": True},
            {
                "id": 2,
                "title": "MediTrust",
                "short_description": "An intelligent hospital and drug interaction platform.",
                "long_description": "MediTrust is a healthcare platform designed to manage hospital information and provide useful information about possible drug interactions.",
                "live_url": "https://meditrust.example.com",
                "github_url": "https://github.com/username/meditrust",
                "image_url": "https://example.com/images/meditrust.png",
                "featured": True},
                {
                    "id": 3,
                "title": "Student Management System",
                "short_description": "A system for managing student information.",
                "long_description": "Student Management System is a web application that allows users to add, view, update, and delete student records efficiently.",
                "live_url": "https://student-management.example.com",
                "github_url": "https://github.com/username/student-management",
                "image_url": "https://example.com/images/student-management.png",
                "featured": False}]
        return JsonResponse(data, safe=False)
class SkillsView(View):
    def get(self,request):
        data=[{
            "id": 1,
            "skill_name": "Python",
            "category": "Programming Language",
            "proficiency": "Advanced",
            "years_of_experience": 1},
            {
                "id": 2,
                "skill_name": "Django",
                "category": "Web Framework",
                "proficiency": "Intermediate",
                "years_of_experience": 2},
            {
                "id": 3,
                "skill_name": "MySQL",
                "category": "Database",
                "proficiency": "Intermediate",
                "years_of_experience": 3}]
        return JsonResponse(data,safe=False)
class ExperienceView(View):
    def get(self,request):
        data=[
            {"id":1,
            "job title":"Software Developer",
            "company name":"ABC Technologies",
            "location":"Kochi,Kerala",
            "employment type":"Permanent",
            "start date":9/12/2022,
            "end date":12/4/2023,
            "currently working":True,
            "description":"I am a passioante employee"},
            {"id": 2,
            "job title": "Python Developer",
            "company name": "Tech Solutions Pvt Ltd",
            "location": "Thrissur,Kerala",
            "employment type": "Full-time",
            "start date": 15/11/2024,
            "end date": 30/16/2025,
            "currently working": False,
            "description": "Worked on Python applications and developed backend features."},
            {"id": 3,
            "job title": "Web Developer",
            "company name": "Digital Innovations",
            "location": "Bangalore, Karnataka",
            "employment type": "Full-time",
            "start date": 11/17/2025,
            "end date": 22/12/2026,
            "currently working": True,
            "description": "Developing responsive web applications and maintaining existing projects."}]
        return JsonResponse(data,safe=False)    
class CertificationView(View):
    def get(self,request):
        data=[
            {"id":1,
            "certification name":"Python developer",
            "organization name":"oracle",
            "issued date":12/2/2022},
            {"id":2,
            "certification name":"Java developer",
            "organization name":"oracle",
            "issued date":10/2/2023},
            {"id":3,
            "certification name":"MySQL",
            "organization name":"oracle",
            "issued date":11/2/2025},]
        return JsonResponse(data,safe=False)
class ServiceView(View):
    def get(self,request):
        data=[
            {"id":1,
            "service name":"web development",
            "Description":"i am a good passionate developer",
            "technologies":"django",
            "contact information":"djangowipro@gmail.com"},
            {"id":2,
            "service name":"Application Developer",
            "Description":"i am a good passionate developer",
            "technologies":"Flask",
            "contact information":"djangowipro@gmail.com"},
            {"id":1,
            "service name":"Frontend",
            "Description":"i am a good passionate developer",
            "technologies":"django",
            "contact information":"djangowipro@gmail.com"},]
        return JsonResponse(data,safe=False)

        