from django.db import models

class DepartmentModel(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 255,null=True)
	description = models.TextField(null = True)
	def __str__(self):
         return self.name

class DocumentTypeModel(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField( max_length = 255,null=True)
	description = models.TextField(max_length = 255 ,null=True)
	def __str__(self):
         return self.name

class DesignationModel(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField( max_length = 255,null=True)
	description = models.TextField(null=True)	
	def __str__(self):
         return self.name

class EmployeeGrade(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField( max_length = 255,null=True)
	description = models.TextField(null=True)	
	def __str__(self):
         return self.name

class EmployeeStatus(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField( max_length = 255,null=True)
	description = models.TextField(null=True)		
	def __str__(self):
         return self.name

class EmployeeType(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField( max_length = 255,null=True)
	description = models.TextField(null=True)	
	def __str__(self):
         return self.name	

