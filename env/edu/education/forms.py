from django import forms 
 
#creating our forms



from .models import *
class courseform(forms.ModelForm):
    class Meta:
        model= course
        fields= ["department","name",]

class semesterform(forms.ModelForm):
    class Meta:
        model= semester
        fields= ["semname","coursename","departmentname",]


class subjectform(forms.ModelForm):
    class Meta:
        model= subject
        fields= ["departmentname","subjectname","coursename","semester",]



class studform(forms.ModelForm):
    class Meta:
        model= student
        fields= ["username","password",]



class parentform(forms.ModelForm):
    class Meta:
        model= student
        fields= ["parentname","gender","std_name","deptname","coursename","emailid","semester","joindate","admno", "address" ,"contactno", ]


class markform1(forms.ModelForm):
    class Meta:
        model= marks
        fields= ["semester","studentname",]

class markform(forms.ModelForm):
    class Meta:
        model= marks
        fields= ["semester","studentname","coursename","departmentname","examname","avmarks","remarks", ]

class attendanceform(forms.ModelForm):
    class Meta:
        model= attendance
        fields= ["department","semester","studentname","coursename","subjectname1","subjectname2","subjectname3", "subjectname4" ,"subjectname5","Subjectname6","Subjectname7","attsub1","attsub2","attsub3","attsub4","attsub5","attsub6","attsub7"]

class attendanceform2(forms.ModelForm):
    class Meta:
        model= attendance
        fields= ["department","semester","coursename",]


class attendanceform3(forms.ModelForm):
    class Meta:
        model= attendance
        fields= ["department","coursename",]


class departmentform(forms.ModelForm):
    class Meta:
        model= department
        fields= ["departmentname",]


