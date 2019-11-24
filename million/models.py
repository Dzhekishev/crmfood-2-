from django.db import models


class Table(models.Model):
	name=models.CharField('name',max_length=20,default='')

class Roles(models.Model):
	name=models.CharField('name',max_length=20,default='')

class Departments(models.Model):
	name=models.CharField('name',max_length=20,default='')	
	

class Users(models.Model):
	name=models.CharField('name',max_length=20,default='')
	surname=models.CharField('surname',max_length=20,default='')
	email=models.CharField('email',max_length=20,default='')
	roleid=models.PositiveIntegerField('roleid',default='')
	phone=models.PositiveIntegerField('phone',default='')


class Meal_Categories(models.Model):
	name=models.CharField('place of concert',max_length=20,default='')
	departmentid=ManyToManyField(Departments)	


class Statuses(models.Model):
	name=models.CharField('name',max_length=20,default='')

class ServicePercentage(models.Model):
	percentage=models.PositiveIntegerField('percentage',default='')

class Meals(models.Model):
	name=models.CharField('name',max_length=20,default='')
	categoryid=ManyToManyField(Meal Categories)
	price=models.PositiveIntegerField('price',default='')
	description=models.CharField('description',max_length=20,default='')


class Orders(models.Model):
	tableid=models.PositiveIntegerField('tableid',default='')
	meals=ManyToManyField(Meals)

class Checks(models.Model):
	orderid=models.PositiveIntegerField('orderid',default='')
	date=models.DateField('date',max_length=20,default='')
	servicefee=models.PositiveIntegerField('servicefee',default='')
	totalsum=models.PositiveIntegerField('totalsum',default='')
	meals=ManyToManyField(Meals)

class Meals_to_order(models.Model):
	orderid=models.PositiveIntegerField('orderd',default='')
	meals=ManyToManyField(Meals)

