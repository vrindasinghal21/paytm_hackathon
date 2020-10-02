from django.db import models

# Create your models here.
# class Data(models.Model):
#     name = models.CharField(max_length=250)
#     mobile = models.IntegerField()
#     password = models.CharField(max_length=250,default='KIET123')
class Signin(models.Model):
	name = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	uniq_id = models.AutoField(primary_key=True)
	mobile = models.BigIntegerField()
	password = models.CharField(max_length=250,default='KIET123')
	email = models.CharField(max_length=250, null=True)
	# address = models.CharField(max_length=500,null=True)

class Dropdown(models.Model):
	uniq_id = models.AutoField(primary_key=True)
	field=models.TextField()
	value=models.TextField()
	uid=models.IntegerField(blank=True,null=True,default=0)

class Materials(models.Model):
	auto_id = models.AutoField(primary_key=True)
	added_by = models.ForeignKey(Signin,null=True,on_delete=models.SET_NULL)
	material=models.ForeignKey(Dropdown,null=True,on_delete=models.SET_NULL)
	category =models.TextField(default=None)
	sub_category =models.TextField(default=None)
	authsize =models.TextField()
	status =models.CharField(max_length=25000,default='INSERT')
	quantity =models.IntegerField(blank=True,null=True,default=0)
	standardsize =models.IntegerField(blank=True,null=True,default=0)

	

class Request(models.Model):
   
	# auto_id=models.AutoField(primary_key=True)
	user_id_added_by_uniq_id=models.ForeignKey(Materials,null=True,on_delete=models.SET_NULL)
	govt_id=models.ForeignKey(Signin,null=True,on_delete=models.SET_NULL)
	time_stamp=models.DateTimeField(auto_now=True)
	approval_status=models.CharField(max_length=10,default='PENDING')
	required=models.IntegerField(blank=True,null=True,default=0)



# class count(models.Model):
#     material_id=models.ForeignKey(Materials,null=True,on_delete=models.SET_NULL)
#     up=models.IntegerField(blank=True,null=True,default=0)
#     down=models.IntegerField(blank=True,null=True,default=0)

# class Report(models.Model):
#     report=models.IntegerField(blank=True,null=True)
#     answer_id=models.ForeignKey(Answer,null=True,on_delete=models.SET_NULL)

# class Pending(models.Model):
	
#     description=models.TextField()
#     blog_id=models.AutoField(primary_key=True)
#     added_by=models.ForeignKey(Signin,null=True,on_delete=models.SET_NULL)
#     time_stamp=models.DateTimeField(auto_now=True)
#     status=models.CharField(max_length=10,default='INSERT')


