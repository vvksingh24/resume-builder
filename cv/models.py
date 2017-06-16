from django.db import models


def upload(instance,filename):
	return "%s/%s"%(instance.id,filename)

class CV(models.Model):
	name=models.CharField(max_length=50,blank=False)
	phone_no=models.IntegerField()
	email_id=models.EmailField()
	photo=models.ImageField(upload_to=upload,null=True,height_field='height', width_field='width',blank=True)
	height=models.IntegerField(default=0)
	width=models.IntegerField(default=0)
	about_you=models.TextField(max_length=250)
	hobbies_and_intrests=models.TextField(blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	profile=models.CharField(max_length=200)
	def __str__(self):
		return self.name
	# skills=models.CharField(max_length=300)
	# education=models.TextField()
	# achievements=models.TextField(,null=True)

class EQ(models.Model):
	cv=models.ForeignKey(CV,on_delete=models.CASCADE,related_name='education')	
	graduation="Graduation"
	senior_secondary="XII Senior Secondary"
	secondary="X Secondary"
	post_graduation="Post Graduation"
	phd="PHD"
	diploma="Diploma"
	courses=(
		(secondary,"Secondary"),
		(senior_secondary,"XII Senior Secondary"),
		(diploma,"Diploma"),
		(graduation,"Graduation"),
		(post_graduation,"Post Graduation"),
		(phd,"PHD")
		)
	course=models.CharField(max_length=30,choices=courses)
	instute_name=models.CharField(max_length=100)
	stream=models.CharField(max_length=50)
	percentage=models.IntegerField()

class Achieve(models.Model):
	cv=models.ForeignKey(CV,on_delete=models.CASCADE,related_name='achievements')
	achievements=models.CharField(max_length=300)

class Skill(models.Model):
	cv=models.ForeignKey(CV,on_delete=models.CASCADE,related_name='skills')
	skill=models.CharField(max_length=30)
	level=models.IntegerField()


class WE(models.Model):
	work_experience=models.ForeignKey(CV,on_delete=models.CASCADE,related_name='work_experience')
	organisation=models.CharField(max_length=50)
	designation=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	years=models.IntegerField()
