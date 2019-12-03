from django.db import models


class Table(models.Model):
	name=models.CharField('name',max_length=20,default='')
	def __str__(self):
		return self.name

class Roles(models.Model):
	name=models.CharField('name',max_length=20,default='')
	def __str__(self):
		return self.name

class Departments(models.Model):
	name=models.CharField('name',max_length=20,default='')	
	def __str__(self):
		return self.name

class Users(models.Model):
	name=models.CharField('name',max_length=20,default='')
	surname=models.CharField('surname',max_length=20,default='')
	login=models.CharField('login',max_length=20,default='')
	password=models.CharField('password',max_length=20,default='')
	email=models.CharField('email',max_length=20,default='')
	roleid=models.ForeignKey(Roles,on_delete=models.CASCADE, default='')
	date=models.DateField('dateofadd',max_length=20,default='')
	phone=models.PositiveIntegerField('phone',default='')




class Meal_Categories(models.Model):
	name=models.CharField('name',max_length=20,default='')
	departmentid=models.ForeignKey(Departments,on_delete=models.CASCADE, default='')	


class Statuses(models.Model):
	name=models.CharField('name',max_length=20,default='')

class ServicePercentage(models.Model):
	percentage=models.ForeignKey(Statuses,on_delete=models.CASCADE, default='')

class Meals(models.Model):
	name=models.CharField('name',max_length=20,default='')
	categoryid=models.ForeignKey(Meal_Categories,on_delete=models.CASCADE, default='')
	price=models.PositiveIntegerField('price',default='')
	description=models.CharField('description',max_length=20,default='')
	def __str__(self):
		return self.name

'''class Orders(models.Model):
	tableid=models.ForeignKey(Table,on_delete=models.CASCADE, default='')
	meals=models.ManyToManyField(Meals)

class Checks(models.Model):
	orderid=models.ForeignKey(Orders,on_delete=models.CASCADE, default='')
	date=models.DateField('date',max_length=20,default='')
	servicefee=models.PositiveIntegerField('servicefee',default='')
	totalsum=models.PositiveIntegerField('totalsum',default='')
	meals=models.ManyToManyField(Meals)

class Meals_to_order(models.Model):
	orderid=models.ForeignKey(Orders,on_delete=models.CASCADE, default='')
	meals=models.ManyToManyField(Meals)

'''